.PHONEY: upload proto-go proto-python

upload:
	python setup.py sdist bdist_wheel
	python -m twine upload --skip-existing dist/*

proto-python:
	python -m grpc_tools.protoc -I=. \
         -I=${GOPATH}/src/swit \
         -I=${GOPATH}/src \
         -I=${GOPATH}/src/github.com  \
         -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
         -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
         -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway --python_out=. --grpc_python_out=. ./stock/stock.proto

proto-go:
	protoc -I=. \
     -I=${GOPATH}/src \
     -I=${GOPATH}/bin \
     -I=${GOPATH}/src/github.com  \
     -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate --validate_out="lang=go:." \
     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway \
     --grpc-gateway_out=logtostderr=true:.\
     --gogoslick_out=\
Mgoogle/protobuf/empty.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/any.proto=github.com/gogo/protobuf/types,\
Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,plugins=grpc:. ./stock/stock.proto

all: proto-go proto-python upload