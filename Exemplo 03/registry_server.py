from flask import Flask, request, jsonify
app = Flask(__name__)
services = {}

@app.route('/index', methods=['GET'])
def index():
    saida = ""
    for name, service in services.items():
        saida += f"{name}:{service}"
    return jsonify(saida), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    port = data.get('port')
    if not name or not port:
        return jsonify({"error": "Nome e porta são obrigatórios."}), 400

    services[name] = f"localhost:{port}"
    return jsonify({"message": f"Serviço '{name}' registrado em localhost:{port}"}), 200

@app.route('/discover/<name>', methods=['GET'])
def discover(name):
    address = services.get(name)
    if address:
        return jsonify({"address": address}), 200
    return jsonify({"error": "Serviço não encontrado."}), 404

if __name__ == '__main__':
    app.run(port=8000, debug=True)