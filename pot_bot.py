# DANNY POT BOT 8/11/2023
# NOTE THIS WILL ONLY WORK ON 1440p DISPLAYS AS THE X/Y COORDINATES WILL CHANGE

import time
import win32api
import pyautogui
import random
import keyboard


# Method to yoink x and y coordinates
# Gets current mouse position on the screen
def get_cursor_position():
    x, y = win32api.GetCursorPos()
    return x, y


def on_key_event():
    if keyboard.is_pressed('esc'):
        print("Pot Bot stopped by user.")
        exit()


# The Actual Bot (not a bot)
def pot_bot():
    # Cords In Order
    # (890, 703)
    # 37.44
    # (1218, 750)
    # 35.85
    # (1399, 758)
    # 1.57
    current_rotations = 0
    while current_rotations < 32:
        start_time = time.time()

        # Go Through the crafting
        # pyautogui.moveTo(629, 704, random.uniform(0.01, 0.2))
        pyautogui.moveTo(890, 703, random.uniform(0.01, 0.2))
        pyautogui.leftClick()
        pyautogui.leftClick()

        # pyautogui.moveTo(1218, 750, random.uniform(0.3, 0.5))
        time.sleep(1.63)
        pyautogui.keyDown('f')
        pyautogui.keyUp('f')
        while time.time() - start_time < 38.6:
            on_key_event()

        start_time = time.time()
        # pyautogui.moveTo(1399, 758, random.uniform(0.3, 0.6))
        pyautogui.keyDown('g')
        pyautogui.keyUp('g')
        while time.time() - start_time < 37.6:
            on_key_event()

        # Increment
        current_rotations = current_rotations + 1


# Attributes
rotations_amount = 32

# Actual Code
print("Pot Bot Time? (Y/N) There will be a 3 Second Delay")
danny_input = input()
if danny_input == 'Y' or danny_input == 'y':
    print("Created By Garrett: Version 1.2")
    print("Starting POT BOT!!!")
    time.sleep(3)
    pot_bot()
else:
    print("Pot man is sad, not starting")
