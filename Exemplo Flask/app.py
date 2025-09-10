from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, mundo!'

if __name__ == '__main__':
    app.run()

# Como rodar:
# pip install Flask
# Salve o código acima como app.py
# flask run
