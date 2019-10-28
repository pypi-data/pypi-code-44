# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='node.proto',
  package='io.casperlabs.comm.discovery',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nnode.proto\x12\x1cio.casperlabs.comm.discovery\"a\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x15\n\rprotocol_port\x18\x03 \x01(\r\x12\x16\n\x0e\x64iscovery_port\x18\x04 \x01(\r\x12\x10\n\x08\x63hain_id\x18\x05 \x01(\x0c\x62\x06proto3')
)




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='io.casperlabs.comm.discovery.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.casperlabs.comm.discovery.Node.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='io.casperlabs.comm.discovery.Node.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_port', full_name='io.casperlabs.comm.discovery.Node.protocol_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_port', full_name='io.casperlabs.comm.discovery.Node.discovery_port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='io.casperlabs.comm.discovery.Node.chain_id', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=44,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['Node'] = _NODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.discovery.Node)
  })
_sym_db.RegisterMessage(Node)


# @@protoc_insertion_point(module_scope)
