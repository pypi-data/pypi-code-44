# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/signagelive/v1alpha1/resources.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admobilize/signagelive/v1alpha1/resources.proto',
  package='admobilize.signagelive.v1alpha1',
  syntax='proto3',
  serialized_options=_b('\n#com.admobilize.signagelive.v1alpha1B\020SignageliveProtoP\001ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/signagelive/v1alpha1\242\002\006ADMSGL\252\002\037AdMobilize.Signagelive.V1Alpha1'),
  serialized_pb=_b('\n/admobilize/signagelive/v1alpha1/resources.proto\x12\x1f\x61\x64mobilize.signagelive.v1alpha1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbd\x02\n\nCredential\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\x15\n\rclient_secret\x18\x05 \x01(\t\x12\x12\n\nauth_token\x18\x06 \x01(\t\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x14\n\x0cnum_mappings\x18\x0b \x01(\x05\x12:\n\x08mappings\x18\x0c \x03(\x0b\x32(.admobilize.signagelive.v1alpha1.Mapping\x12.\n\ncreated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf4\x01\n\x07Mapping\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rcredential_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x11\n\tdevice_id\x18\x04 \x01(\t\x12\x15\n\rserial_number\x18\x05 \x01(\t\x12\x12\n\nnetwork_id\x18\x06 \x01(\t\x12\x14\n\x0csource_table\x18\x07 \x01(\t\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\xa9\x01\n#com.admobilize.signagelive.v1alpha1B\x10SignageliveProtoP\x01ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/signagelive/v1alpha1\xa2\x02\x06\x41\x44MSGL\xaa\x02\x1f\x41\x64Mobilize.Signagelive.V1Alpha1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CREDENTIAL = _descriptor.Descriptor(
  name='Credential',
  full_name='admobilize.signagelive.v1alpha1.Credential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admobilize.signagelive.v1alpha1.Credential.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='admobilize.signagelive.v1alpha1.Credential.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='admobilize.signagelive.v1alpha1.Credential.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='admobilize.signagelive.v1alpha1.Credential.client_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_secret', full_name='admobilize.signagelive.v1alpha1.Credential.client_secret', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='admobilize.signagelive.v1alpha1.Credential.auth_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='admobilize.signagelive.v1alpha1.Credential.user_id', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_mappings', full_name='admobilize.signagelive.v1alpha1.Credential.num_mappings', index=7,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mappings', full_name='admobilize.signagelive.v1alpha1.Credential.mappings', index=8,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='admobilize.signagelive.v1alpha1.Credential.created_at', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='admobilize.signagelive.v1alpha1.Credential.updated_at', index=10,
      number=14, type=11, cpp_type=10, label=1,
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
  serialized_start=118,
  serialized_end=435,
)


_MAPPING = _descriptor.Descriptor(
  name='Mapping',
  full_name='admobilize.signagelive.v1alpha1.Mapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admobilize.signagelive.v1alpha1.Mapping.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credential_id', full_name='admobilize.signagelive.v1alpha1.Mapping.credential_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='admobilize.signagelive.v1alpha1.Mapping.project_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='admobilize.signagelive.v1alpha1.Mapping.device_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='admobilize.signagelive.v1alpha1.Mapping.serial_number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_id', full_name='admobilize.signagelive.v1alpha1.Mapping.network_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_table', full_name='admobilize.signagelive.v1alpha1.Mapping.source_table', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='admobilize.signagelive.v1alpha1.Mapping.created_at', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='admobilize.signagelive.v1alpha1.Mapping.updated_at', index=8,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_start=438,
  serialized_end=682,
)

_CREDENTIAL.fields_by_name['mappings'].message_type = _MAPPING
_CREDENTIAL.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREDENTIAL.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MAPPING.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MAPPING.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Credential'] = _CREDENTIAL
DESCRIPTOR.message_types_by_name['Mapping'] = _MAPPING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Credential = _reflection.GeneratedProtocolMessageType('Credential', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIAL,
  '__module__' : 'admobilize.signagelive.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.signagelive.v1alpha1.Credential)
  })
_sym_db.RegisterMessage(Credential)

Mapping = _reflection.GeneratedProtocolMessageType('Mapping', (_message.Message,), {
  'DESCRIPTOR' : _MAPPING,
  '__module__' : 'admobilize.signagelive.v1alpha1.resources_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.signagelive.v1alpha1.Mapping)
  })
_sym_db.RegisterMessage(Mapping)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
