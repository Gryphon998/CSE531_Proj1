# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbank.proto\x12\x05proj1\"B\n\x12MsgDeliveryRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x03\"D\n\x10MsgDeliveryReply\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x03\x32Q\n\nBankSystem\x12\x43\n\x0bMsgDelivery\x12\x19.proj1.MsgDeliveryRequest\x1a\x17.proj1.MsgDeliveryReply\"\x00\x62\x06proto3')



_MSGDELIVERYREQUEST = DESCRIPTOR.message_types_by_name['MsgDeliveryRequest']
_MSGDELIVERYREPLY = DESCRIPTOR.message_types_by_name['MsgDeliveryReply']
MsgDeliveryRequest = _reflection.GeneratedProtocolMessageType('MsgDeliveryRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGDELIVERYREQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proj1.MsgDeliveryRequest)
  })
_sym_db.RegisterMessage(MsgDeliveryRequest)

MsgDeliveryReply = _reflection.GeneratedProtocolMessageType('MsgDeliveryReply', (_message.Message,), {
  'DESCRIPTOR' : _MSGDELIVERYREPLY,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:proj1.MsgDeliveryReply)
  })
_sym_db.RegisterMessage(MsgDeliveryReply)

_BANKSYSTEM = DESCRIPTOR.services_by_name['BankSystem']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MSGDELIVERYREQUEST._serialized_start=21
  _MSGDELIVERYREQUEST._serialized_end=87
  _MSGDELIVERYREPLY._serialized_start=89
  _MSGDELIVERYREPLY._serialized_end=157
  _BANKSYSTEM._serialized_start=159
  _BANKSYSTEM._serialized_end=240
# @@protoc_insertion_point(module_scope)
