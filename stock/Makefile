include ../Makefile

GOPATH:="/Users/ben/go"

.PHONEY: proto-go proto-python

proto-go:
	protoc -I=. \
     -I=${GOPATH}/src/swit \
     -I=${GOPATH}/src \
     -I=${GOPATH}/src/github.com  \
     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
     -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate --validate_out="lang=go:." \
     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway \
     -I=${GOPATH}/src/swit/swit-grpc-library-golang \
     --grpc-gateway_out=logtostderr=true:.\
     --gogofast_out=\
Mgoogle/protobuf/empty.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/any.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,plugins=grpc:. ./stock.proto
#Mswit-grpc-library-golang/protos/message.alpha/model.proto=golang.swit.dev/grpc/protos/message.alpha,\
#Mswit-grpc-library-golang/protos/message.alpha/swagger/annotations.proto=golang.swit.dev/grpc/protos/message.alpha,\
Mswit/swit-grpc-message-golang/proto/swagger/openapiv2.proto=golang.swit.dev/grpc/protos/message.alpha,plugins=grpc:. ./message.proto ./model.proto


proto-python:
	python -m grpc_tools.protoc -I=. \
         -I=${GOPATH}/src/swit \
         -I=${GOPATH}/src \
         -I=${GOPATH}/src/github.com  \
         -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
         -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
         -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway --python_out=. --grpc_python_out=. stock.proto