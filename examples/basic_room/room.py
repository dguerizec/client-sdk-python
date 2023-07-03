import sys
import livekit
import logging
import asyncio
from signal import SIGINT, SIGTERM

from livekit import ArgbFrame
from livekit._proto.video_frame_pb2 import FORMAT_BGRA, FORMAT_ABGR, FORMAT_ARGB, FORMAT_RGBA

URL = 'ws://localhost:7880'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MDY2MTMyODgsImlzcyI6IkFQSVRzRWZpZFpqclFvWSIsIm5hbWUiOiJuYXRpdmUiLCJuYmYiOjE2NzI2MTMyODgsInN1YiI6Im5hdGl2ZSIsInZpZGVvIjp7InJvb20iOiJ0ZXN0Iiwicm9vbUFkbWluIjp0cnVlLCJyb29tQ3JlYXRlIjp0cnVlLCJyb29tSm9pbiI6dHJ1ZSwicm9vbUxpc3QiOnRydWV9fQ.uSNIangMRu8jZD5mnRYoCHjcsQWCrJXgHCs0aNIgBFY'

import cv2
import numpy as np

import time

async def main():
    room = livekit.Room()

    audio_stream = None
    video_stream = None

    logging.info("connecting to %s", URL)
    try:
        await room.connect(URL, TOKEN)
        logging.info("connected to room %s", room.name)
    except livekit.ConnectError as e:
        logging.error("failed to connect to the room: %s", e)
        return False

    @room.on("participant_connected")
    def on_participant_connected(participant: livekit.RemoteParticipant):
        logging.info(
            "participant connected: %s %s", participant.sid, participant.identity)

    @room.on("participant_disconnected")
    def on_participant_disconnected(participant: livekit.RemoteParticipant):
        logging.info("participant disconnected: %s %s",
                     participant.sid, participant.identity)

    @room.on("track_published")
    def on_track_published(publication: livekit.LocalTrackPublication, participant: livekit.RemoteParticipant):
        logging.info("track published: %s from participant %s (%s)",
                     publication.sid, participant.sid, participant.identity)

    @room.on("track_unpublished")
    def on_track_unpublished(publication: livekit.LocalTrackPublication, participant: livekit.RemoteParticipant):
        logging.info("track unpublished: %s", publication.sid)

    @room.on("participant_disconnected")
    def on_participant_disconnected(participant: livekit.Participant):
        print(f"DEBUG: on_participant_disconnected {participant}")

    @room.on("participant_connected")
    def on_participant_connected(participant: livekit.Participant):
        print(f"DEBUG: on_participant_connected {participant}")

    @room.on("track_unsubscribed")
    def on_track_unsubscribed(track: livekit.Track, publication: livekit.RemoteTrackPublication, participant: livekit.RemoteParticipant):
        print(f"DEBUG: on_track_unsubscribed {track} {publication} {participant}")

    @room.on("track_unpublished")
    def on_track_unpublished(publication: livekit.LocalTrackPublication, participant: livekit.LocalParticipant):
        print(f"DEBUG: on_track_unpublished {publication} {participant}")

    @room.on("track_published")
    def on_track_published(publication: livekit.LocalTrackPublication, participant: livekit.LocalParticipant):
        print(f"DEBUG: on_track_published {publication} {participant}")

    @room.on("track_subscribed")
    def on_track_subscribed(track: livekit.Track, publication: livekit.RemoteTrackPublication, participant: livekit.RemoteParticipant):
        logging.info("track subscribed: %s", publication.sid)
        print(f"DEBUG: on_track_unsubscribed {track} {publication} {participant}")
        start_time = 0 # time.time()
        print(f"DEBUG: on_track_subscribed received track subscription {track.kind}")
        if track.kind == livekit.TrackKind.KIND_VIDEO:
            nonlocal video_stream
            video_stream = livekit.VideoStream(track)

            print(f"DEBUG: on_track_subscribed setting track event on {track.sid} {track.name}")
            frame_num = 0

            @video_stream.on("frame_received")
            def on_video_frame(frame: livekit.VideoFrame):
                nonlocal frame_num
                nonlocal start_time
                # only write a frame every 2 seconds
                if time.time() - start_time < 10:
                    return
                start_time = time.time()
                print(f"DEBUG: on_video_frame received video frame on {track.sid} {frame.buffer}")

                size = frame.buffer.width * frame.buffer.height
                yuv = frame.buffer.to_i420()

                argb_frame = ArgbFrame(format=FORMAT_ARGB, width=frame.buffer.width, height=frame.buffer.height)
                frame.buffer.to_argb(argb_frame)

                image = np.array(argb_frame.data, dtype=np.uint8).reshape((argb_frame.height, argb_frame.width, 4))
                # write image to file
                #cv2.imwrite(f"{track.sid}-{frame_num:04d}.jpg", image)
                cv2.imwrite(f"{track.sid}.png", image)
                frame_num += 1
                # display image
                #cv2.imshow(track.sid, image)
        elif track.kind == livekit.TrackKind.KIND_AUDIO:
            print("Subscribed to an Audio Track")
            nonlocal audio_stream
            audio_stream = livekit.AudioStream(track)

            @audio_stream.on('frame_received')
            def on_audio_frame(frame: livekit.AudioFrame):
                # received an audio frame from the track
                pass


    @room.on("track_unsubscribed")
    def on_track_unsubscribed(track: livekit.Track, publication: livekit.RemoteTrackPublication, participant: livekit.RemoteParticipant):
        logging.info("track unsubscribed: %s", publication.sid)

    try:
        await room.run()
    except asyncio.CancelledError:
        logging.info("closing the room")
        await room.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, handlers=[
                        logging.FileHandler("basic_room.log"), logging.StreamHandler()])

    if '--help' in sys.argv:
        print("Usage: python3 room.py --token <token>")
        print("Usage: python3 room.py --key <key> --secret <secret> --room <room> --identity <identity>")
        sys.exit(0)
    # get token parameters from command line
    if len(sys.argv) > 1:
        import optparse
        parser = optparse.OptionParser()
        parser.add_option('--token', dest='token', help='token', default=None)
        parser.add_option('--key', dest='key', help='key')
        parser.add_option('--secret', dest='secret', help='secret')
        parser.add_option('--room', dest='room', help='room')
        parser.add_option('--identity', dest='identity', help='identity')
        (options, args) = parser.parse_args()
        if options.token:
            TOKEN = options.token
        else:
            TOKEN = livekit.create_access_token(options.key, options.secret, options.room, options.identity)
    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())
    for signal in [SIGINT, SIGTERM]:
        loop.add_signal_handler(signal, main_task.cancel)
    try:
        loop.run_until_complete(main_task)
    finally:
        loop.close()

