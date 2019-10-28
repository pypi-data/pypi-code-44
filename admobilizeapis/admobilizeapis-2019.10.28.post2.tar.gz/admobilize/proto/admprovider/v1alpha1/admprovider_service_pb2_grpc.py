# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from admobilize.proto.admprovider.v1alpha1 import admprovider_service_pb2 as admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2
from admobilize.proto.admprovider.v1alpha1 import resources_pb2 as admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2
from admobilize.proto.vision.v1 import vision_pb2 as admobilize_dot_vision_dot_v1_dot_vision__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AdmproviderServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Provision = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/Provision',
        request_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.ProvisionRequest.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.ProvisionResponse.FromString,
        )
    self.StreamLogs = channel.unary_stream(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/StreamLogs',
        request_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.StreamLogsRequest.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.StreamLogsResponse.FromString,
        )
    self.StreamState = channel.unary_stream(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/StreamState',
        request_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.StreamStateRequest.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.State.FromString,
        )
    self.StreamFrames = channel.unary_stream(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/StreamFrames',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Frame.FromString,
        )
    self.StreamDetections = channel.unary_stream(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/StreamDetections',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=admobilize_dot_vision_dot_v1_dot_vision__pb2.VisionResult.FromString,
        )
    self.GetState = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/GetState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.State.FromString,
        )
    self.GetStatus = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/GetStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.GetStatusResponse.FromString,
        )
    self.Run = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/Run',
        request_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Configuration.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/SetConfig',
        request_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Configuration.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/GetConfig',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Configuration.FromString,
        )
    self.SendCommand = channel.unary_unary(
        '/admobilize.admprovider.v1alpha1.AdmproviderService/SendCommand',
        request_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.SendCommandRequest.SerializeToString,
        response_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.SendCommandResponse.FromString,
        )


class AdmproviderServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Provision(self, request, context):
    """Provision a new device
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamLogs(self, request, context):
    """Stream admprovider and/or malos-vision logs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamState(self, request, context):
    """Stream state data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamFrames(self, request, context):
    """Stream frames from camera
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamDetections(self, request, context):
    """Stream detections
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    """Get state data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStatus(self, request, context):
    """Get general application status data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Run(self, request, context):
    """Run admprovider
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfig(self, request, context):
    """Set config
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfig(self, request, context):
    """Get config
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendCommand(self, request, context):
    """Send command
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdmproviderServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Provision': grpc.unary_unary_rpc_method_handler(
          servicer.Provision,
          request_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.ProvisionRequest.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.ProvisionResponse.SerializeToString,
      ),
      'StreamLogs': grpc.unary_stream_rpc_method_handler(
          servicer.StreamLogs,
          request_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.StreamLogsRequest.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.StreamLogsResponse.SerializeToString,
      ),
      'StreamState': grpc.unary_stream_rpc_method_handler(
          servicer.StreamState,
          request_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.StreamStateRequest.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.State.SerializeToString,
      ),
      'StreamFrames': grpc.unary_stream_rpc_method_handler(
          servicer.StreamFrames,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Frame.SerializeToString,
      ),
      'StreamDetections': grpc.unary_stream_rpc_method_handler(
          servicer.StreamDetections,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=admobilize_dot_vision_dot_v1_dot_vision__pb2.VisionResult.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.State.SerializeToString,
      ),
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.GetStatusResponse.SerializeToString,
      ),
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Configuration.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Configuration.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_resources__pb2.Configuration.SerializeToString,
      ),
      'SendCommand': grpc.unary_unary_rpc_method_handler(
          servicer.SendCommand,
          request_deserializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.SendCommandRequest.FromString,
          response_serializer=admobilize_dot_admprovider_dot_v1alpha1_dot_admprovider__service__pb2.SendCommandResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'admobilize.admprovider.v1alpha1.AdmproviderService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
