import cv2 as cv
from time import time
import time as tym
import os
import pyautogui as pg
import numpy as np
from windowcapture import WindowCapture
import win32gui
from ctypes import windll, Structure, c_long, byref
from playsound import playsound

os.chdir(os.path.dirname(os.path.abspath(__file__)))

winTitle = "Iskolar Ran Online"
count = 0
loop_time = time()
threshold = 0.9
pg.FAILSAFE = True
pg.PAUSE = 0.1

enchantCoord = {"x": 0, "y": 0}
yesCoord = {"x":0, "y": 0}
firstBox = {"x": 0, "y": 0, "w": 0, "h": 0}

sealedType = 2
    
def Sealed(height):
    img_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    target = cv.imread('images/blocker/enchant.png',0)
    w, h = target.shape[::-1]
    res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + height), (0,0,0), -1)


def InitWindow():
     # Move window

    hwnd = win32gui.FindWindow(None, winTitle)
    desktop = win32gui.GetDesktopWindow()
    l,t,r,b = win32gui.GetWindowRect(hwnd)
    dt_l, dt_t, dt_r, dt_b = win32gui.GetWindowRect(desktop)
    centre_x, centre_y = win32gui.ClientToScreen( desktop, ( (dt_r-dt_l)//2, (dt_b-dt_t)//2) )
    win32gui.MoveWindow(hwnd, -8, 0, r-l, b-t, 0) 

def InitCoordinates():
    img_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    target = cv.imread('images/buttons/enchant.png',0)
    w, h = target.shape[::-1]
    res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)
        enchantCoord["x"] = pt[0] + 30
        enchantCoord["y"] = pt[1] + 40

    img_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    target = cv.imread('images/buttons/yes.png',0)
    w, h = target.shape[::-1]
    res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)
        yesCoord["x"] = pt[0] + 30
        yesCoord["y"] = pt[1] + 40

    img_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    target = cv.imread('images/blocker/enchant.png',0)
    w, h = target.shape[::-1]
    res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        firstBox["x"] = pt[0]
        firstBox["y"] = pt[1]
        firstBox["w"] = w
        firstBox["h"] = h


def OnClickFirstBox():
    pg.moveTo(firstBox["x"]+15, firstBox["y"]+62)
    pg.mouseDown()
    pg.mouseUp()

def OnClickSecondBox():
    pg.moveTo(firstBox["x"]+15, firstBox["y"]+82)
    pg.mouseDown()
    pg.mouseUp()

def Next():
    pg.moveTo(enchantCoord["x"], enchantCoord["y"])
    pg.mouseDown()
    pg.mouseUp()
    pg.moveTo(yesCoord["x"], yesCoord["y"])
    pg.mouseDown()
    pg.mouseUp()


if __name__ == '__main__':
    wincap = WindowCapture(winTitle)
    newWindowTile = win32gui.GetWindowText (win32gui.GetForegroundWindow())
    screenshot = wincap.get_screenshot()

    InitCoordinates()
    InitWindow()

    if not enchantCoord["x"] or not enchantCoord["y"]:
        exit()

    if not yesCoord["x"] or not yesCoord["y"]:
        exit()


    while(True):
        wincap = WindowCapture(winTitle)
        newWindowTile = win32gui.GetWindowText (win32gui.GetForegroundWindow())
        # get an updated image of the game
        screenshot = wincap.get_screenshot()
        
        if (sealedType == 1):
            # 1 sealed
            Sealed(42)
        
        if (sealedType == 2):
            # 2 sealed
            Sealed(62)

        img_gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

        # win32gui.MoveWindow(hwnd, centre_x-(r//2), centre_y-(b//2), r-l, b-t, 0) 

        target = cv.imread('images/goals/attack.png',0)
        w, h = target.shape[::-1]
        res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
        loc_1 = np.where( res >= 0.99)

        for pt in zip(*loc_1[::-1]):
            cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

        target = cv.imread('images/goals/energy.png',0)
        w, h = target.shape[::-1]
        res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
        loc_2 = np.where( res >= 0.99)

        for pt in zip(*loc_2[::-1]):
            cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

        target = cv.imread('images/goals/accuracy.png',0)
        w, h = target.shape[::-1]
        res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
        loc_3 = np.where( res >= 0.97)
        
        for pt in zip(*loc_3[::-1]):
            cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)


        # target = cv.imread('images/goals/max1.png',0)
        # w, h = target.shape[::-1]
        # res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
        # loc_1 = np.where( res >= threshold)

        # for pt in zip(*loc_1[::-1]):
        #     cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

        # target = cv.imread('images/goals/max2.png',0)
        # w, h = target.shape[::-1]
        # res = cv.matchTemplate(img_gray,target,cv.TM_CCOEFF_NORMED)
        # loc_2 = np.where( res >= threshold)

        # for pt in zip(*loc_2[::-1]):
        #     cv.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

        # cv.rectangle(screenshot, pt, (firstBox["x"] + , pt[1] + h), (0,0,255), 1)

        # if np.any(loc_1) or np.any(loc_2):

        if np.any(loc_1) or np.any(loc_2) or np.any(loc_3):
            print("Valid")
            playsound("uwu.mp3")
            break
        else:
            print("Invalid")
            if sealedType >= 1:
                OnClickFirstBox()
            if sealedType >= 2:
                OnClickSecondBox()
            if sealedType >= 0:
                Next()

        # Show display
        cv.imshow('Computer Vision', screenshot)

        loop_time = time()

        if cv.waitKey(1) == 27:
            cv.destroyAllWindows()
            break

    print('Done.')