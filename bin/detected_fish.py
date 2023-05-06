import cv2
import numpy as np
import mss
from datetime import timedelta
from datetime import datetime
import keyboard
import time

def detected():
    start = datetime.now().replace(microsecond=0)
    def frame():
        sct = mss.mss()
        monitor = {'top': 200, 'left': 0, 'width': 1920, 'height': 600}
        img = np.array(sct.grab(monitor))
        img = np.flip(img[:, :, :3], 2)  # 1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 2
        return img

    number = 0
    stop = 0
    massiv = []
    vektor = 'None'


    while True:
        time.sleep(0.1)
        number += 1
        img = frame()

        template = cv2.imread('bin/data/fish.png')
        w, h = template.shape[:-1]

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            stop += 1
            massiv.append(pt[0])

            if stop == 2:
                if massiv[0] > massiv[1]:
                    if massiv[0] - massiv[1] > 5:
                        if vektor == 'up' or vektor == 'None':
                            vektor = 'down'
                            keyboard.release('a')
                            keyboard.press('d')

                if massiv[0] < massiv[1]:
                    if massiv[1] - massiv[0] > 5:
                        if vektor == 'down' or vektor == 'None':
                            vektor = 'up'
                            keyboard.release('d')
                            keyboard.press('a')

                stop = 0
                massiv = [] 
            print(f"{datetime.now().replace(microsecond=0)} || Fish Detected || Cord: x: {pt[0]}, y: {pt[1]} || Vektor: {vektor}")
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        
        if datetime.now().replace(microsecond=0) - start == timedelta(seconds = 51):
            keyboard.release('d')
            keyboard.release('a')
            return