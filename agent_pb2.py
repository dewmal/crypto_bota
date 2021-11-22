# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent.proto',
  package='api.agent',
  syntax='proto3',
  serialized_options=b'Z\033github.com/syigen/rakun/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61gent.proto\x12\tapi.agent\x1a\x1fgoogle/protobuf/timestamp.proto\"!\n\x05\x41gent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\"\n\x04\x44\x61ta\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x98\x02\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\t\x12 \n\x06sender\x18\x02 \x01(\x0b\x32\x10.api.agent.Agent\x12 \n\x07\x63ontent\x18\x03 \x03(\x0b\x32\x0f.api.agent.Data\x12\x12\n\nrequest_id\x18\x04 \x01(\t\x12*\n\x04type\x18\x06 \x01(\x0e\x32\x17.api.agent.Message.TypeH\x00\x88\x01\x01\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12-\n\ttimestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"7\n\x04Type\x12\n\n\x06SYSTEM\x10\x00\x12\t\n\x05\x41GENT\x10\x01\x12\x0b\n\x07\x43OMMAND\x10\x02\x12\x0b\n\x07\x44ISPLAY\x10\x03\x42\x07\n\x05_type\"h\n\x07\x43onnect\x12\x1e\n\x04user\x18\x01 \x01(\x0b\x32\x10.api.agent.Agent\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"Y\n\tTimeDelta\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x04meta\x18\x02 \x03(\x0b\x32\x0f.api.agent.Data\"\x07\n\x05\x43lose2\xb7\x01\n\tBroadcast\x12\x38\n\x0c\x43reateStream\x12\x12.api.agent.Connect\x1a\x12.api.agent.Message0\x01\x12\x36\n\x08SyncTime\x12\x12.api.agent.Connect\x1a\x14.api.agent.TimeDelta0\x01\x12\x38\n\x10\x42roadcastMessage\x12\x12.api.agent.Message\x1a\x10.api.agent.CloseB\x1dZ\x1bgithub.com/syigen/rakun/apib\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='api.agent.Message.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMAND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=347,
  serialized_end=402,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)


_AGENT = _descriptor.Descriptor(
  name='Agent',
  full_name='api.agent.Agent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.agent.Agent.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.agent.Agent.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=59,
  serialized_end=92,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='api.agent.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.agent.Data.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.agent.Data.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=94,
  serialized_end=128,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='api.agent.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.agent.Message.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='api.agent.Message.sender', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='api.agent.Message.content', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='api.agent.Message.request_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='api.agent.Message.type', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='api.agent.Message.tags', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='api.agent.Message.timestamp', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_type', full_name='api.agent.Message._type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=131,
  serialized_end=411,
)


_CONNECT = _descriptor.Descriptor(
  name='Connect',
  full_name='api.agent.Connect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='api.agent.Connect.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='api.agent.Connect.active', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='api.agent.Connect.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=413,
  serialized_end=517,
)


_TIMEDELTA = _descriptor.Descriptor(
  name='TimeDelta',
  full_name='api.agent.TimeDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='api.agent.TimeDelta.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='api.agent.TimeDelta.meta', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=519,
  serialized_end=608,
)


_CLOSE = _descriptor.Descriptor(
  name='Close',
  full_name='api.agent.Close',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=610,
  serialized_end=617,
)

_MESSAGE.fields_by_name['sender'].message_type = _AGENT
_MESSAGE.fields_by_name['content'].message_type = _DATA
_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGE_TYPE.containing_type = _MESSAGE
_MESSAGE.oneofs_by_name['_type'].fields.append(
  _MESSAGE.fields_by_name['type'])
_MESSAGE.fields_by_name['type'].containing_oneof = _MESSAGE.oneofs_by_name['_type']
_CONNECT.fields_by_name['user'].message_type = _AGENT
_CONNECT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEDELTA.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEDELTA.fields_by_name['meta'].message_type = _DATA
DESCRIPTOR.message_types_by_name['Agent'] = _AGENT
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Connect'] = _CONNECT
DESCRIPTOR.message_types_by_name['TimeDelta'] = _TIMEDELTA
DESCRIPTOR.message_types_by_name['Close'] = _CLOSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), {
  'DESCRIPTOR' : _AGENT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.agent.Agent)
  })
_sym_db.RegisterMessage(Agent)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.agent.Data)
  })
_sym_db.RegisterMessage(Data)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.agent.Message)
  })
_sym_db.RegisterMessage(Message)

Connect = _reflection.GeneratedProtocolMessageType('Connect', (_message.Message,), {
  'DESCRIPTOR' : _CONNECT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.agent.Connect)
  })
_sym_db.RegisterMessage(Connect)

TimeDelta = _reflection.GeneratedProtocolMessageType('TimeDelta', (_message.Message,), {
  'DESCRIPTOR' : _TIMEDELTA,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.agent.TimeDelta)
  })
_sym_db.RegisterMessage(TimeDelta)

Close = _reflection.GeneratedProtocolMessageType('Close', (_message.Message,), {
  'DESCRIPTOR' : _CLOSE,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.agent.Close)
  })
_sym_db.RegisterMessage(Close)


DESCRIPTOR._options = None

_BROADCAST = _descriptor.ServiceDescriptor(
  name='Broadcast',
  full_name='api.agent.Broadcast',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=620,
  serialized_end=803,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateStream',
    full_name='api.agent.Broadcast.CreateStream',
    index=0,
    containing_service=None,
    input_type=_CONNECT,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SyncTime',
    full_name='api.agent.Broadcast.SyncTime',
    index=1,
    containing_service=None,
    input_type=_CONNECT,
    output_type=_TIMEDELTA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BroadcastMessage',
    full_name='api.agent.Broadcast.BroadcastMessage',
    index=2,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_CLOSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROADCAST)

DESCRIPTOR.services_by_name['Broadcast'] = _BROADCAST

# @@protoc_insertion_point(module_scope)
