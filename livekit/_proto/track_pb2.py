# Copyright 2023 LiveKit, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: track.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import handle_pb2 as handle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btrack.proto\x12\rlivekit.proto\x1a\x0chandle.proto\">\n\x17\x43reateVideoTrackRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsource_handle\x18\x02 \x01(\x04\"C\n\x18\x43reateVideoTrackResponse\x12\'\n\x05track\x18\x01 \x01(\x0b\x32\x18.livekit.proto.TrackInfo\">\n\x17\x43reateAudioTrackRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsource_handle\x18\x02 \x01(\x04\"C\n\x18\x43reateAudioTrackResponse\x12\'\n\x05track\x18\x01 \x01(\x0b\x32\x18.livekit.proto.TrackInfo\"\x0c\n\nTrackEvent\"\x9a\x02\n\x14TrackPublicationInfo\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\x0b\n\x03sid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12&\n\x04kind\x18\x04 \x01(\x0e\x32\x18.livekit.proto.TrackKind\x12*\n\x06source\x18\x05 \x01(\x0e\x32\x1a.livekit.proto.TrackSource\x12\x13\n\x0bsimulcasted\x18\x06 \x01(\x08\x12\r\n\x05width\x18\x07 \x01(\r\x12\x0e\n\x06height\x18\x08 \x01(\r\x12\x11\n\tmime_type\x18\t \x01(\t\x12\r\n\x05muted\x18\n \x01(\x08\x12\x0e\n\x06remote\x18\x0b \x01(\x08\"\xce\x01\n\tTrackInfo\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\x0b\n\x03sid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12&\n\x04kind\x18\x04 \x01(\x0e\x32\x18.livekit.proto.TrackKind\x12\x30\n\x0cstream_state\x18\x05 \x01(\x0e\x32\x1a.livekit.proto.StreamState\x12\r\n\x05muted\x18\x06 \x01(\x08\x12\x0e\n\x06remote\x18\x07 \x01(\x08*=\n\tTrackKind\x12\x10\n\x0cKIND_UNKNOWN\x10\x00\x12\x0e\n\nKIND_AUDIO\x10\x01\x12\x0e\n\nKIND_VIDEO\x10\x02*\x81\x01\n\x0bTrackSource\x12\x12\n\x0eSOURCE_UNKNOWN\x10\x00\x12\x11\n\rSOURCE_CAMERA\x10\x01\x12\x15\n\x11SOURCE_MICROPHONE\x10\x02\x12\x16\n\x12SOURCE_SCREENSHARE\x10\x03\x12\x1c\n\x18SOURCE_SCREENSHARE_AUDIO\x10\x04*D\n\x0bStreamState\x12\x11\n\rSTATE_UNKNOWN\x10\x00\x12\x10\n\x0cSTATE_ACTIVE\x10\x01\x12\x10\n\x0cSTATE_PAUSED\x10\x02\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'track_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_TRACKKIND']._serialized_start=818
  _globals['_TRACKKIND']._serialized_end=879
  _globals['_TRACKSOURCE']._serialized_start=882
  _globals['_TRACKSOURCE']._serialized_end=1011
  _globals['_STREAMSTATE']._serialized_start=1013
  _globals['_STREAMSTATE']._serialized_end=1081
  _globals['_CREATEVIDEOTRACKREQUEST']._serialized_start=44
  _globals['_CREATEVIDEOTRACKREQUEST']._serialized_end=106
  _globals['_CREATEVIDEOTRACKRESPONSE']._serialized_start=108
  _globals['_CREATEVIDEOTRACKRESPONSE']._serialized_end=175
  _globals['_CREATEAUDIOTRACKREQUEST']._serialized_start=177
  _globals['_CREATEAUDIOTRACKREQUEST']._serialized_end=239
  _globals['_CREATEAUDIOTRACKRESPONSE']._serialized_start=241
  _globals['_CREATEAUDIOTRACKRESPONSE']._serialized_end=308
  _globals['_TRACKEVENT']._serialized_start=310
  _globals['_TRACKEVENT']._serialized_end=322
  _globals['_TRACKPUBLICATIONINFO']._serialized_start=325
  _globals['_TRACKPUBLICATIONINFO']._serialized_end=607
  _globals['_TRACKINFO']._serialized_start=610
  _globals['_TRACKINFO']._serialized_end=816
# @@protoc_insertion_point(module_scope)
