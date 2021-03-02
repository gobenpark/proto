# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from stock import stock_pb2 as stock_dot_stock__pb2


class StockStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AllMarkets = channel.unary_unary(
                '/stock.Stock/AllMarkets',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.AllMarketsReply.FromString,
                )
        self.Account = channel.unary_unary(
                '/stock.Stock/Account',
                request_serializer=stock_dot_stock__pb2.AccountRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.AccountReply.FromString,
                )
        self.TickStream = channel.unary_stream(
                '/stock.Stock/TickStream',
                request_serializer=stock_dot_stock__pb2.TickRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.TickReply.FromString,
                )
        self.Chart = channel.unary_unary(
                '/stock.Stock/Chart',
                request_serializer=stock_dot_stock__pb2.ChartRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.ChartReply.FromString,
                )
        self.Accounts = channel.unary_unary(
                '/stock.Stock/Accounts',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.AccountsReply.FromString,
                )
        self.Buy = channel.unary_unary(
                '/stock.Stock/Buy',
                request_serializer=stock_dot_stock__pb2.BuyRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.BuyReply.FromString,
                )
        self.Sell = channel.unary_unary(
                '/stock.Stock/Sell',
                request_serializer=stock_dot_stock__pb2.SellRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.SellReply.FromString,
                )
        self.OrderList = channel.unary_unary(
                '/stock.Stock/OrderList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.OrderListReply.FromString,
                )
        self.CancelOrder = channel.unary_unary(
                '/stock.Stock/CancelOrder',
                request_serializer=stock_dot_stock__pb2.CancelOrderRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TradeStream = channel.unary_stream(
                '/stock.Stock/TradeStream',
                request_serializer=stock_dot_stock__pb2.TradeStreamRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.TradeStreamReply.FromString,
                )
        self.OrderBookStream = channel.unary_stream(
                '/stock.Stock/OrderBookStream',
                request_serializer=stock_dot_stock__pb2.OrderBookStreamRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.OrderBookStreamReply.FromString,
                )
        self.Order = channel.unary_unary(
                '/stock.Stock/Order',
                request_serializer=stock_dot_stock__pb2.OrderRequest.SerializeToString,
                response_deserializer=stock_dot_stock__pb2.OrderReply.FromString,
                )


class StockServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AllMarkets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Account(self, request, context):
        """특정 소유하고 있는 주식,코인 정보
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TickStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Chart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Accounts(self, request, context):
        """모든 소유하고 있는 주식, 코인정보
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Buy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sell(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TradeStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderBookStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Order(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AllMarkets': grpc.unary_unary_rpc_method_handler(
                    servicer.AllMarkets,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=stock_dot_stock__pb2.AllMarketsReply.SerializeToString,
            ),
            'Account': grpc.unary_unary_rpc_method_handler(
                    servicer.Account,
                    request_deserializer=stock_dot_stock__pb2.AccountRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.AccountReply.SerializeToString,
            ),
            'TickStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TickStream,
                    request_deserializer=stock_dot_stock__pb2.TickRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.TickReply.SerializeToString,
            ),
            'Chart': grpc.unary_unary_rpc_method_handler(
                    servicer.Chart,
                    request_deserializer=stock_dot_stock__pb2.ChartRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.ChartReply.SerializeToString,
            ),
            'Accounts': grpc.unary_unary_rpc_method_handler(
                    servicer.Accounts,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=stock_dot_stock__pb2.AccountsReply.SerializeToString,
            ),
            'Buy': grpc.unary_unary_rpc_method_handler(
                    servicer.Buy,
                    request_deserializer=stock_dot_stock__pb2.BuyRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.BuyReply.SerializeToString,
            ),
            'Sell': grpc.unary_unary_rpc_method_handler(
                    servicer.Sell,
                    request_deserializer=stock_dot_stock__pb2.SellRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.SellReply.SerializeToString,
            ),
            'OrderList': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=stock_dot_stock__pb2.OrderListReply.SerializeToString,
            ),
            'CancelOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrder,
                    request_deserializer=stock_dot_stock__pb2.CancelOrderRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'TradeStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TradeStream,
                    request_deserializer=stock_dot_stock__pb2.TradeStreamRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.TradeStreamReply.SerializeToString,
            ),
            'OrderBookStream': grpc.unary_stream_rpc_method_handler(
                    servicer.OrderBookStream,
                    request_deserializer=stock_dot_stock__pb2.OrderBookStreamRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.OrderBookStreamReply.SerializeToString,
            ),
            'Order': grpc.unary_unary_rpc_method_handler(
                    servicer.Order,
                    request_deserializer=stock_dot_stock__pb2.OrderRequest.FromString,
                    response_serializer=stock_dot_stock__pb2.OrderReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stock.Stock', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Stock(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AllMarkets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/AllMarkets',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            stock_dot_stock__pb2.AllMarketsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/Account',
            stock_dot_stock__pb2.AccountRequest.SerializeToString,
            stock_dot_stock__pb2.AccountReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TickStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stock.Stock/TickStream',
            stock_dot_stock__pb2.TickRequest.SerializeToString,
            stock_dot_stock__pb2.TickReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Chart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/Chart',
            stock_dot_stock__pb2.ChartRequest.SerializeToString,
            stock_dot_stock__pb2.ChartReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Accounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/Accounts',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            stock_dot_stock__pb2.AccountsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Buy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/Buy',
            stock_dot_stock__pb2.BuyRequest.SerializeToString,
            stock_dot_stock__pb2.BuyReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sell(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/Sell',
            stock_dot_stock__pb2.SellRequest.SerializeToString,
            stock_dot_stock__pb2.SellReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/OrderList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            stock_dot_stock__pb2.OrderListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/CancelOrder',
            stock_dot_stock__pb2.CancelOrderRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TradeStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stock.Stock/TradeStream',
            stock_dot_stock__pb2.TradeStreamRequest.SerializeToString,
            stock_dot_stock__pb2.TradeStreamReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderBookStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stock.Stock/OrderBookStream',
            stock_dot_stock__pb2.OrderBookStreamRequest.SerializeToString,
            stock_dot_stock__pb2.OrderBookStreamReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Order(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stock.Stock/Order',
            stock_dot_stock__pb2.OrderRequest.SerializeToString,
            stock_dot_stock__pb2.OrderReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
