import pyautogui
import time
import subprocess

#1

subprocess.call("C:\\Users\\dell\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")


time.sleep(2)
print("starting....")

#2
while True:
        join = pyautogui.locateOnScreen('join.png')
        if join != None:
            pyautogui.click(join)
            print("Clicked Join")
            break
        else:
            print("Could not find join 1")

while True:
     window = pyautogui.locateOnScreen('join window.png')
     if window != None:
          print('cum into the unkown')
          break
     else:
          print('fat')

pyautogui.typewrite('4148248863')
      
while True:
        join2 = pyautogui.locateOnScreen('join2.png')
        if join2 != None:
            pyautogui.click(join2)
            print("Clicked Join")
            break
        else:
            print("Could not find join2")

time.sleep(2)

while True:
        passw = pyautogui.locateOnScreen('pass.png')
        if passw != None:
            break
        else:
            print("Could not find pass")

pyautogui.typewrite('123')
pyautogui.hotkey("enter")