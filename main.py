import pyuac
import pyautogui
import keyboard
import time
import random
import detected_fish
from datetime import datetime 

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()

print(f'{datetime.now().replace(microsecond=0)} || BOT loading. Please wait 5 second!')
time.sleep(5)

while True:
    print(f'{datetime.now().replace(microsecond=0)} || Start catch fish!')
    keyboard.press_and_release('e')
    time.sleep(0.2)
    keyboard.press_and_release('`')

    detected_fish.detected()
    print(f'{datetime.now().replace(microsecond=0)} || Pulling Out fish!')
    pyautogui.mouseDown(button='left')
    time.sleep(15)
    pyautogui.mouseUp(button='left')
    
    print(f'{datetime.now().replace(microsecond=0)} || EZ FISH!!!')
    pause = random.random().__round__(1) + random.random().__round__(1)
    if pause < 0.5:
        pause = 0.5
    time.sleep(0.1)
    keyboard.press_and_release('`')
    time.sleep(pause)