# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import provider_pb2 as provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='resource.proto',
  package='pulumirpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eresource.proto\x12\tpulumirpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0eprovider.proto\"$\n\x16SupportsFeatureRequest\x12\n\n\x02id\x18\x01 \x01(\t\"-\n\x17SupportsFeatureResponse\x12\x12\n\nhasSupport\x18\x01 \x01(\x08\"\xfc\x01\n\x13ReadResourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12+\n\nproperties\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x14\n\x0c\x64\x65pendencies\x18\x06 \x03(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x0f\n\x07version\x18\x08 \x01(\t\x12\x15\n\racceptSecrets\x18\t \x01(\x08\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\n \x03(\t\x12\x0f\n\x07\x61liases\x18\x0b \x03(\t\"P\n\x14ReadResourceResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x80\x06\n\x17RegisterResourceRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06parent\x18\x03 \x01(\t\x12\x0e\n\x06\x63ustom\x18\x04 \x01(\x08\x12\'\n\x06object\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07protect\x18\x06 \x01(\x08\x12\x14\n\x0c\x64\x65pendencies\x18\x07 \x03(\t\x12\x10\n\x08provider\x18\x08 \x01(\t\x12Z\n\x14propertyDependencies\x18\t \x03(\x0b\x32<.pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\n \x01(\x08\x12\x0f\n\x07version\x18\x0b \x01(\t\x12\x15\n\rignoreChanges\x18\x0c \x03(\t\x12\x15\n\racceptSecrets\x18\r \x01(\x08\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\x0e \x03(\t\x12\x0f\n\x07\x61liases\x18\x0f \x03(\t\x12\x10\n\x08importId\x18\x10 \x01(\t\x12I\n\x0e\x63ustomTimeouts\x18\x11 \x01(\x0b\x32\x31.pulumirpc.RegisterResourceRequest.CustomTimeouts\x12\"\n\x1a\x64\x65leteBeforeReplaceDefined\x18\x12 \x01(\x08\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a@\n\x0e\x43ustomTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06update\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\t\x1at\n\x19PropertyDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.pulumirpc.RegisterResourceRequest.PropertyDependencies:\x02\x38\x01\"}\n\x18RegisterResourceResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\'\n\x06object\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06stable\x18\x04 \x01(\x08\x12\x0f\n\x07stables\x18\x05 \x03(\t\"W\n\x1eRegisterResourceOutputsRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12(\n\x07outputs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct2\xc0\x03\n\x0fResourceMonitor\x12Z\n\x0fSupportsFeature\x12!.pulumirpc.SupportsFeatureRequest\x1a\".pulumirpc.SupportsFeatureResponse\"\x00\x12?\n\x06Invoke\x12\x18.pulumirpc.InvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x12Q\n\x0cReadResource\x12\x1e.pulumirpc.ReadResourceRequest\x1a\x1f.pulumirpc.ReadResourceResponse\"\x00\x12]\n\x10RegisterResource\x12\".pulumirpc.RegisterResourceRequest\x1a#.pulumirpc.RegisterResourceResponse\"\x00\x12^\n\x17RegisterResourceOutputs\x12).pulumirpc.RegisterResourceOutputsRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,provider__pb2.DESCRIPTOR,])




_SUPPORTSFEATUREREQUEST = _descriptor.Descriptor(
  name='SupportsFeatureRequest',
  full_name='pulumirpc.SupportsFeatureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.SupportsFeatureRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=104,
  serialized_end=140,
)


_SUPPORTSFEATURERESPONSE = _descriptor.Descriptor(
  name='SupportsFeatureResponse',
  full_name='pulumirpc.SupportsFeatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hasSupport', full_name='pulumirpc.SupportsFeatureResponse.hasSupport', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=142,
  serialized_end=187,
)


_READRESOURCEREQUEST = _descriptor.Descriptor(
  name='ReadResourceRequest',
  full_name='pulumirpc.ReadResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.ReadResourceRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.ReadResourceRequest.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.ReadResourceRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='pulumirpc.ReadResourceRequest.parent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.ReadResourceRequest.properties', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='pulumirpc.ReadResourceRequest.dependencies', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='pulumirpc.ReadResourceRequest.provider', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pulumirpc.ReadResourceRequest.version', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceptSecrets', full_name='pulumirpc.ReadResourceRequest.acceptSecrets', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additionalSecretOutputs', full_name='pulumirpc.ReadResourceRequest.additionalSecretOutputs', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliases', full_name='pulumirpc.ReadResourceRequest.aliases', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=190,
  serialized_end=442,
)


_READRESOURCERESPONSE = _descriptor.Descriptor(
  name='ReadResourceResponse',
  full_name='pulumirpc.ReadResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.ReadResourceResponse.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.ReadResourceResponse.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=444,
  serialized_end=524,
)


_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES = _descriptor.Descriptor(
  name='PropertyDependencies',
  full_name='pulumirpc.RegisterResourceRequest.PropertyDependencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urns', full_name='pulumirpc.RegisterResourceRequest.PropertyDependencies.urns', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1075,
  serialized_end=1111,
)

_REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS = _descriptor.Descriptor(
  name='CustomTimeouts',
  full_name='pulumirpc.RegisterResourceRequest.CustomTimeouts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='pulumirpc.RegisterResourceRequest.CustomTimeouts.create', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='pulumirpc.RegisterResourceRequest.CustomTimeouts.update', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete', full_name='pulumirpc.RegisterResourceRequest.CustomTimeouts.delete', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1113,
  serialized_end=1177,
)

_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY = _descriptor.Descriptor(
  name='PropertyDependenciesEntry',
  full_name='pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1295,
)

_REGISTERRESOURCEREQUEST = _descriptor.Descriptor(
  name='RegisterResourceRequest',
  full_name='pulumirpc.RegisterResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.RegisterResourceRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.RegisterResourceRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='pulumirpc.RegisterResourceRequest.parent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom', full_name='pulumirpc.RegisterResourceRequest.custom', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='pulumirpc.RegisterResourceRequest.object', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protect', full_name='pulumirpc.RegisterResourceRequest.protect', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='pulumirpc.RegisterResourceRequest.dependencies', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='pulumirpc.RegisterResourceRequest.provider', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='propertyDependencies', full_name='pulumirpc.RegisterResourceRequest.propertyDependencies', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteBeforeReplace', full_name='pulumirpc.RegisterResourceRequest.deleteBeforeReplace', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pulumirpc.RegisterResourceRequest.version', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreChanges', full_name='pulumirpc.RegisterResourceRequest.ignoreChanges', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceptSecrets', full_name='pulumirpc.RegisterResourceRequest.acceptSecrets', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additionalSecretOutputs', full_name='pulumirpc.RegisterResourceRequest.additionalSecretOutputs', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliases', full_name='pulumirpc.RegisterResourceRequest.aliases', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='importId', full_name='pulumirpc.RegisterResourceRequest.importId', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customTimeouts', full_name='pulumirpc.RegisterResourceRequest.customTimeouts', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteBeforeReplaceDefined', full_name='pulumirpc.RegisterResourceRequest.deleteBeforeReplaceDefined', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES, _REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS, _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=1295,
)


_REGISTERRESOURCERESPONSE = _descriptor.Descriptor(
  name='RegisterResourceResponse',
  full_name='pulumirpc.RegisterResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.RegisterResourceResponse.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='pulumirpc.RegisterResourceResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='pulumirpc.RegisterResourceResponse.object', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stable', full_name='pulumirpc.RegisterResourceResponse.stable', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stables', full_name='pulumirpc.RegisterResourceResponse.stables', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1297,
  serialized_end=1422,
)


_REGISTERRESOURCEOUTPUTSREQUEST = _descriptor.Descriptor(
  name='RegisterResourceOutputsRequest',
  full_name='pulumirpc.RegisterResourceOutputsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.RegisterResourceOutputsRequest.urn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='pulumirpc.RegisterResourceOutputsRequest.outputs', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1424,
  serialized_end=1511,
)

_READRESOURCEREQUEST.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_READRESOURCERESPONSE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES.containing_type = _REGISTERRESOURCEREQUEST
_REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS.containing_type = _REGISTERRESOURCEREQUEST
_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY.fields_by_name['value'].message_type = _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES
_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY.containing_type = _REGISTERRESOURCEREQUEST
_REGISTERRESOURCEREQUEST.fields_by_name['object'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REGISTERRESOURCEREQUEST.fields_by_name['propertyDependencies'].message_type = _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY
_REGISTERRESOURCEREQUEST.fields_by_name['customTimeouts'].message_type = _REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS
_REGISTERRESOURCERESPONSE.fields_by_name['object'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REGISTERRESOURCEOUTPUTSREQUEST.fields_by_name['outputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['SupportsFeatureRequest'] = _SUPPORTSFEATUREREQUEST
DESCRIPTOR.message_types_by_name['SupportsFeatureResponse'] = _SUPPORTSFEATURERESPONSE
DESCRIPTOR.message_types_by_name['ReadResourceRequest'] = _READRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['ReadResourceResponse'] = _READRESOURCERESPONSE
DESCRIPTOR.message_types_by_name['RegisterResourceRequest'] = _REGISTERRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['RegisterResourceResponse'] = _REGISTERRESOURCERESPONSE
DESCRIPTOR.message_types_by_name['RegisterResourceOutputsRequest'] = _REGISTERRESOURCEOUTPUTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SupportsFeatureRequest = _reflection.GeneratedProtocolMessageType('SupportsFeatureRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTSFEATUREREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.SupportsFeatureRequest)
  })
_sym_db.RegisterMessage(SupportsFeatureRequest)

SupportsFeatureResponse = _reflection.GeneratedProtocolMessageType('SupportsFeatureResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTSFEATURERESPONSE,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.SupportsFeatureResponse)
  })
_sym_db.RegisterMessage(SupportsFeatureResponse)

ReadResourceRequest = _reflection.GeneratedProtocolMessageType('ReadResourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _READRESOURCEREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadResourceRequest)
  })
_sym_db.RegisterMessage(ReadResourceRequest)

ReadResourceResponse = _reflection.GeneratedProtocolMessageType('ReadResourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESOURCERESPONSE,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.ReadResourceResponse)
  })
_sym_db.RegisterMessage(ReadResourceResponse)

RegisterResourceRequest = _reflection.GeneratedProtocolMessageType('RegisterResourceRequest', (_message.Message,), {

  'PropertyDependencies' : _reflection.GeneratedProtocolMessageType('PropertyDependencies', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIES,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.PropertyDependencies)
    })
  ,

  'CustomTimeouts' : _reflection.GeneratedProtocolMessageType('CustomTimeouts', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_CUSTOMTIMEOUTS,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.CustomTimeouts)
    })
  ,

  'PropertyDependenciesEntry' : _reflection.GeneratedProtocolMessageType('PropertyDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY,
    '__module__' : 'resource_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest.PropertyDependenciesEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTERRESOURCEREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceRequest)
  })
_sym_db.RegisterMessage(RegisterResourceRequest)
_sym_db.RegisterMessage(RegisterResourceRequest.PropertyDependencies)
_sym_db.RegisterMessage(RegisterResourceRequest.CustomTimeouts)
_sym_db.RegisterMessage(RegisterResourceRequest.PropertyDependenciesEntry)

RegisterResourceResponse = _reflection.GeneratedProtocolMessageType('RegisterResourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESOURCERESPONSE,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceResponse)
  })
_sym_db.RegisterMessage(RegisterResourceResponse)

RegisterResourceOutputsRequest = _reflection.GeneratedProtocolMessageType('RegisterResourceOutputsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESOURCEOUTPUTSREQUEST,
  '__module__' : 'resource_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.RegisterResourceOutputsRequest)
  })
_sym_db.RegisterMessage(RegisterResourceOutputsRequest)


_REGISTERRESOURCEREQUEST_PROPERTYDEPENDENCIESENTRY._options = None

_RESOURCEMONITOR = _descriptor.ServiceDescriptor(
  name='ResourceMonitor',
  full_name='pulumirpc.ResourceMonitor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1514,
  serialized_end=1962,
  methods=[
  _descriptor.MethodDescriptor(
    name='SupportsFeature',
    full_name='pulumirpc.ResourceMonitor.SupportsFeature',
    index=0,
    containing_service=None,
    input_type=_SUPPORTSFEATUREREQUEST,
    output_type=_SUPPORTSFEATURERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Invoke',
    full_name='pulumirpc.ResourceMonitor.Invoke',
    index=1,
    containing_service=None,
    input_type=provider__pb2._INVOKEREQUEST,
    output_type=provider__pb2._INVOKERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadResource',
    full_name='pulumirpc.ResourceMonitor.ReadResource',
    index=2,
    containing_service=None,
    input_type=_READRESOURCEREQUEST,
    output_type=_READRESOURCERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterResource',
    full_name='pulumirpc.ResourceMonitor.RegisterResource',
    index=3,
    containing_service=None,
    input_type=_REGISTERRESOURCEREQUEST,
    output_type=_REGISTERRESOURCERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterResourceOutputs',
    full_name='pulumirpc.ResourceMonitor.RegisterResourceOutputs',
    index=4,
    containing_service=None,
    input_type=_REGISTERRESOURCEOUTPUTSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCEMONITOR)

DESCRIPTOR.services_by_name['ResourceMonitor'] = _RESOURCEMONITOR

# @@protoc_insertion_point(module_scope)
