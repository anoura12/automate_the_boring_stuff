import pyautogui
import time


while(True):
    p = pyautogui.position() #gives current position of the cursor
    pyautogui.moveTo(p[0] + 5, p[1], duration=0.25) #moves the cursor by 5 units in the x-axis
    time.sleep(10) #gives the cursor a time lag of 10 seconds
    


