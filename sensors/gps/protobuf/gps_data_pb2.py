# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='sensors/gps/protobuf/gps_data.proto',
  package='',
  serialized_pb='\n#sensors/gps/protobuf/gps_data.proto\"P\n\x07SatInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06in_use\x18\x02 \x02(\x08\x12\x0b\n\x03\x65lv\x18\x03 \x02(\x05\x12\x0f\n\x07\x61zimuth\x18\x04 \x02(\x05\x12\x0b\n\x03sig\x18\x05 \x02(\x05\"\xaf\x01\n\x07GpsData\x12\x0b\n\x03\x66ix\x18\x01 \x02(\r\x12\x0c\n\x04time\x18\x02 \x02(\t\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x0b\n\x03lon\x18\x04 \x01(\x01\x12\x0b\n\x03\x61lt\x18\x05 \x01(\x01\x12\x0c\n\x04hdop\x18\x06 \x01(\x02\x12\x0c\n\x04vdop\x18\x07 \x01(\x02\x12\r\n\x05speed\x18\x08 \x01(\x02\x12\x0e\n\x06\x63ourse\x18\t \x01(\x02\x12\x0c\n\x04sats\x18\n \x01(\r\x12\x19\n\x07satinfo\x18\x0b \x03(\x0b\x32\x08.SatInfo')




_SATINFO = descriptor.Descriptor(
  name='SatInfo',
  full_name='SatInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='SatInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='in_use', full_name='SatInfo.in_use', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='elv', full_name='SatInfo.elv', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='azimuth', full_name='SatInfo.azimuth', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sig', full_name='SatInfo.sig', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=39,
  serialized_end=119,
)


_GPSDATA = descriptor.Descriptor(
  name='GpsData',
  full_name='GpsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='fix', full_name='GpsData.fix', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='GpsData.time', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lat', full_name='GpsData.lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lon', full_name='GpsData.lon', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alt', full_name='GpsData.alt', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hdop', full_name='GpsData.hdop', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vdop', full_name='GpsData.vdop', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='speed', full_name='GpsData.speed', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='course', full_name='GpsData.course', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sats', full_name='GpsData.sats', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='satinfo', full_name='GpsData.satinfo', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=122,
  serialized_end=297,
)

_GPSDATA.fields_by_name['satinfo'].message_type = _SATINFO
DESCRIPTOR.message_types_by_name['SatInfo'] = _SATINFO
DESCRIPTOR.message_types_by_name['GpsData'] = _GPSDATA

class SatInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SATINFO
  
  # @@protoc_insertion_point(class_scope:SatInfo)

class GpsData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GPSDATA
  
  # @@protoc_insertion_point(class_scope:GpsData)

# @@protoc_insertion_point(module_scope)
