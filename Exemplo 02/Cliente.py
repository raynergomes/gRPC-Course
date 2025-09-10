import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # NOTE(gRPC): the `close()` call is optional. Since in this example we
    # are about to exit the program, it is omitted to simplify the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='Hello gRPC!'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()