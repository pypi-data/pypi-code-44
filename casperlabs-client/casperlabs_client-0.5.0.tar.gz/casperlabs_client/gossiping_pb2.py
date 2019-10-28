# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gossiping.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import empty_pb2 as empty__pb2
from . import consensus_pb2 as consensus__pb2
from . import node_pb2 as node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gossiping.proto',
  package='io.casperlabs.comm.gossiping',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fgossiping.proto\x12\x1cio.casperlabs.comm.gossiping\x1a\x0b\x65mpty.proto\x1a\x0f\x63onsensus.proto\x1a\nnode.proto\"\\\n\x10NewBlocksRequest\x12\x32\n\x06sender\x18\x01 \x01(\x0b\x32\".io.casperlabs.comm.discovery.Node\x12\x14\n\x0c\x62lock_hashes\x18\x02 \x03(\x0c\"#\n\x11NewBlocksResponse\x12\x0e\n\x06is_new\x18\x01 \x01(\x08\"3\n\x1bStreamBlockSummariesRequest\x12\x14\n\x0c\x62lock_hashes\x18\x01 \x03(\x0c\"q\n#StreamAncestorBlockSummariesRequest\x12\x1b\n\x13target_block_hashes\x18\x01 \x03(\x0c\x12\x1a\n\x12known_block_hashes\x18\x02 \x03(\x0c\x12\x11\n\tmax_depth\x18\x03 \x01(\r\"#\n!StreamDagTipBlockSummariesRequest\"i\n\x16GetBlockChunkedRequest\x12\x12\n\nblock_hash\x18\x01 \x01(\x0c\x12\x12\n\nchunk_size\x18\x02 \x01(\r\x12\'\n\x1f\x61\x63\x63\x65pted_compression_algorithms\x18\x03 \x03(\t\"\x1c\n\x1aGetGenesisCandidateRequest\"d\n\x12\x41\x64\x64\x41pprovalRequest\x12\x12\n\nblock_hash\x18\x01 \x01(\x0c\x12:\n\x08\x61pproval\x18\x02 \x01(\x0b\x32(.io.casperlabs.casper.consensus.Approval\"\xc2\x01\n\x05\x43hunk\x12<\n\x06header\x18\x01 \x01(\x0b\x32*.io.casperlabs.comm.gossiping.Chunk.HeaderH\x00\x12\x0e\n\x04\x64\x61ta\x18\x02 \x01(\x0cH\x00\x1a`\n\x06Header\x12\x1d\n\x15\x63ompression_algorithm\x18\x01 \x01(\t\x12\x16\n\x0e\x63ontent_length\x18\x02 \x01(\r\x12\x1f\n\x17original_content_length\x18\x03 \x01(\rB\t\n\x07\x63ontent2\xf2\x06\n\rGossipService\x12l\n\tNewBlocks\x12..io.casperlabs.comm.gossiping.NewBlocksRequest\x1a/.io.casperlabs.comm.gossiping.NewBlocksResponse\x12\x91\x01\n\x1cStreamAncestorBlockSummaries\x12\x41.io.casperlabs.comm.gossiping.StreamAncestorBlockSummariesRequest\x1a,.io.casperlabs.casper.consensus.BlockSummary0\x01\x12\x8d\x01\n\x1aStreamDagTipBlockSummaries\x12?.io.casperlabs.comm.gossiping.StreamDagTipBlockSummariesRequest\x1a,.io.casperlabs.casper.consensus.BlockSummary0\x01\x12\x81\x01\n\x14StreamBlockSummaries\x12\x39.io.casperlabs.comm.gossiping.StreamBlockSummariesRequest\x1a,.io.casperlabs.casper.consensus.BlockSummary0\x01\x12n\n\x0fGetBlockChunked\x12\x34.io.casperlabs.comm.gossiping.GetBlockChunkedRequest\x1a#.io.casperlabs.comm.gossiping.Chunk0\x01\x12\x81\x01\n\x13GetGenesisCandidate\x12\x38.io.casperlabs.comm.gossiping.GetGenesisCandidateRequest\x1a\x30.io.casperlabs.casper.consensus.GenesisCandidate\x12W\n\x0b\x41\x64\x64\x41pproval\x12\x30.io.casperlabs.comm.gossiping.AddApprovalRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[empty__pb2.DESCRIPTOR,consensus__pb2.DESCRIPTOR,node__pb2.DESCRIPTOR,])




_NEWBLOCKSREQUEST = _descriptor.Descriptor(
  name='NewBlocksRequest',
  full_name='io.casperlabs.comm.gossiping.NewBlocksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='io.casperlabs.comm.gossiping.NewBlocksRequest.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hashes', full_name='io.casperlabs.comm.gossiping.NewBlocksRequest.block_hashes', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  serialized_start=91,
  serialized_end=183,
)


_NEWBLOCKSRESPONSE = _descriptor.Descriptor(
  name='NewBlocksResponse',
  full_name='io.casperlabs.comm.gossiping.NewBlocksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_new', full_name='io.casperlabs.comm.gossiping.NewBlocksResponse.is_new', index=0,
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
  serialized_start=185,
  serialized_end=220,
)


_STREAMBLOCKSUMMARIESREQUEST = _descriptor.Descriptor(
  name='StreamBlockSummariesRequest',
  full_name='io.casperlabs.comm.gossiping.StreamBlockSummariesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_hashes', full_name='io.casperlabs.comm.gossiping.StreamBlockSummariesRequest.block_hashes', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=222,
  serialized_end=273,
)


_STREAMANCESTORBLOCKSUMMARIESREQUEST = _descriptor.Descriptor(
  name='StreamAncestorBlockSummariesRequest',
  full_name='io.casperlabs.comm.gossiping.StreamAncestorBlockSummariesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_block_hashes', full_name='io.casperlabs.comm.gossiping.StreamAncestorBlockSummariesRequest.target_block_hashes', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='known_block_hashes', full_name='io.casperlabs.comm.gossiping.StreamAncestorBlockSummariesRequest.known_block_hashes', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='io.casperlabs.comm.gossiping.StreamAncestorBlockSummariesRequest.max_depth', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=275,
  serialized_end=388,
)


_STREAMDAGTIPBLOCKSUMMARIESREQUEST = _descriptor.Descriptor(
  name='StreamDagTipBlockSummariesRequest',
  full_name='io.casperlabs.comm.gossiping.StreamDagTipBlockSummariesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=390,
  serialized_end=425,
)


_GETBLOCKCHUNKEDREQUEST = _descriptor.Descriptor(
  name='GetBlockChunkedRequest',
  full_name='io.casperlabs.comm.gossiping.GetBlockChunkedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='io.casperlabs.comm.gossiping.GetBlockChunkedRequest.block_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_size', full_name='io.casperlabs.comm.gossiping.GetBlockChunkedRequest.chunk_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accepted_compression_algorithms', full_name='io.casperlabs.comm.gossiping.GetBlockChunkedRequest.accepted_compression_algorithms', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=427,
  serialized_end=532,
)


_GETGENESISCANDIDATEREQUEST = _descriptor.Descriptor(
  name='GetGenesisCandidateRequest',
  full_name='io.casperlabs.comm.gossiping.GetGenesisCandidateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=534,
  serialized_end=562,
)


_ADDAPPROVALREQUEST = _descriptor.Descriptor(
  name='AddApprovalRequest',
  full_name='io.casperlabs.comm.gossiping.AddApprovalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='io.casperlabs.comm.gossiping.AddApprovalRequest.block_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approval', full_name='io.casperlabs.comm.gossiping.AddApprovalRequest.approval', index=1,
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
  serialized_start=564,
  serialized_end=664,
)


_CHUNK_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='io.casperlabs.comm.gossiping.Chunk.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='compression_algorithm', full_name='io.casperlabs.comm.gossiping.Chunk.Header.compression_algorithm', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_length', full_name='io.casperlabs.comm.gossiping.Chunk.Header.content_length', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_content_length', full_name='io.casperlabs.comm.gossiping.Chunk.Header.original_content_length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=754,
  serialized_end=850,
)

_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='io.casperlabs.comm.gossiping.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='io.casperlabs.comm.gossiping.Chunk.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='io.casperlabs.comm.gossiping.Chunk.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHUNK_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='io.casperlabs.comm.gossiping.Chunk.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=667,
  serialized_end=861,
)

_NEWBLOCKSREQUEST.fields_by_name['sender'].message_type = node__pb2._NODE
_ADDAPPROVALREQUEST.fields_by_name['approval'].message_type = consensus__pb2._APPROVAL
_CHUNK_HEADER.containing_type = _CHUNK
_CHUNK.fields_by_name['header'].message_type = _CHUNK_HEADER
_CHUNK.oneofs_by_name['content'].fields.append(
  _CHUNK.fields_by_name['header'])
_CHUNK.fields_by_name['header'].containing_oneof = _CHUNK.oneofs_by_name['content']
_CHUNK.oneofs_by_name['content'].fields.append(
  _CHUNK.fields_by_name['data'])
_CHUNK.fields_by_name['data'].containing_oneof = _CHUNK.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['NewBlocksRequest'] = _NEWBLOCKSREQUEST
DESCRIPTOR.message_types_by_name['NewBlocksResponse'] = _NEWBLOCKSRESPONSE
DESCRIPTOR.message_types_by_name['StreamBlockSummariesRequest'] = _STREAMBLOCKSUMMARIESREQUEST
DESCRIPTOR.message_types_by_name['StreamAncestorBlockSummariesRequest'] = _STREAMANCESTORBLOCKSUMMARIESREQUEST
DESCRIPTOR.message_types_by_name['StreamDagTipBlockSummariesRequest'] = _STREAMDAGTIPBLOCKSUMMARIESREQUEST
DESCRIPTOR.message_types_by_name['GetBlockChunkedRequest'] = _GETBLOCKCHUNKEDREQUEST
DESCRIPTOR.message_types_by_name['GetGenesisCandidateRequest'] = _GETGENESISCANDIDATEREQUEST
DESCRIPTOR.message_types_by_name['AddApprovalRequest'] = _ADDAPPROVALREQUEST
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewBlocksRequest = _reflection.GeneratedProtocolMessageType('NewBlocksRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWBLOCKSREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.NewBlocksRequest)
  })
_sym_db.RegisterMessage(NewBlocksRequest)

NewBlocksResponse = _reflection.GeneratedProtocolMessageType('NewBlocksResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWBLOCKSRESPONSE,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.NewBlocksResponse)
  })
_sym_db.RegisterMessage(NewBlocksResponse)

StreamBlockSummariesRequest = _reflection.GeneratedProtocolMessageType('StreamBlockSummariesRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMBLOCKSUMMARIESREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.StreamBlockSummariesRequest)
  })
_sym_db.RegisterMessage(StreamBlockSummariesRequest)

StreamAncestorBlockSummariesRequest = _reflection.GeneratedProtocolMessageType('StreamAncestorBlockSummariesRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMANCESTORBLOCKSUMMARIESREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.StreamAncestorBlockSummariesRequest)
  })
_sym_db.RegisterMessage(StreamAncestorBlockSummariesRequest)

StreamDagTipBlockSummariesRequest = _reflection.GeneratedProtocolMessageType('StreamDagTipBlockSummariesRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMDAGTIPBLOCKSUMMARIESREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.StreamDagTipBlockSummariesRequest)
  })
_sym_db.RegisterMessage(StreamDagTipBlockSummariesRequest)

GetBlockChunkedRequest = _reflection.GeneratedProtocolMessageType('GetBlockChunkedRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKCHUNKEDREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.GetBlockChunkedRequest)
  })
_sym_db.RegisterMessage(GetBlockChunkedRequest)

GetGenesisCandidateRequest = _reflection.GeneratedProtocolMessageType('GetGenesisCandidateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGENESISCANDIDATEREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.GetGenesisCandidateRequest)
  })
_sym_db.RegisterMessage(GetGenesisCandidateRequest)

AddApprovalRequest = _reflection.GeneratedProtocolMessageType('AddApprovalRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDAPPROVALREQUEST,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.AddApprovalRequest)
  })
_sym_db.RegisterMessage(AddApprovalRequest)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _CHUNK_HEADER,
    '__module__' : 'gossiping_pb2'
    # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.Chunk.Header)
    })
  ,
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'gossiping_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.comm.gossiping.Chunk)
  })
_sym_db.RegisterMessage(Chunk)
_sym_db.RegisterMessage(Chunk.Header)



_GOSSIPSERVICE = _descriptor.ServiceDescriptor(
  name='GossipService',
  full_name='io.casperlabs.comm.gossiping.GossipService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=864,
  serialized_end=1746,
  methods=[
  _descriptor.MethodDescriptor(
    name='NewBlocks',
    full_name='io.casperlabs.comm.gossiping.GossipService.NewBlocks',
    index=0,
    containing_service=None,
    input_type=_NEWBLOCKSREQUEST,
    output_type=_NEWBLOCKSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamAncestorBlockSummaries',
    full_name='io.casperlabs.comm.gossiping.GossipService.StreamAncestorBlockSummaries',
    index=1,
    containing_service=None,
    input_type=_STREAMANCESTORBLOCKSUMMARIESREQUEST,
    output_type=consensus__pb2._BLOCKSUMMARY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamDagTipBlockSummaries',
    full_name='io.casperlabs.comm.gossiping.GossipService.StreamDagTipBlockSummaries',
    index=2,
    containing_service=None,
    input_type=_STREAMDAGTIPBLOCKSUMMARIESREQUEST,
    output_type=consensus__pb2._BLOCKSUMMARY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamBlockSummaries',
    full_name='io.casperlabs.comm.gossiping.GossipService.StreamBlockSummaries',
    index=3,
    containing_service=None,
    input_type=_STREAMBLOCKSUMMARIESREQUEST,
    output_type=consensus__pb2._BLOCKSUMMARY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockChunked',
    full_name='io.casperlabs.comm.gossiping.GossipService.GetBlockChunked',
    index=4,
    containing_service=None,
    input_type=_GETBLOCKCHUNKEDREQUEST,
    output_type=_CHUNK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetGenesisCandidate',
    full_name='io.casperlabs.comm.gossiping.GossipService.GetGenesisCandidate',
    index=5,
    containing_service=None,
    input_type=_GETGENESISCANDIDATEREQUEST,
    output_type=consensus__pb2._GENESISCANDIDATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddApproval',
    full_name='io.casperlabs.comm.gossiping.GossipService.AddApproval',
    index=6,
    containing_service=None,
    input_type=_ADDAPPROVALREQUEST,
    output_type=empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GOSSIPSERVICE)

DESCRIPTOR.services_by_name['GossipService'] = _GOSSIPSERVICE

# @@protoc_insertion_point(module_scope)
