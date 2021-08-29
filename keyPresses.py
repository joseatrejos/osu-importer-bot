from pynput.keyboard import Key, Controller
import time
import os

keyboard = Controller()

timeout = 60*5   # Time in seconds
timeout_start = time.time()

while time.time() < timeout_start + timeout:
    time.sleep(2.5)

    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.shift)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.release(Key.shift_l)
    keyboard.press(Key.enter)
