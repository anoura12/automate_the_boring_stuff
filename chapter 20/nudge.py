import pyautogui
import time

while(True):
    p = pyautogui.position()
    pyautogui.moveTo(p[0] + 5, p[1], duration=0.25)
    time.sleep(10)
    


