import os
import sys
from datetime import datetime

def getPath():
    """Absolute path of 'workSpaceRoot/logs/log.txt'"""
    path:str = os.path.abspath(__file__)
    path = path.replace("src\\module\\log.py", "logs\\log.txt")
    print(path)
    return path

def getActualTime():
    # Get the actual time by error
    now = datetime.now()
    timeStamp:str = "["

    # For each arg on datetime.now (except the first one), add it to timeStamp var
    for arg in sys.argv[1:]:
        print(now.strftime(arg))
        timeStamp += now.strftime(arg)

    return timeStamp

def logException(e: Exception):
    """Only for register errors and failed execution!!"""
    
    # timeStamp = (datetime.now().strftime("%d:%m:%y:%H:%M:%S"))

    error = getActualTime() + "]" + "Error: " + str(e.args[0])
    print("error")

    # Save on WorkSpaceRoot/logs/log.txt
    try:
        with open(getPath(), "a", encoding="utf-8") as file:
            file.write(f"\n{error}")
            file.close()
    except:
        with open(getPath(), "w", encoding="utf-8") as file:
            file.write(error)
            file.close()

def logExceptionSTR(e: str):
    """This is only for the errors than you want to write manually"""

    error = getActualTime() + "]" + "Error: " + e

    print("error")
    try:
        with open(getPath(), "a", encoding="utf-8") as file:
            file.write(f"\n{error}")
            file.close()
    except:
        with open(getPath(), "w", encoding="utf-8") as file:
            file.write(error)
            file.close()