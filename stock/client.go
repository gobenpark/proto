package stock

import (
	"context"
	"google.golang.org/grpc"
)

//Generate stockclient
func NewSocketClient(ctx context.Context, url string) (StockClient, error) {
	cli, err := grpc.DialContext(ctx, url, grpc.WithInsecure())
	if err != nil {
		return nil, err
	}
	return NewStockClient(cli), nil
}
