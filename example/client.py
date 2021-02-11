
import grpc
from stock import stock_pb2
from stock import stock_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = stock_pb2_grpc.StockStub(channel)
    response = stub.Account(stock_pb2.AccountRequest(account="h"))
    print(response)

if __name__ == '__main__':
    run()