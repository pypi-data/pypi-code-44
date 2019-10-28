# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/vision/v1/vision_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from admobilize.proto.vision.v1 import vision_pb2 as admobilize_dot_vision_dot_v1_dot_vision__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admobilize/vision/v1/vision_service.proto',
  package='admobilize.vision.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.admobilize.proto.vision.v1B\022VisionServiceProtoP\001Z8bitbucket.org/admobilize/admobilizeapis-go/pkg/vision/v1\252\002\024AdMobilize.Vision.V1'),
  serialized_pb=_b('\n)admobilize/vision/v1/vision_service.proto\x12\x14\x61\x64mobilize.vision.v1\x1a!admobilize/vision/v1/vision.proto\"\xcd\x02\n\rVisionRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\x39\n\tdetection\x18\x02 \x03(\x0e\x32&.admobilize.vision.v1.EnumDetectionTag\x12\x43\n\x0brecognition\x18\x03 \x03(\x0e\x32..admobilize.vision.v1.EnumFacialRecognitionTag\x12L\n\x13vehicle_recognition\x18\x06 \x03(\x0e\x32/.admobilize.vision.v1.EnumVehicleRecognitionTag\x12\x33\n\nimage_list\x18\x04 \x01(\x0b\x32\x1f.admobilize.vision.v1.ImageList\x12*\n\x05video\x18\x05 \x01(\x0b\x32\x1b.admobilize.vision.v1.Video2j\n\rVisionService\x12Y\n\x0cProcessImage\x12#.admobilize.vision.v1.VisionRequest\x1a\".admobilize.vision.v1.VisionResult\"\x00\x42\x87\x01\n\x1e\x63om.admobilize.proto.vision.v1B\x12VisionServiceProtoP\x01Z8bitbucket.org/admobilize/admobilizeapis-go/pkg/vision/v1\xaa\x02\x14\x41\x64Mobilize.Vision.V1b\x06proto3')
  ,
  dependencies=[admobilize_dot_vision_dot_v1_dot_vision__pb2.DESCRIPTOR,])




_VISIONREQUEST = _descriptor.Descriptor(
  name='VisionRequest',
  full_name='admobilize.vision.v1.VisionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='admobilize.vision.v1.VisionRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection', full_name='admobilize.vision.v1.VisionRequest.detection', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recognition', full_name='admobilize.vision.v1.VisionRequest.recognition', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_recognition', full_name='admobilize.vision.v1.VisionRequest.vehicle_recognition', index=3,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_list', full_name='admobilize.vision.v1.VisionRequest.image_list', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video', full_name='admobilize.vision.v1.VisionRequest.video', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=436,
)

_VISIONREQUEST.fields_by_name['detection'].enum_type = admobilize_dot_vision_dot_v1_dot_vision__pb2._ENUMDETECTIONTAG
_VISIONREQUEST.fields_by_name['recognition'].enum_type = admobilize_dot_vision_dot_v1_dot_vision__pb2._ENUMFACIALRECOGNITIONTAG
_VISIONREQUEST.fields_by_name['vehicle_recognition'].enum_type = admobilize_dot_vision_dot_v1_dot_vision__pb2._ENUMVEHICLERECOGNITIONTAG
_VISIONREQUEST.fields_by_name['image_list'].message_type = admobilize_dot_vision_dot_v1_dot_vision__pb2._IMAGELIST
_VISIONREQUEST.fields_by_name['video'].message_type = admobilize_dot_vision_dot_v1_dot_vision__pb2._VIDEO
DESCRIPTOR.message_types_by_name['VisionRequest'] = _VISIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VisionRequest = _reflection.GeneratedProtocolMessageType('VisionRequest', (_message.Message,), {
  'DESCRIPTOR' : _VISIONREQUEST,
  '__module__' : 'admobilize.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.vision.v1.VisionRequest)
  })
_sym_db.RegisterMessage(VisionRequest)


DESCRIPTOR._options = None

_VISIONSERVICE = _descriptor.ServiceDescriptor(
  name='VisionService',
  full_name='admobilize.vision.v1.VisionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=438,
  serialized_end=544,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessImage',
    full_name='admobilize.vision.v1.VisionService.ProcessImage',
    index=0,
    containing_service=None,
    input_type=_VISIONREQUEST,
    output_type=admobilize_dot_vision_dot_v1_dot_vision__pb2._VISIONRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VISIONSERVICE)

DESCRIPTOR.services_by_name['VisionService'] = _VISIONSERVICE

# @@protoc_insertion_point(module_scope)
