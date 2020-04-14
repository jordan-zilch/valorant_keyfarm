#!/usr/bin/env python
import webbrowser
import twitch
import time
import os
import sys

def usage():
    print("Either:\nvalorant.py {CLIENT_ID}\nvalorant.py {CLIENT_ID} {WEB_BROWSER}")
    print("See README.md")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        usage()
        sys.exit()

    client_id=sys.argv[1]
    browser='google-chrome'
    if len(sys.argv) == 3:
        browser=sys.argv[2]
    DROPSENABLED_TAGID = "c2542d6d-cd10-4532-919b-3d19f30a768b"
    
    while True:
        stream_to_watch = ""
        stream_to_watch_id = -1

        # Find a drops-enabled Valorant stream
        helix = twitch.Helix(client_id=client_id)
        for stream in helix.streams(game_id=516575):
            if DROPSENABLED_TAGID in stream.data['tag_ids']:
                # subprocess.check_call(['google-chrome', 'https://twitch.tv/' + stream.data['user_name']])
                stream_to_watch = stream.data['user_name']
                stream_to_watch_id = stream.data['user_id']
                print("gonna watch " + stream_to_watch)
                webbrowser.get(browser).open('https://twitch.tv/' + stream.data['user_name'])    
                # os.system("google-chrome " + "https://twitch.tv/" + stream.data['user_name'])
                break
        print("watching " + stream_to_watch)

        # Watch the stream until it isnt live
        if stream_to_watch != "":
            live = True
            while live:
                print(stream_to_watch + " still live")
                # Heartbeat every 20 seconds to check that its live
                b = helix.streams(user_id=stream_to_watch_id)
                if len(b._data) >= 1:
                    live = b._data[0].type == "live"
                else:
                    live = False
                time.sleep(20)

            os.system("pkill chrome")


main()
