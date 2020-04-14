#!/usr/bin/env python
import webbrowser
import twitch
import time
import os
import sys

client_id=sys.argv[1]
DROPSENABLED_TAGID = "c2542d6d-cd10-4532-919b-3d19f30a768b"

def main():
    while True:
        stream_to_watch = ""
        stream_to_watch_id = -1

        helix = twitch.Helix(client_id=client_id)
        for stream in helix.streams(game_id=516575):
            if DROPSENABLED_TAGID in stream.data['tag_ids']:
                # subprocess.check_call(['google-chrome', 'https://twitch.tv/' + stream.data['user_name']])
                webbrowser.get('google-chrome').open('https://twitch.tv/' + stream.data['user_name'])
                    
                stream_to_watch = stream.data['user_name']
                stream_to_watch_id = stream.data['user_id']
                print("gonna watch " + stream_to_watch)
                os.system("google-chrome " + "https://twitch.tv/" + stream.data['user_name'])
                time.sleep(4)
                break
        print("watching " + stream_to_watch)


        if stream_to_watch != "":
            live = True
            while live:
                print(stream_to_watch + " still live")
                # Heartbeat every five minutes to check that its live
                b = helix.streams(user_id=stream_to_watch_id)
                live = b._data[0].type == "live"
                time.sleep(10)
            os.system("pkill chrome")


main()
