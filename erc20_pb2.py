# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: erc20.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65rc20.proto\x12\x10messari.erc20.v1\"A\n\x0b\x45RC20Tokens\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32\x1c.messari.erc20.v1.ERC20TokenR\x05items\"n\n\nERC20Token\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x16\n\x06symbol\x18\x03 \x01(\tR\x06symbol\x12\x1a\n\x08\x64\x65\x63imals\x18\x04 \x01(\x04R\x08\x64\x65\x63imals\"G\n\x0eTransferEvents\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32\x1f.messari.erc20.v1.TransferEventR\x05items\"\xc7\x01\n\rTransferEvent\x12\x17\n\x07tx_hash\x18\x01 \x01(\tR\x06txHash\x12\x1b\n\tlog_index\x18\x02 \x01(\rR\x08logIndex\x12\x1f\n\x0blog_ordinal\x18\x03 \x01(\x04R\nlogOrdinal\x12#\n\rtoken_address\x18\x04 \x01(\tR\x0ctokenAddress\x12\x12\n\x04\x66rom\x18\x05 \x01(\tR\x04\x66rom\x12\x0e\n\x02to\x18\x06 \x01(\tR\x02to\x12\x16\n\x06\x61mount\x18\x07 \x01(\tR\x06\x61mount\"M\n\x0cTokenBalance\x12#\n\rtoken_address\x18\x01 \x01(\tR\x0ctokenAddress\x12\x18\n\x07\x62\x61lance\x18\x02 \x01(\tR\x07\x62\x61lance\"_\n\x07\x41\x63\x63ount\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12:\n\x08\x62\x61lances\x18\x02 \x03(\x0b\x32\x1e.messari.erc20.v1.TokenBalanceR\x08\x62\x61lancesb\x06proto3')



_ERC20TOKENS = DESCRIPTOR.message_types_by_name['ERC20Tokens']
_ERC20TOKEN = DESCRIPTOR.message_types_by_name['ERC20Token']
_TRANSFEREVENTS = DESCRIPTOR.message_types_by_name['TransferEvents']
_TRANSFEREVENT = DESCRIPTOR.message_types_by_name['TransferEvent']
_TOKENBALANCE = DESCRIPTOR.message_types_by_name['TokenBalance']
_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
ERC20Tokens = _reflection.GeneratedProtocolMessageType('ERC20Tokens', (_message.Message,), {
  'DESCRIPTOR' : _ERC20TOKENS,
  '__module__' : 'erc20_pb2'
  # @@protoc_insertion_point(class_scope:messari.erc20.v1.ERC20Tokens)
  })
_sym_db.RegisterMessage(ERC20Tokens)

ERC20Token = _reflection.GeneratedProtocolMessageType('ERC20Token', (_message.Message,), {
  'DESCRIPTOR' : _ERC20TOKEN,
  '__module__' : 'erc20_pb2'
  # @@protoc_insertion_point(class_scope:messari.erc20.v1.ERC20Token)
  })
_sym_db.RegisterMessage(ERC20Token)

TransferEvents = _reflection.GeneratedProtocolMessageType('TransferEvents', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFEREVENTS,
  '__module__' : 'erc20_pb2'
  # @@protoc_insertion_point(class_scope:messari.erc20.v1.TransferEvents)
  })
_sym_db.RegisterMessage(TransferEvents)

TransferEvent = _reflection.GeneratedProtocolMessageType('TransferEvent', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFEREVENT,
  '__module__' : 'erc20_pb2'
  # @@protoc_insertion_point(class_scope:messari.erc20.v1.TransferEvent)
  })
_sym_db.RegisterMessage(TransferEvent)

TokenBalance = _reflection.GeneratedProtocolMessageType('TokenBalance', (_message.Message,), {
  'DESCRIPTOR' : _TOKENBALANCE,
  '__module__' : 'erc20_pb2'
  # @@protoc_insertion_point(class_scope:messari.erc20.v1.TokenBalance)
  })
_sym_db.RegisterMessage(TokenBalance)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'erc20_pb2'
  # @@protoc_insertion_point(class_scope:messari.erc20.v1.Account)
  })
_sym_db.RegisterMessage(Account)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ERC20TOKENS._serialized_start=33
  _ERC20TOKENS._serialized_end=98
  _ERC20TOKEN._serialized_start=100
  _ERC20TOKEN._serialized_end=210
  _TRANSFEREVENTS._serialized_start=212
  _TRANSFEREVENTS._serialized_end=283
  _TRANSFEREVENT._serialized_start=286
  _TRANSFEREVENT._serialized_end=485
  _TOKENBALANCE._serialized_start=487
  _TOKENBALANCE._serialized_end=564
  _ACCOUNT._serialized_start=566
  _ACCOUNT._serialized_end=661
# @@protoc_insertion_point(module_scope)