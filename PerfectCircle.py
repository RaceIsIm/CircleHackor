import numpy as np
import win32api
import pyautogui
import time

#F11 To fullscreen your browser!

ready = True
aim_key = 0x14 #https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
r = 380 #Radius of your circle
circle_steps = 25 #Corners? of your circle i guess?, lower = faster (2 linear 3 = triangle, 4 = square)
width, height = pyautogui.size() #Screen size X , Y
y_offset = (1 / 27) * height #Offset of the center white dot
center_x, center_y = width / 2, (height - y_offset) / 2 #Center point

#Sleep MS
def Sleep(MS):
    time.sleep((MS / 1000))

#Keystate
def IsKeyHeld(key):
    if win32api.GetAsyncKeyState(key) & 0x8000:
        return True
    else:
        return False


def Circle(radius, steps):
    pyautogui.mouseDown()
    Sleep(5)
    for i in range(steps + 2): #+2 to fully finish the circle
        if IsKeyHeld(aim_key):  
            angle = i * (2.0 * np.pi / steps)
            dx = int(center_x + radius * np.cos(angle))
            dy = int(center_y + radius * np.sin(angle))
            pyautogui.moveTo(dx,dy)
    pyautogui.mouseUp()

while True:
    if win32api.GetAsyncKeyState(aim_key):
        if ready:
            pyautogui.moveTo((center_x+ r), center_y) #Move mouse to Beginning of circle
            Sleep(5)
            Circle(r, circle_steps)
            ready = False
            Sleep(1000)
    if not IsKeyHeld(aim_key):
        ready = True