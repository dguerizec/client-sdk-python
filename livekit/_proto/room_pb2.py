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
# source: room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import handle_pb2 as handle__pb2
from . import participant_pb2 as participant__pb2
from . import track_pb2 as track__pb2
from . import video_frame_pb2 as video__frame__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nroom.proto\x12\rlivekit.proto\x1a\x0chandle.proto\x1a\x11participant.proto\x1a\x0btrack.proto\x1a\x11video_frame.proto\"Y\n\x0e\x43onnectRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12+\n\x07options\x18\x03 \x01(\x0b\x32\x1a.livekit.proto.RoomOptions\"#\n\x0f\x43onnectResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"\xf9\x02\n\x0f\x43onnectCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12%\n\x04room\x18\x03 \x01(\x0b\x32\x17.livekit.proto.RoomInfo\x12\x39\n\x11local_participant\x18\x04 \x01(\x0b\x32\x1e.livekit.proto.ParticipantInfo\x12J\n\x0cparticipants\x18\x05 \x03(\x0b\x32\x34.livekit.proto.ConnectCallback.ParticipantWithTracks\x1a\x87\x01\n\x15ParticipantWithTracks\x12\x33\n\x0bparticipant\x18\x01 \x01(\x0b\x32\x1e.livekit.proto.ParticipantInfo\x12\x39\n\x0cpublications\x18\x02 \x03(\x0b\x32#.livekit.proto.TrackPublicationInfoB\x08\n\x06_error\"(\n\x11\x44isconnectRequest\x12\x13\n\x0broom_handle\x18\x01 \x01(\x04\"&\n\x12\x44isconnectResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"&\n\x12\x44isconnectCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"\x82\x01\n\x13PublishTrackRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x14\n\x0ctrack_handle\x18\x02 \x01(\x04\x12\x33\n\x07options\x18\x03 \x01(\x0b\x32\".livekit.proto.TrackPublishOptions\"(\n\x14PublishTrackResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"\x80\x01\n\x14PublishTrackCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x38\n\x0bpublication\x18\x03 \x01(\x0b\x32#.livekit.proto.TrackPublicationInfoB\x08\n\x06_error\"g\n\x15UnpublishTrackRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\x19\n\x11stop_on_unpublish\x18\x03 \x01(\x08\"*\n\x16UnpublishTrackResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"H\n\x16UnpublishTrackCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xa1\x01\n\x12PublishDataRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x10\n\x08\x64\x61ta_ptr\x18\x02 \x01(\x04\x12\x10\n\x08\x64\x61ta_len\x18\x03 \x01(\x04\x12+\n\x04kind\x18\x04 \x01(\x0e\x32\x1d.livekit.proto.DataPacketKind\x12\x18\n\x10\x64\x65stination_sids\x18\x05 \x03(\t\"\'\n\x13PublishDataResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"E\n\x13PublishDataCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"E\n\x14SetSubscribedRequest\x12\x11\n\tsubscribe\x18\x01 \x01(\x08\x12\x1a\n\x12publication_handle\x18\x02 \x01(\x04\"\x17\n\x15SetSubscribedResponse\";\n\rVideoEncoding\x12\x13\n\x0bmax_bitrate\x18\x01 \x01(\x04\x12\x15\n\rmax_framerate\x18\x02 \x01(\x01\"$\n\rAudioEncoding\x12\x13\n\x0bmax_bitrate\x18\x01 \x01(\x04\"\x8a\x02\n\x13TrackPublishOptions\x12\x34\n\x0evideo_encoding\x18\x01 \x01(\x0b\x32\x1c.livekit.proto.VideoEncoding\x12\x34\n\x0e\x61udio_encoding\x18\x02 \x01(\x0b\x32\x1c.livekit.proto.AudioEncoding\x12.\n\x0bvideo_codec\x18\x03 \x01(\x0e\x32\x19.livekit.proto.VideoCodec\x12\x0b\n\x03\x64tx\x18\x04 \x01(\x08\x12\x0b\n\x03red\x18\x05 \x01(\x08\x12\x11\n\tsimulcast\x18\x06 \x01(\x08\x12*\n\x06source\x18\x07 \x01(\x0e\x32\x1a.livekit.proto.TrackSource\"P\n\x0bRoomOptions\x12\x16\n\x0e\x61uto_subscribe\x18\x01 \x01(\x08\x12\x17\n\x0f\x61\x64\x61ptive_stream\x18\x02 \x01(\x08\x12\x10\n\x08\x64ynacast\x18\x03 \x01(\x08\"_\n\nBufferInfo\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\x10\n\x08\x64\x61ta_ptr\x18\x02 \x01(\x04\x12\x10\n\x08\x64\x61ta_len\x18\x03 \x01(\x04\"\xd9\t\n\tRoomEvent\x12\x13\n\x0broom_handle\x18\x01 \x01(\x04\x12\x44\n\x15participant_connected\x18\x02 \x01(\x0b\x32#.livekit.proto.ParticipantConnectedH\x00\x12J\n\x18participant_disconnected\x18\x03 \x01(\x0b\x32&.livekit.proto.ParticipantDisconnectedH\x00\x12\x43\n\x15local_track_published\x18\x04 \x01(\x0b\x32\".livekit.proto.LocalTrackPublishedH\x00\x12G\n\x17local_track_unpublished\x18\x05 \x01(\x0b\x32$.livekit.proto.LocalTrackUnpublishedH\x00\x12\x38\n\x0ftrack_published\x18\x06 \x01(\x0b\x32\x1d.livekit.proto.TrackPublishedH\x00\x12<\n\x11track_unpublished\x18\x07 \x01(\x0b\x32\x1f.livekit.proto.TrackUnpublishedH\x00\x12:\n\x10track_subscribed\x18\x08 \x01(\x0b\x32\x1e.livekit.proto.TrackSubscribedH\x00\x12>\n\x12track_unsubscribed\x18\t \x01(\x0b\x32 .livekit.proto.TrackUnsubscribedH\x00\x12K\n\x19track_subscription_failed\x18\n \x01(\x0b\x32&.livekit.proto.TrackSubscriptionFailedH\x00\x12\x30\n\x0btrack_muted\x18\x0b \x01(\x0b\x32\x19.livekit.proto.TrackMutedH\x00\x12\x34\n\rtrack_unmuted\x18\x0c \x01(\x0b\x32\x1b.livekit.proto.TrackUnmutedH\x00\x12G\n\x17\x61\x63tive_speakers_changed\x18\r \x01(\x0b\x32$.livekit.proto.ActiveSpeakersChangedH\x00\x12M\n\x1a\x63onnection_quality_changed\x18\x0e \x01(\x0b\x32\'.livekit.proto.ConnectionQualityChangedH\x00\x12\x34\n\rdata_received\x18\x0f \x01(\x0b\x32\x1b.livekit.proto.DataReceivedH\x00\x12I\n\x18\x63onnection_state_changed\x18\x10 \x01(\x0b\x32%.livekit.proto.ConnectionStateChangedH\x00\x12-\n\tconnected\x18\x11 \x01(\x0b\x32\x18.livekit.proto.ConnectedH\x00\x12\x33\n\x0c\x64isconnected\x18\x12 \x01(\x0b\x32\x1b.livekit.proto.DisconnectedH\x00\x12\x33\n\x0creconnecting\x18\x13 \x01(\x0b\x32\x1b.livekit.proto.ReconnectingH\x00\x12\x31\n\x0breconnected\x18\x14 \x01(\x0b\x32\x1a.livekit.proto.ReconnectedH\x00\x42\t\n\x07message\"f\n\x08RoomInfo\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\x0b\n\x03sid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\t\"D\n\x14ParticipantConnected\x12,\n\x04info\x18\x01 \x01(\x0b\x32\x1e.livekit.proto.ParticipantInfo\"2\n\x17ParticipantDisconnected\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\"(\n\x13LocalTrackPublished\x12\x11\n\ttrack_sid\x18\x01 \x01(\t\"0\n\x15LocalTrackUnpublished\x12\x17\n\x0fpublication_sid\x18\x01 \x01(\t\"c\n\x0eTrackPublished\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x38\n\x0bpublication\x18\x02 \x01(\x0b\x32#.livekit.proto.TrackPublicationInfo\"D\n\x10TrackUnpublished\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x17\n\x0fpublication_sid\x18\x02 \x01(\t\"S\n\x0fTrackSubscribed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\'\n\x05track\x18\x02 \x01(\x0b\x32\x18.livekit.proto.TrackInfo\"?\n\x11TrackUnsubscribed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\"T\n\x17TrackSubscriptionFailed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"8\n\nTrackMuted\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\":\n\x0cTrackUnmuted\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\"1\n\x15\x41\x63tiveSpeakersChanged\x12\x18\n\x10participant_sids\x18\x01 \x03(\t\"f\n\x18\x43onnectionQualityChanged\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x31\n\x07quality\x18\x02 \x01(\x0e\x32 .livekit.proto.ConnectionQuality\"\x96\x01\n\x0c\x44\x61taReceived\x12\'\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x19.livekit.proto.BufferInfo\x12\x1c\n\x0fparticipant_sid\x18\x02 \x01(\tH\x00\x88\x01\x01\x12+\n\x04kind\x18\x03 \x01(\x0e\x32\x1d.livekit.proto.DataPacketKindB\x12\n\x10_participant_sid\"G\n\x16\x43onnectionStateChanged\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.ConnectionState\"\x0b\n\tConnected\"\x0e\n\x0c\x44isconnected\"\x0e\n\x0cReconnecting\"\r\n\x0bReconnected*N\n\x11\x43onnectionQuality\x12\x10\n\x0cQUALITY_POOR\x10\x00\x12\x10\n\x0cQUALITY_GOOD\x10\x01\x12\x15\n\x11QUALITY_EXCELLENT\x10\x02*S\n\x0f\x43onnectionState\x12\x15\n\x11\x43ONN_DISCONNECTED\x10\x00\x12\x12\n\x0e\x43ONN_CONNECTED\x10\x01\x12\x15\n\x11\x43ONN_RECONNECTING\x10\x02*3\n\x0e\x44\x61taPacketKind\x12\x0e\n\nKIND_LOSSY\x10\x00\x12\x11\n\rKIND_RELIABLE\x10\x01\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'room_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_CONNECTIONQUALITY']._serialized_start=4700
  _globals['_CONNECTIONQUALITY']._serialized_end=4778
  _globals['_CONNECTIONSTATE']._serialized_start=4780
  _globals['_CONNECTIONSTATE']._serialized_end=4863
  _globals['_DATAPACKETKIND']._serialized_start=4865
  _globals['_DATAPACKETKIND']._serialized_end=4916
  _globals['_CONNECTREQUEST']._serialized_start=94
  _globals['_CONNECTREQUEST']._serialized_end=183
  _globals['_CONNECTRESPONSE']._serialized_start=185
  _globals['_CONNECTRESPONSE']._serialized_end=220
  _globals['_CONNECTCALLBACK']._serialized_start=223
  _globals['_CONNECTCALLBACK']._serialized_end=600
  _globals['_CONNECTCALLBACK_PARTICIPANTWITHTRACKS']._serialized_start=455
  _globals['_CONNECTCALLBACK_PARTICIPANTWITHTRACKS']._serialized_end=590
  _globals['_DISCONNECTREQUEST']._serialized_start=602
  _globals['_DISCONNECTREQUEST']._serialized_end=642
  _globals['_DISCONNECTRESPONSE']._serialized_start=644
  _globals['_DISCONNECTRESPONSE']._serialized_end=682
  _globals['_DISCONNECTCALLBACK']._serialized_start=684
  _globals['_DISCONNECTCALLBACK']._serialized_end=722
  _globals['_PUBLISHTRACKREQUEST']._serialized_start=725
  _globals['_PUBLISHTRACKREQUEST']._serialized_end=855
  _globals['_PUBLISHTRACKRESPONSE']._serialized_start=857
  _globals['_PUBLISHTRACKRESPONSE']._serialized_end=897
  _globals['_PUBLISHTRACKCALLBACK']._serialized_start=900
  _globals['_PUBLISHTRACKCALLBACK']._serialized_end=1028
  _globals['_UNPUBLISHTRACKREQUEST']._serialized_start=1030
  _globals['_UNPUBLISHTRACKREQUEST']._serialized_end=1133
  _globals['_UNPUBLISHTRACKRESPONSE']._serialized_start=1135
  _globals['_UNPUBLISHTRACKRESPONSE']._serialized_end=1177
  _globals['_UNPUBLISHTRACKCALLBACK']._serialized_start=1179
  _globals['_UNPUBLISHTRACKCALLBACK']._serialized_end=1251
  _globals['_PUBLISHDATAREQUEST']._serialized_start=1254
  _globals['_PUBLISHDATAREQUEST']._serialized_end=1415
  _globals['_PUBLISHDATARESPONSE']._serialized_start=1417
  _globals['_PUBLISHDATARESPONSE']._serialized_end=1456
  _globals['_PUBLISHDATACALLBACK']._serialized_start=1458
  _globals['_PUBLISHDATACALLBACK']._serialized_end=1527
  _globals['_SETSUBSCRIBEDREQUEST']._serialized_start=1529
  _globals['_SETSUBSCRIBEDREQUEST']._serialized_end=1598
  _globals['_SETSUBSCRIBEDRESPONSE']._serialized_start=1600
  _globals['_SETSUBSCRIBEDRESPONSE']._serialized_end=1623
  _globals['_VIDEOENCODING']._serialized_start=1625
  _globals['_VIDEOENCODING']._serialized_end=1684
  _globals['_AUDIOENCODING']._serialized_start=1686
  _globals['_AUDIOENCODING']._serialized_end=1722
  _globals['_TRACKPUBLISHOPTIONS']._serialized_start=1725
  _globals['_TRACKPUBLISHOPTIONS']._serialized_end=1991
  _globals['_ROOMOPTIONS']._serialized_start=1993
  _globals['_ROOMOPTIONS']._serialized_end=2073
  _globals['_BUFFERINFO']._serialized_start=2075
  _globals['_BUFFERINFO']._serialized_end=2170
  _globals['_ROOMEVENT']._serialized_start=2173
  _globals['_ROOMEVENT']._serialized_end=3414
  _globals['_ROOMINFO']._serialized_start=3416
  _globals['_ROOMINFO']._serialized_end=3518
  _globals['_PARTICIPANTCONNECTED']._serialized_start=3520
  _globals['_PARTICIPANTCONNECTED']._serialized_end=3588
  _globals['_PARTICIPANTDISCONNECTED']._serialized_start=3590
  _globals['_PARTICIPANTDISCONNECTED']._serialized_end=3640
  _globals['_LOCALTRACKPUBLISHED']._serialized_start=3642
  _globals['_LOCALTRACKPUBLISHED']._serialized_end=3682
  _globals['_LOCALTRACKUNPUBLISHED']._serialized_start=3684
  _globals['_LOCALTRACKUNPUBLISHED']._serialized_end=3732
  _globals['_TRACKPUBLISHED']._serialized_start=3734
  _globals['_TRACKPUBLISHED']._serialized_end=3833
  _globals['_TRACKUNPUBLISHED']._serialized_start=3835
  _globals['_TRACKUNPUBLISHED']._serialized_end=3903
  _globals['_TRACKSUBSCRIBED']._serialized_start=3905
  _globals['_TRACKSUBSCRIBED']._serialized_end=3988
  _globals['_TRACKUNSUBSCRIBED']._serialized_start=3990
  _globals['_TRACKUNSUBSCRIBED']._serialized_end=4053
  _globals['_TRACKSUBSCRIPTIONFAILED']._serialized_start=4055
  _globals['_TRACKSUBSCRIPTIONFAILED']._serialized_end=4139
  _globals['_TRACKMUTED']._serialized_start=4141
  _globals['_TRACKMUTED']._serialized_end=4197
  _globals['_TRACKUNMUTED']._serialized_start=4199
  _globals['_TRACKUNMUTED']._serialized_end=4257
  _globals['_ACTIVESPEAKERSCHANGED']._serialized_start=4259
  _globals['_ACTIVESPEAKERSCHANGED']._serialized_end=4308
  _globals['_CONNECTIONQUALITYCHANGED']._serialized_start=4310
  _globals['_CONNECTIONQUALITYCHANGED']._serialized_end=4412
  _globals['_DATARECEIVED']._serialized_start=4415
  _globals['_DATARECEIVED']._serialized_end=4565
  _globals['_CONNECTIONSTATECHANGED']._serialized_start=4567
  _globals['_CONNECTIONSTATECHANGED']._serialized_end=4638
  _globals['_CONNECTED']._serialized_start=4640
  _globals['_CONNECTED']._serialized_end=4651
  _globals['_DISCONNECTED']._serialized_start=4653
  _globals['_DISCONNECTED']._serialized_end=4667
  _globals['_RECONNECTING']._serialized_start=4669
  _globals['_RECONNECTING']._serialized_end=4683
  _globals['_RECONNECTED']._serialized_start=4685
  _globals['_RECONNECTED']._serialized_end=4698
# @@protoc_insertion_point(module_scope)
