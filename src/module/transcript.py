import os
import whisper

def getPath():
    """Get the path for 'lastAudio.mp3' on WorkSpaceRoot"""
    path:str = os.path.abspath()
    path = path.replace("src/module/audio.py", "data/lastAudio.mp3")
    print(path)
    return path

def transcriptor(model: str):
    """Transcribe the lastAudio"""

    # Recive the "model"
    model = whisper.load_model(model)
    result = model.transcribe(getPath())

    return result
