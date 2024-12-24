PROTO_SRC=protos/glossary.proto
PY_OUT=.

gen:
	python -m grpc_tools.protoc \
		--proto_path=protos \
		--python_out=$(PY_OUT) \
		--grpc_python_out=$(PY_OUT) \
		$(PROTO_SRC)
