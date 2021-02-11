
from concurrent import futures
from stock import stock_pb2_grpc
from stock import stock_pb2

import grpc

class StockServer(stock_pb2_grpc.StockServicer):
    def Account(self, request, context):
        print(request)
        return stock_pb2.AccountReply(info="hello")

    def Tick(self, request, context):
        pass

    def Chart(self, request, context):
        pass


    def Accounts(self, request, context):
        pass

    def Buy(self, request, context):
        pass

    def Sell(self, request, context):
        pass


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_pb2_grpc.add_StockServicer_to_server(StockServer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


