# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import ipc_pb2 as ipc__pb2


class ExecutionEngineServiceStub(object):
  """Definition of the service.
  ExecutionEngine implements server part while Consensus implements client part.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.commit = channel.unary_unary(
        '/io.casperlabs.ipc.ExecutionEngineService/commit',
        request_serializer=ipc__pb2.CommitRequest.SerializeToString,
        response_deserializer=ipc__pb2.CommitResponse.FromString,
        )
    self.query = channel.unary_unary(
        '/io.casperlabs.ipc.ExecutionEngineService/query',
        request_serializer=ipc__pb2.QueryRequest.SerializeToString,
        response_deserializer=ipc__pb2.QueryResponse.FromString,
        )
    self.validate = channel.unary_unary(
        '/io.casperlabs.ipc.ExecutionEngineService/validate',
        request_serializer=ipc__pb2.ValidateRequest.SerializeToString,
        response_deserializer=ipc__pb2.ValidateResponse.FromString,
        )
    self.execute = channel.unary_unary(
        '/io.casperlabs.ipc.ExecutionEngineService/execute',
        request_serializer=ipc__pb2.ExecuteRequest.SerializeToString,
        response_deserializer=ipc__pb2.ExecuteResponse.FromString,
        )
    self.run_genesis = channel.unary_unary(
        '/io.casperlabs.ipc.ExecutionEngineService/run_genesis',
        request_serializer=ipc__pb2.ChainSpec.GenesisConfig.SerializeToString,
        response_deserializer=ipc__pb2.GenesisResponse.FromString,
        )
    self.upgrade = channel.unary_unary(
        '/io.casperlabs.ipc.ExecutionEngineService/upgrade',
        request_serializer=ipc__pb2.UpgradeRequest.SerializeToString,
        response_deserializer=ipc__pb2.UpgradeResponse.FromString,
        )


class ExecutionEngineServiceServicer(object):
  """Definition of the service.
  ExecutionEngine implements server part while Consensus implements client part.
  """

  def commit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def validate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def execute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def run_genesis(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def upgrade(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExecutionEngineServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'commit': grpc.unary_unary_rpc_method_handler(
          servicer.commit,
          request_deserializer=ipc__pb2.CommitRequest.FromString,
          response_serializer=ipc__pb2.CommitResponse.SerializeToString,
      ),
      'query': grpc.unary_unary_rpc_method_handler(
          servicer.query,
          request_deserializer=ipc__pb2.QueryRequest.FromString,
          response_serializer=ipc__pb2.QueryResponse.SerializeToString,
      ),
      'validate': grpc.unary_unary_rpc_method_handler(
          servicer.validate,
          request_deserializer=ipc__pb2.ValidateRequest.FromString,
          response_serializer=ipc__pb2.ValidateResponse.SerializeToString,
      ),
      'execute': grpc.unary_unary_rpc_method_handler(
          servicer.execute,
          request_deserializer=ipc__pb2.ExecuteRequest.FromString,
          response_serializer=ipc__pb2.ExecuteResponse.SerializeToString,
      ),
      'run_genesis': grpc.unary_unary_rpc_method_handler(
          servicer.run_genesis,
          request_deserializer=ipc__pb2.ChainSpec.GenesisConfig.FromString,
          response_serializer=ipc__pb2.GenesisResponse.SerializeToString,
      ),
      'upgrade': grpc.unary_unary_rpc_method_handler(
          servicer.upgrade,
          request_deserializer=ipc__pb2.UpgradeRequest.FromString,
          response_serializer=ipc__pb2.UpgradeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.casperlabs.ipc.ExecutionEngineService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
