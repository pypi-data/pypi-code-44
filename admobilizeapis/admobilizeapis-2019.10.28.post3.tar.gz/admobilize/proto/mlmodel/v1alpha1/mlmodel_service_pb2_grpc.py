# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from admobilize.proto.mlmodel.v1alpha1 import mlmodel_service_pb2 as admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class MLModelServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateModels = channel.unary_unary(
        '/admobilize.mlmodel.v1alpha1.MLModelService/CreateModels',
        request_serializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.CreateModelsRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetModels = channel.unary_unary(
        '/admobilize.mlmodel.v1alpha1.MLModelService/GetModels',
        request_serializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.GetModelsRequest.SerializeToString,
        response_deserializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.GetModelsResponse.FromString,
        )
    self.DeleteModels = channel.unary_unary(
        '/admobilize.mlmodel.v1alpha1.MLModelService/DeleteModels',
        request_serializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.DeleteModelsRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class MLModelServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateModels(self, request, context):
    """Create a set of Models in the API
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModels(self, request, context):
    """Obtain a set of specific Models matching from the API
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteModels(self, request, context):
    """Delete a set of Models from the API
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MLModelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateModels': grpc.unary_unary_rpc_method_handler(
          servicer.CreateModels,
          request_deserializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.CreateModelsRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetModels': grpc.unary_unary_rpc_method_handler(
          servicer.GetModels,
          request_deserializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.GetModelsRequest.FromString,
          response_serializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.GetModelsResponse.SerializeToString,
      ),
      'DeleteModels': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteModels,
          request_deserializer=admobilize_dot_mlmodel_dot_v1alpha1_dot_mlmodel__service__pb2.DeleteModelsRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'admobilize.mlmodel.v1alpha1.MLModelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
