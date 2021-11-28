from numpy.core.records import record
import pyautogui
import cv2
from pathlib import Path
import numpy as np
import os

resolution = (1920, 1080)
fps = 60.0
codec = cv2.VideoWriter_fourcc(*"XVID")

def recordScreen():
    recordScreen.counter = int(readCounterVal())

    filename = Path("srecord.avi")

    if filename.is_file():
        filename = f"srecord{str(recordScreen.counter)}.avi"
        recordScreen.counter += 1
        writeCounterVal(str(recordScreen.counter))

    out = cv2.VideoWriter(str(filename), codec, fps, resolution)

    print("Recording started...")

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        out.write(frame)
        
        # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    print("Screen Recording done!")

    print(os.path.abspath(str(filename)))

    # Release the Video writer
    out.release()
    # Destroy all windows
    cv2.destroyAllWindows()

def writeCounterVal(value):
    f = open("counterValSR.txt", "w")

    if not Path("counterValSR.txt").is_file():
        f.write("0")
    else:
        f.write(value)

    f.close()

def readCounterVal():
    if not Path("counterValSR.txt").is_file():
        content = "0"
    else:
        f = open("counterValSR.txt", "r")
        content = f.read()
        f.close()

    return content


if __name__ == "__main__":
    recordScreen()
