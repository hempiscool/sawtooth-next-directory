# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: email_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='email_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x65mail_state.proto\"(\n\x0e\x45mailContainer\x12\x16\n\x06\x65mails\x18\x02 \x03(\x0b\x32\x06.Email\"\'\n\x05\x45mail\x12\x0f\n\x07next_id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\tb\x06proto3')
)




_EMAILCONTAINER = _descriptor.Descriptor(
  name='EmailContainer',
  full_name='EmailContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='emails', full_name='EmailContainer.emails', index=0,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=21,
  serialized_end=61,
)


_EMAIL = _descriptor.Descriptor(
  name='Email',
  full_name='Email',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_id', full_name='Email.next_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='Email.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=102,
)

_EMAILCONTAINER.fields_by_name['emails'].message_type = _EMAIL
DESCRIPTOR.message_types_by_name['EmailContainer'] = _EMAILCONTAINER
DESCRIPTOR.message_types_by_name['Email'] = _EMAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmailContainer = _reflection.GeneratedProtocolMessageType('EmailContainer', (_message.Message,), dict(
  DESCRIPTOR = _EMAILCONTAINER,
  __module__ = 'email_state_pb2'
  # @@protoc_insertion_point(class_scope:EmailContainer)
  ))
_sym_db.RegisterMessage(EmailContainer)

Email = _reflection.GeneratedProtocolMessageType('Email', (_message.Message,), dict(
  DESCRIPTOR = _EMAIL,
  __module__ = 'email_state_pb2'
  # @@protoc_insertion_point(class_scope:Email)
  ))
_sym_db.RegisterMessage(Email)


# @@protoc_insertion_point(module_scope)
