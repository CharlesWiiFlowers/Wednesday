import os
from pytube import YouTube

# Peronal imports
from module.log import logException

def getPath():
    """Get the path for 'data' on WorkSpaceRoot"""
    path:str = os.path.abspath()
    path = path.replace("src/module/audio.py", "data/")
    print(path)
    return path

class audio():

    def __init__(self) -> None:
        pass

    async def downloadAudioYoutube(link: str):
        """Only give me your URL and I gift your lastAudio.mp3 on /root/data"""

        #  on_progress_callback= , on_complete_callback=lambda :

        try:
            yt = YouTube(url=link)
            stream = yt.streams.get_audio_only()
            stream.download(output_path=getPath(), filename="lastAudio.mp3")

        except Exception as e:
            logException(e=e)

    def download(link: str):
        """This distinguise on Youtube link and then make it download."""

        print("What?")

        # Check if "link" string has a substring
        if "youtube" in link:
            audio.downloadAudioYoutube(link=link)
        else:
            logException(e="Link site isn't defined or not supported")