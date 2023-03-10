# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sf/substreams/v1/substreams.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sf.substreams.v1 import modules_pb2 as sf_dot_substreams_dot_v1_dot_modules__pb2
from sf.substreams.v1 import clock_pb2 as sf_dot_substreams_dot_v1_dot_clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sf/substreams/v1/substreams.proto\x12\x10sf.substreams.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1esf/substreams/v1/modules.proto\x1a\x1csf/substreams/v1/clock.proto\"\x9a\x03\n\x07Request\x12&\n\x0fstart_block_num\x18\x01 \x01(\x03R\rstartBlockNum\x12!\n\x0cstart_cursor\x18\x02 \x01(\tR\x0bstartCursor\x12$\n\x0estop_block_num\x18\x03 \x01(\x04R\x0cstopBlockNum\x12\x39\n\nfork_steps\x18\x04 \x03(\x0e\x32\x1a.sf.substreams.v1.ForkStepR\tforkSteps\x12;\n\x19irreversibility_condition\x18\x05 \x01(\tR\x18irreversibilityCondition\x12\x33\n\x07modules\x18\x06 \x01(\x0b\x32\x19.sf.substreams.v1.ModulesR\x07modules\x12%\n\x0eoutput_modules\x18\x07 \x03(\tR\routputModules\x12J\n\"initial_store_snapshot_for_modules\x18\x08 \x03(\tR\x1einitialStoreSnapshotForModules\"\xf2\x02\n\x08Response\x12\x39\n\x07session\x18\x05 \x01(\x0b\x32\x1d.sf.substreams.v1.SessionInitH\x00R\x07session\x12?\n\x08progress\x18\x01 \x01(\x0b\x32!.sf.substreams.v1.ModulesProgressH\x00R\x08progress\x12L\n\rsnapshot_data\x18\x02 \x01(\x0b\x32%.sf.substreams.v1.InitialSnapshotDataH\x00R\x0csnapshotData\x12X\n\x11snapshot_complete\x18\x03 \x01(\x0b\x32).sf.substreams.v1.InitialSnapshotCompleteH\x00R\x10snapshotComplete\x12\x37\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.sf.substreams.v1.BlockScopedDataH\x00R\x04\x64\x61taB\t\n\x07message\"(\n\x0bSessionInit\x12\x19\n\x08trace_id\x18\x01 \x01(\tR\x07traceId\"1\n\x17InitialSnapshotComplete\x12\x16\n\x06\x63ursor\x18\x01 \x01(\tR\x06\x63ursor\"\xa9\x01\n\x13InitialSnapshotData\x12\x1f\n\x0bmodule_name\x18\x01 \x01(\tR\nmoduleName\x12\x35\n\x06\x64\x65ltas\x18\x02 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltasR\x06\x64\x65ltas\x12\x1b\n\tsent_keys\x18\x04 \x01(\x04R\x08sentKeys\x12\x1d\n\ntotal_keys\x18\x03 \x01(\x04R\ttotalKeys\"\xc2\x01\n\x0f\x42lockScopedData\x12\x38\n\x07outputs\x18\x01 \x03(\x0b\x32\x1e.sf.substreams.v1.ModuleOutputR\x07outputs\x12-\n\x05\x63lock\x18\x03 \x01(\x0b\x32\x17.sf.substreams.v1.ClockR\x05\x63lock\x12.\n\x04step\x18\x06 \x01(\x0e\x32\x1a.sf.substreams.v1.ForkStepR\x04step\x12\x16\n\x06\x63ursor\x18\n \x01(\tR\x06\x63ursor\"\xe0\x01\n\x0cModuleOutput\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x35\n\nmap_output\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\tmapOutput\x12\x42\n\x0cstore_deltas\x18\x03 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltasH\x00R\x0bstoreDeltas\x12\x12\n\x04logs\x18\x04 \x03(\tR\x04logs\x12%\n\x0elogs_truncated\x18\x05 \x01(\x08R\rlogsTruncatedB\x06\n\x04\x64\x61ta\"M\n\x0fModulesProgress\x12:\n\x07modules\x18\x01 \x03(\x0b\x32 .sf.substreams.v1.ModuleProgressR\x07modules\"\xe6\x05\n\x0eModuleProgress\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\\\n\x10processed_ranges\x18\x02 \x01(\x0b\x32/.sf.substreams.v1.ModuleProgress.ProcessedRangeH\x00R\x0fprocessedRanges\x12T\n\rinitial_state\x18\x03 \x01(\x0b\x32-.sf.substreams.v1.ModuleProgress.InitialStateH\x00R\x0cinitialState\x12Z\n\x0fprocessed_bytes\x18\x04 \x01(\x0b\x32/.sf.substreams.v1.ModuleProgress.ProcessedBytesH\x00R\x0eprocessedBytes\x12\x41\n\x06\x66\x61iled\x18\x05 \x01(\x0b\x32\'.sf.substreams.v1.ModuleProgress.FailedH\x00R\x06\x66\x61iled\x1aY\n\x0eProcessedRange\x12G\n\x10processed_ranges\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.BlockRangeR\x0fprocessedRanges\x1a\x41\n\x0cInitialState\x12\x31\n\x15\x61vailable_up_to_block\x18\x02 \x01(\x04R\x12\x61vailableUpToBlock\x1aj\n\x0eProcessedBytes\x12(\n\x10total_bytes_read\x18\x01 \x01(\x04R\x0etotalBytesRead\x12.\n\x13total_bytes_written\x18\x02 \x01(\x04R\x11totalBytesWritten\x1a[\n\x06\x46\x61iled\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reason\x12\x12\n\x04logs\x18\x02 \x03(\tR\x04logs\x12%\n\x0elogs_truncated\x18\x03 \x01(\x08R\rlogsTruncatedB\x06\n\x04type\"J\n\nBlockRange\x12\x1f\n\x0bstart_block\x18\x02 \x01(\x04R\nstartBlock\x12\x1b\n\tend_block\x18\x03 \x01(\x04R\x08\x65ndBlock\"C\n\x0bStoreDeltas\x12\x34\n\x06\x64\x65ltas\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.StoreDeltaR\x06\x64\x65ltas\"\xf4\x01\n\nStoreDelta\x12\x44\n\toperation\x18\x01 \x01(\x0e\x32&.sf.substreams.v1.StoreDelta.OperationR\toperation\x12\x18\n\x07ordinal\x18\x02 \x01(\x04R\x07ordinal\x12\x10\n\x03key\x18\x03 \x01(\tR\x03key\x12\x1b\n\told_value\x18\x04 \x01(\x0cR\x08oldValue\x12\x1b\n\tnew_value\x18\x05 \x01(\x0cR\x08newValue\":\n\tOperation\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\xa6\x01\n\x06Output\x12\x1b\n\tblock_num\x18\x01 \x01(\x04R\x08\x62lockNum\x12\x19\n\x08\x62lock_id\x18\x02 \x01(\tR\x07\x62lockId\x12\x38\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12*\n\x05value\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value*\\\n\x08\x46orkStep\x12\x10\n\x0cSTEP_UNKNOWN\x10\x00\x12\x0c\n\x08STEP_NEW\x10\x01\x12\r\n\tSTEP_UNDO\x10\x02\x12\x15\n\x11STEP_IRREVERSIBLE\x10\x04\"\x04\x08\x03\x10\x03\"\x04\x08\x05\x10\x05\x32K\n\x06Stream\x12\x41\n\x06\x42locks\x12\x19.sf.substreams.v1.Request\x1a\x1a.sf.substreams.v1.Response0\x01\x42\x46ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreamsb\x06proto3')

_FORKSTEP = DESCRIPTOR.enum_types_by_name['ForkStep']
ForkStep = enum_type_wrapper.EnumTypeWrapper(_FORKSTEP)
STEP_UNKNOWN = 0
STEP_NEW = 1
STEP_UNDO = 2
STEP_IRREVERSIBLE = 4


_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_SESSIONINIT = DESCRIPTOR.message_types_by_name['SessionInit']
_INITIALSNAPSHOTCOMPLETE = DESCRIPTOR.message_types_by_name['InitialSnapshotComplete']
_INITIALSNAPSHOTDATA = DESCRIPTOR.message_types_by_name['InitialSnapshotData']
_BLOCKSCOPEDDATA = DESCRIPTOR.message_types_by_name['BlockScopedData']
_MODULEOUTPUT = DESCRIPTOR.message_types_by_name['ModuleOutput']
_MODULESPROGRESS = DESCRIPTOR.message_types_by_name['ModulesProgress']
_MODULEPROGRESS = DESCRIPTOR.message_types_by_name['ModuleProgress']
_MODULEPROGRESS_PROCESSEDRANGE = _MODULEPROGRESS.nested_types_by_name['ProcessedRange']
_MODULEPROGRESS_INITIALSTATE = _MODULEPROGRESS.nested_types_by_name['InitialState']
_MODULEPROGRESS_PROCESSEDBYTES = _MODULEPROGRESS.nested_types_by_name['ProcessedBytes']
_MODULEPROGRESS_FAILED = _MODULEPROGRESS.nested_types_by_name['Failed']
_BLOCKRANGE = DESCRIPTOR.message_types_by_name['BlockRange']
_STOREDELTAS = DESCRIPTOR.message_types_by_name['StoreDeltas']
_STOREDELTA = DESCRIPTOR.message_types_by_name['StoreDelta']
_OUTPUT = DESCRIPTOR.message_types_by_name['Output']
_STOREDELTA_OPERATION = _STOREDELTA.enum_types_by_name['Operation']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.Response)
  })
_sym_db.RegisterMessage(Response)

SessionInit = _reflection.GeneratedProtocolMessageType('SessionInit', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONINIT,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.SessionInit)
  })
_sym_db.RegisterMessage(SessionInit)

InitialSnapshotComplete = _reflection.GeneratedProtocolMessageType('InitialSnapshotComplete', (_message.Message,), {
  'DESCRIPTOR' : _INITIALSNAPSHOTCOMPLETE,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.InitialSnapshotComplete)
  })
_sym_db.RegisterMessage(InitialSnapshotComplete)

InitialSnapshotData = _reflection.GeneratedProtocolMessageType('InitialSnapshotData', (_message.Message,), {
  'DESCRIPTOR' : _INITIALSNAPSHOTDATA,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.InitialSnapshotData)
  })
_sym_db.RegisterMessage(InitialSnapshotData)

BlockScopedData = _reflection.GeneratedProtocolMessageType('BlockScopedData', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKSCOPEDDATA,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.BlockScopedData)
  })
_sym_db.RegisterMessage(BlockScopedData)

ModuleOutput = _reflection.GeneratedProtocolMessageType('ModuleOutput', (_message.Message,), {
  'DESCRIPTOR' : _MODULEOUTPUT,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleOutput)
  })
_sym_db.RegisterMessage(ModuleOutput)

ModulesProgress = _reflection.GeneratedProtocolMessageType('ModulesProgress', (_message.Message,), {
  'DESCRIPTOR' : _MODULESPROGRESS,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModulesProgress)
  })
_sym_db.RegisterMessage(ModulesProgress)

ModuleProgress = _reflection.GeneratedProtocolMessageType('ModuleProgress', (_message.Message,), {

  'ProcessedRange' : _reflection.GeneratedProtocolMessageType('ProcessedRange', (_message.Message,), {
    'DESCRIPTOR' : _MODULEPROGRESS_PROCESSEDRANGE,
    '__module__' : 'sf.substreams.v1.substreams_pb2'
    # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleProgress.ProcessedRange)
    })
  ,

  'InitialState' : _reflection.GeneratedProtocolMessageType('InitialState', (_message.Message,), {
    'DESCRIPTOR' : _MODULEPROGRESS_INITIALSTATE,
    '__module__' : 'sf.substreams.v1.substreams_pb2'
    # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleProgress.InitialState)
    })
  ,

  'ProcessedBytes' : _reflection.GeneratedProtocolMessageType('ProcessedBytes', (_message.Message,), {
    'DESCRIPTOR' : _MODULEPROGRESS_PROCESSEDBYTES,
    '__module__' : 'sf.substreams.v1.substreams_pb2'
    # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleProgress.ProcessedBytes)
    })
  ,

  'Failed' : _reflection.GeneratedProtocolMessageType('Failed', (_message.Message,), {
    'DESCRIPTOR' : _MODULEPROGRESS_FAILED,
    '__module__' : 'sf.substreams.v1.substreams_pb2'
    # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleProgress.Failed)
    })
  ,
  'DESCRIPTOR' : _MODULEPROGRESS,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleProgress)
  })
_sym_db.RegisterMessage(ModuleProgress)
_sym_db.RegisterMessage(ModuleProgress.ProcessedRange)
_sym_db.RegisterMessage(ModuleProgress.InitialState)
_sym_db.RegisterMessage(ModuleProgress.ProcessedBytes)
_sym_db.RegisterMessage(ModuleProgress.Failed)

BlockRange = _reflection.GeneratedProtocolMessageType('BlockRange', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKRANGE,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.BlockRange)
  })
_sym_db.RegisterMessage(BlockRange)

StoreDeltas = _reflection.GeneratedProtocolMessageType('StoreDeltas', (_message.Message,), {
  'DESCRIPTOR' : _STOREDELTAS,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.StoreDeltas)
  })
_sym_db.RegisterMessage(StoreDeltas)

StoreDelta = _reflection.GeneratedProtocolMessageType('StoreDelta', (_message.Message,), {
  'DESCRIPTOR' : _STOREDELTA,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.StoreDelta)
  })
_sym_db.RegisterMessage(StoreDelta)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.Output)
  })
_sym_db.RegisterMessage(Output)

_STREAM = DESCRIPTOR.services_by_name['Stream']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreams'
  _FORKSTEP._serialized_start=3037
  _FORKSTEP._serialized_end=3129
  _REQUEST._serialized_start=178
  _REQUEST._serialized_end=588
  _RESPONSE._serialized_start=591
  _RESPONSE._serialized_end=961
  _SESSIONINIT._serialized_start=963
  _SESSIONINIT._serialized_end=1003
  _INITIALSNAPSHOTCOMPLETE._serialized_start=1005
  _INITIALSNAPSHOTCOMPLETE._serialized_end=1054
  _INITIALSNAPSHOTDATA._serialized_start=1057
  _INITIALSNAPSHOTDATA._serialized_end=1226
  _BLOCKSCOPEDDATA._serialized_start=1229
  _BLOCKSCOPEDDATA._serialized_end=1423
  _MODULEOUTPUT._serialized_start=1426
  _MODULEOUTPUT._serialized_end=1650
  _MODULESPROGRESS._serialized_start=1652
  _MODULESPROGRESS._serialized_end=1729
  _MODULEPROGRESS._serialized_start=1732
  _MODULEPROGRESS._serialized_end=2474
  _MODULEPROGRESS_PROCESSEDRANGE._serialized_start=2109
  _MODULEPROGRESS_PROCESSEDRANGE._serialized_end=2198
  _MODULEPROGRESS_INITIALSTATE._serialized_start=2200
  _MODULEPROGRESS_INITIALSTATE._serialized_end=2265
  _MODULEPROGRESS_PROCESSEDBYTES._serialized_start=2267
  _MODULEPROGRESS_PROCESSEDBYTES._serialized_end=2373
  _MODULEPROGRESS_FAILED._serialized_start=2375
  _MODULEPROGRESS_FAILED._serialized_end=2466
  _BLOCKRANGE._serialized_start=2476
  _BLOCKRANGE._serialized_end=2550
  _STOREDELTAS._serialized_start=2552
  _STOREDELTAS._serialized_end=2619
  _STOREDELTA._serialized_start=2622
  _STOREDELTA._serialized_end=2866
  _STOREDELTA_OPERATION._serialized_start=2808
  _STOREDELTA_OPERATION._serialized_end=2866
  _OUTPUT._serialized_start=2869
  _OUTPUT._serialized_end=3035
  _STREAM._serialized_start=3131
  _STREAM._serialized_end=3206
# @@protoc_insertion_point(module_scope)
