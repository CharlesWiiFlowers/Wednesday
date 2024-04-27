import os
import whisper

def getPath():
    """Get the path for 'lastAudio.mp3' on WorkSpaceRoot"""
    path:str = os.path.abspath(__file__)
    path = path.replace("src/module/audio.py", "data/lastAudio.mp3")
    print(path)
    return path

def transcriptor(model: str):
    """Transcribe the lastAudio"""

    # Recive the "model"
    whispy = whisper.load_model(model)
    result = whispy.transcribe(getPath())

    return result