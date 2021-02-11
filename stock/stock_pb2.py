# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock.proto',
  package='stock',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bstock.proto\x12\x05stock\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x10\n\x0e\x41\x63\x63ountRequest\"\x0e\n\x0c\x41\x63\x63ountReply\"\r\n\x0bTickRequest\"T\n\tTickReply\x12\r\n\x05price\x18\x01 \x01(\x01\x12(\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06volume\x18\x03 \x01(\x01\"\x0e\n\x0c\x43hartRequest\",\n\nChartReply\x12\x1e\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x10.stock.ChartData\"\x0f\n\rAccountsReply\"\x0c\n\nBuyRequest\"\n\n\x08\x42uyReply\"\r\n\x0bSellRequest\"\x0b\n\tSellReply\"}\n\tChartData\x12\x0c\n\x04open\x18\x01 \x01(\x01\x12\x0c\n\x04high\x18\x02 \x01(\x01\x12\x0b\n\x03low\x18\x03 \x01(\x01\x12\r\n\x05\x63lose\x18\x04 \x01(\x01\x12\x0e\n\x06volume\x18\x05 \x01(\x01\x12(\n\x04\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xbe\x02\n\x05Stock\x12\x37\n\x07\x41\x63\x63ount\x12\x15.stock.AccountRequest\x1a\x13.stock.AccountReply\"\x00\x12\x30\n\x04Tick\x12\x12.stock.TickRequest\x1a\x10.stock.TickReply\"\x00\x30\x01\x12\x31\n\x05\x43hart\x12\x13.stock.ChartRequest\x1a\x11.stock.ChartReply\"\x00\x12:\n\x08\x41\x63\x63ounts\x12\x16.google.protobuf.Empty\x1a\x14.stock.AccountsReply\"\x00\x12+\n\x03\x42uy\x12\x11.stock.BuyRequest\x1a\x0f.stock.BuyReply\"\x00\x12.\n\x04Sell\x12\x12.stock.SellRequest\x1a\x10.stock.SellReply\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ACCOUNTREQUEST = _descriptor.Descriptor(
  name='AccountRequest',
  full_name='stock.AccountRequest',
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
  serialized_start=84,
  serialized_end=100,
)


_ACCOUNTREPLY = _descriptor.Descriptor(
  name='AccountReply',
  full_name='stock.AccountReply',
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
  serialized_start=102,
  serialized_end=116,
)


_TICKREQUEST = _descriptor.Descriptor(
  name='TickRequest',
  full_name='stock.TickRequest',
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
  serialized_start=118,
  serialized_end=131,
)


_TICKREPLY = _descriptor.Descriptor(
  name='TickReply',
  full_name='stock.TickReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='stock.TickReply.price', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='stock.TickReply.date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='stock.TickReply.volume', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=133,
  serialized_end=217,
)


_CHARTREQUEST = _descriptor.Descriptor(
  name='ChartRequest',
  full_name='stock.ChartRequest',
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
  serialized_start=219,
  serialized_end=233,
)


_CHARTREPLY = _descriptor.Descriptor(
  name='ChartReply',
  full_name='stock.ChartReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='stock.ChartReply.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=235,
  serialized_end=279,
)


_ACCOUNTSREPLY = _descriptor.Descriptor(
  name='AccountsReply',
  full_name='stock.AccountsReply',
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
  serialized_start=281,
  serialized_end=296,
)


_BUYREQUEST = _descriptor.Descriptor(
  name='BuyRequest',
  full_name='stock.BuyRequest',
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
  serialized_start=298,
  serialized_end=310,
)


_BUYREPLY = _descriptor.Descriptor(
  name='BuyReply',
  full_name='stock.BuyReply',
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
  serialized_start=312,
  serialized_end=322,
)


_SELLREQUEST = _descriptor.Descriptor(
  name='SellRequest',
  full_name='stock.SellRequest',
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
  serialized_start=324,
  serialized_end=337,
)


_SELLREPLY = _descriptor.Descriptor(
  name='SellReply',
  full_name='stock.SellReply',
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
  serialized_start=339,
  serialized_end=350,
)


_CHARTDATA = _descriptor.Descriptor(
  name='ChartData',
  full_name='stock.ChartData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='open', full_name='stock.ChartData.open', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high', full_name='stock.ChartData.high', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low', full_name='stock.ChartData.low', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close', full_name='stock.ChartData.close', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='stock.ChartData.volume', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='stock.ChartData.date', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=352,
  serialized_end=477,
)

_TICKREPLY.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHARTREPLY.fields_by_name['data'].message_type = _CHARTDATA
_CHARTDATA.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['AccountRequest'] = _ACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['AccountReply'] = _ACCOUNTREPLY
DESCRIPTOR.message_types_by_name['TickRequest'] = _TICKREQUEST
DESCRIPTOR.message_types_by_name['TickReply'] = _TICKREPLY
DESCRIPTOR.message_types_by_name['ChartRequest'] = _CHARTREQUEST
DESCRIPTOR.message_types_by_name['ChartReply'] = _CHARTREPLY
DESCRIPTOR.message_types_by_name['AccountsReply'] = _ACCOUNTSREPLY
DESCRIPTOR.message_types_by_name['BuyRequest'] = _BUYREQUEST
DESCRIPTOR.message_types_by_name['BuyReply'] = _BUYREPLY
DESCRIPTOR.message_types_by_name['SellRequest'] = _SELLREQUEST
DESCRIPTOR.message_types_by_name['SellReply'] = _SELLREPLY
DESCRIPTOR.message_types_by_name['ChartData'] = _CHARTDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountRequest = _reflection.GeneratedProtocolMessageType('AccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.AccountRequest)
  })
_sym_db.RegisterMessage(AccountRequest)

AccountReply = _reflection.GeneratedProtocolMessageType('AccountReply', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTREPLY,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.AccountReply)
  })
_sym_db.RegisterMessage(AccountReply)

TickRequest = _reflection.GeneratedProtocolMessageType('TickRequest', (_message.Message,), {
  'DESCRIPTOR' : _TICKREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.TickRequest)
  })
_sym_db.RegisterMessage(TickRequest)

TickReply = _reflection.GeneratedProtocolMessageType('TickReply', (_message.Message,), {
  'DESCRIPTOR' : _TICKREPLY,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.TickReply)
  })
_sym_db.RegisterMessage(TickReply)

ChartRequest = _reflection.GeneratedProtocolMessageType('ChartRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHARTREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.ChartRequest)
  })
_sym_db.RegisterMessage(ChartRequest)

ChartReply = _reflection.GeneratedProtocolMessageType('ChartReply', (_message.Message,), {
  'DESCRIPTOR' : _CHARTREPLY,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.ChartReply)
  })
_sym_db.RegisterMessage(ChartReply)

AccountsReply = _reflection.GeneratedProtocolMessageType('AccountsReply', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTSREPLY,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.AccountsReply)
  })
_sym_db.RegisterMessage(AccountsReply)

BuyRequest = _reflection.GeneratedProtocolMessageType('BuyRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUYREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.BuyRequest)
  })
_sym_db.RegisterMessage(BuyRequest)

BuyReply = _reflection.GeneratedProtocolMessageType('BuyReply', (_message.Message,), {
  'DESCRIPTOR' : _BUYREPLY,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.BuyReply)
  })
_sym_db.RegisterMessage(BuyReply)

SellRequest = _reflection.GeneratedProtocolMessageType('SellRequest', (_message.Message,), {
  'DESCRIPTOR' : _SELLREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.SellRequest)
  })
_sym_db.RegisterMessage(SellRequest)

SellReply = _reflection.GeneratedProtocolMessageType('SellReply', (_message.Message,), {
  'DESCRIPTOR' : _SELLREPLY,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.SellReply)
  })
_sym_db.RegisterMessage(SellReply)

ChartData = _reflection.GeneratedProtocolMessageType('ChartData', (_message.Message,), {
  'DESCRIPTOR' : _CHARTDATA,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.ChartData)
  })
_sym_db.RegisterMessage(ChartData)



_STOCK = _descriptor.ServiceDescriptor(
  name='Stock',
  full_name='stock.Stock',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=480,
  serialized_end=798,
  methods=[
  _descriptor.MethodDescriptor(
    name='Account',
    full_name='stock.Stock.Account',
    index=0,
    containing_service=None,
    input_type=_ACCOUNTREQUEST,
    output_type=_ACCOUNTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Tick',
    full_name='stock.Stock.Tick',
    index=1,
    containing_service=None,
    input_type=_TICKREQUEST,
    output_type=_TICKREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Chart',
    full_name='stock.Stock.Chart',
    index=2,
    containing_service=None,
    input_type=_CHARTREQUEST,
    output_type=_CHARTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Accounts',
    full_name='stock.Stock.Accounts',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ACCOUNTSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Buy',
    full_name='stock.Stock.Buy',
    index=4,
    containing_service=None,
    input_type=_BUYREQUEST,
    output_type=_BUYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Sell',
    full_name='stock.Stock.Sell',
    index=5,
    containing_service=None,
    input_type=_SELLREQUEST,
    output_type=_SELLREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOCK)

DESCRIPTOR.services_by_name['Stock'] = _STOCK

# @@protoc_insertion_point(module_scope)