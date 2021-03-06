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

#proto-go:
#	protoc -I=. \
#     -I=${GOPATH}/src \
#     -I=${GOPATH}/bin \
#     -I=${GOPATH}/src/github.com  \
#     -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
#     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway \
#     --validate_out="lang=go,paths=source_relative:./stock"
#     --grpc-gateway_out=logtostderr=true:.\
#     --gogoslick_out=\
#Mgoogle/protobuf/empty.proto=github.com/gogo/protobuf/types,\
#Mgoogle/protobuf/any.proto=github.com/gogo/protobuf/types,\
#Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,plugins=grpc:. ./stock/stock.proto

proto-go:
	protoc -I=. \
     -I=${GOPATH}/src \
     -I=${GOPATH}/src/github.com  \
     -I=${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate --validate_out="lang=go,paths=source_relative:." \
     -I=${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway \
     --go_out . \
     --go_opt paths=source_relative \
     --go-grpc_out . \
     --go-grpc_opt paths=source_relative \
	./stock/stock.proto


all: proto-go proto-python upload
	git add .
	git commit -m "upgrade"
	git push origin master