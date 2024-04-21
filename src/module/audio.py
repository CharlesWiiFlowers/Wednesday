import os
from pytube import YouTube

# Peronal imports
from log import logException

def getPath():
    """Get the path for 'data' on WorkSpaceRoot"""
    path:str = os.path.abspath()
    path = path.replace("src/module/audio.py", "data/")
    print(path)
    return path

async def downloadAudioYoutube(link: str):
    """Only give me your URL and I gift your lastAudio.mp3 on /root/data"""

    try:
        yt = YouTube(url=link, on_progress_callback=[](), on_complete_callback=[]())
        stream = yt.streams.get_audio_only()
        stream.download(output_path=getPath(), filename="lastAudio.mp3")

    except Exception as e:
        logException(e=e)