import os
import sys
from datetime import datetime
from multipledispatch import dispatch

def getPath():
    """Absolute path of 'workSpaceRoot/logs/log.txt'"""
    path:str = os.path.abspath()
    path = path.replace("src/module/log.py", "logs/log.txt")
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

# Use @dispatch for overload this method
@dispatch(Exception)
def logException(e: Exception):
    """This is only for register errors and failed execution!!"""
    
    # timeStamp = (datetime.now().strftime("%d:%m:%y:%H:%M:%S"))

    error = getActualTime() + "]" + "Error: " + str(e.args[0])

    # Save on WorkSpaceRoot/logs/log.txt
    with open(getPath(), "a+", encoding="utf-8") as file:
        file.write(error)

@dispatch(str)
def logException(e: str):
    """This is only for the errors than you want to write manually"""

    error = getActualTime() + "]" + "Error: " + e

    with open(getPath(), "a+", encoding="utf-8") as file:
        file.write(error)