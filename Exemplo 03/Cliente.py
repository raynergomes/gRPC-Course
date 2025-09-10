import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import requests
import sys


def run():
    # URL do servidor de registro para descobrir o serviço 'greeter_service'
    registry_url = 'http://localhost:8000/discover/greeter_service'
    print("Procurando o endereço do servidor no registro...")

    try:
        response = requests.get(registry_url)
        if response.status_code == 200:
            address_data = response.json()
            server_address = address_data.get('address')
            print(f"Endereço do servidor encontrado: {server_address}")
        else:
            print("Erro: Servidor 'greeter_service' não encontrado no registro.")
            sys.exit(1)  # Sai do programa em caso de erro

    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor de registro.")
        print("Certifique-se de que o servidor de registro está em execução na porta 8000.")
        sys.exit(1)  # Sai do programa em caso de erro

    # Inicia a conexão gRPC usando o endereço obtido do registro
    with grpc.insecure_channel(server_address) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        try:
            response = stub.SayHello(helloworld_pb2.HelloRequest(name='Hello gRPC!'))
            print("Greeter client received: " + response.message)
        except grpc.RpcError as e:
            print(f"Erro gRPC: {e.details()}")

if __name__ == '__main__':
    run()
