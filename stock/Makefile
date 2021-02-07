include ../Makefile

.PHONEY: proto

proto:
	protoc -I=. \
     -I=${GOPATH}/src/swit \
     -I=${GOPATH}/src \
     -I=${GOPATH}/src/github.com  \
     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
     -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate --validate_out="lang=go:." \
     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway \
     -I=${GOPATH}/src/swit/swit-grpc-library-golang \
     -I=${GOPATH}/src/swit/swit-grpc-library-golang/protos/apps/v4/swagger \
     --swagger_out=logtostderr=true:./swagger \
     --grpc-gateway_out=logtostderr=true:.\
     --gogofast_out=\
Mprotos/reaction/v5/model.proto=golang.swit.dev/grpc/protos/reaction/v5,\
Mgoogle/protobuf/empty.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/any.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/struct.proto=github.com/gogo/protobuf/types,\
Mswit/swit-grpc-library-golang/protos/response/response.proto=golang.swit.dev/grpc/protos/response,plugins=grpc:. ./store.googlecalendar.proto
#Mswit-grpc-library-golang/protos/message.alpha/model.proto=golang.swit.dev/grpc/protos/message.alpha,\
#Mswit-grpc-library-golang/protos/message.alpha/swagger/annotations.proto=golang.swit.dev/grpc/protos/message.alpha,\
Mswit/swit-grpc-message-golang/proto/swagger/openapiv2.proto=golang.swit.dev/grpc/protos/message.alpha,plugins=grpc:. ./message.proto ./model.proto