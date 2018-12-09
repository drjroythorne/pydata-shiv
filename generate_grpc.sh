#!/bin/bash

python -m grpc_tools.protoc -Iproto --python_out=. --python_grpc_out=. pydata_shiv/prediction.proto
