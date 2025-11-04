import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import time
from concurrent import futures
import requests


# Definição do serviço Greeter
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message=f'Hello, {request.name}!')


# Função para iniciar o servidor gRPC e registrá-lo
def serve():
    server_port = 50051
    server_address = f'[::]:{server_port}'
    registry_url = 'http://localhost:8000/register'

    # Cria o servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(server_address)
    server.start()
    print(f"Server started, listening on port {server_port}")

    # Registra o serviço no registry-server
    service_data = {
        'name': 'greeter_service',
        'ip': '127.0.0.1',
        'port': server_port
    }
    try:
        response = requests.post(registry_url, json=service_data)
        if response.status_code == 200:
            print("Serviço registrado com sucesso no servidor de registro!")
        else:
            print(
                f"Falha ao registrar o serviço. Status: {response.status_code}, Erro: {response.json().get('error', 'N/A')}")
    except requests.exceptions.ConnectionError:
        print(
            "Erro: Não foi possível conectar ao servidor de registro. Verifique se ele está em execução na porta 8000.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
