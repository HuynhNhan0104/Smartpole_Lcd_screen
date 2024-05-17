import vlc
import streamlink

# url = "https://www.youtube.com/watch?v=NCq2BK0zhNM"
url="https://www.youtube.com/watch?v=rKn4EQ3-Ns0"
stream = streamlink.streams(url)
url = stream['best'].to_url()
print(url)
vlc_instance = vlc.Instance('--verbose=2')
video_player = vlc_instance.media_player_new()
video_player.set_mrl(url)
# p.set_fullscreen(True)
video_player.play()
while True: 
    try:
        pass
    except: 
        break