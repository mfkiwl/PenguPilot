# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='powerman/protobuf/power.proto',
  package='',
  serialized_pb='\n\x1dpowerman/protobuf/power.proto\"&\n\x08PowerReq\x12\x1a\n\x03\x63md\x18\x01 \x02(\x0e\x32\r.PowerCommand\"(\n\x08PowerRep\x12\x1c\n\x06status\x18\x01 \x02(\x0e\x32\x0c.PowerStatus\"\x89\x01\n\nPowerState\x12\x0f\n\x07voltage\x18\x01 \x02(\x02\x12\x0f\n\x07\x63urrent\x18\x02 \x02(\x02\x12\x10\n\x08\x63\x61pacity\x18\x03 \x02(\x02\x12\x10\n\x08\x63onsumed\x18\x04 \x02(\x02\x12\x11\n\tremaining\x18\x05 \x02(\x02\x12\x10\n\x08\x63ritical\x18\x06 \x02(\x08\x12\x10\n\x08\x65stimate\x18\x07 \x01(\x02*1\n\x0cPowerCommand\x12\x0f\n\x0bSTAND_POWER\x10\x00\x12\x10\n\x0c\x46LIGHT_POWER\x10\x01*0\n\x0bPowerStatus\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08\x45_SYNTAX\x10\x01\x12\x0b\n\x07\x45_POWER\x10\x02')

_POWERCOMMAND = descriptor.EnumDescriptor(
  name='PowerCommand',
  full_name='PowerCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STAND_POWER', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FLIGHT_POWER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=255,
  serialized_end=304,
)


_POWERSTATUS = descriptor.EnumDescriptor(
  name='PowerStatus',
  full_name='PowerStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='E_SYNTAX', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='E_POWER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=306,
  serialized_end=354,
)


STAND_POWER = 0
FLIGHT_POWER = 1
OK = 0
E_SYNTAX = 1
E_POWER = 2



_POWERREQ = descriptor.Descriptor(
  name='PowerReq',
  full_name='PowerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cmd', full_name='PowerReq.cmd', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=33,
  serialized_end=71,
)


_POWERREP = descriptor.Descriptor(
  name='PowerRep',
  full_name='PowerRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='PowerRep.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=73,
  serialized_end=113,
)


_POWERSTATE = descriptor.Descriptor(
  name='PowerState',
  full_name='PowerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='voltage', full_name='PowerState.voltage', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='current', full_name='PowerState.current', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='capacity', full_name='PowerState.capacity', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='consumed', full_name='PowerState.consumed', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='remaining', full_name='PowerState.remaining', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='critical', full_name='PowerState.critical', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='estimate', full_name='PowerState.estimate', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=116,
  serialized_end=253,
)

_POWERREQ.fields_by_name['cmd'].enum_type = _POWERCOMMAND
_POWERREP.fields_by_name['status'].enum_type = _POWERSTATUS
DESCRIPTOR.message_types_by_name['PowerReq'] = _POWERREQ
DESCRIPTOR.message_types_by_name['PowerRep'] = _POWERREP
DESCRIPTOR.message_types_by_name['PowerState'] = _POWERSTATE

class PowerReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POWERREQ
  
  # @@protoc_insertion_point(class_scope:PowerReq)

class PowerRep(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POWERREP
  
  # @@protoc_insertion_point(class_scope:PowerRep)

class PowerState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POWERSTATE
  
  # @@protoc_insertion_point(class_scope:PowerState)

# @@protoc_insertion_point(module_scope)
