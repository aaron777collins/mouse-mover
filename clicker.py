import dependencies as dependencies
dependencies.installAll()

import pyautogui
import time
import random
from pynput import keyboard
import secrets
import logging

width, height = pyautogui.size()

MIN_WAIT = 1
MAX_WAIT = 30

running = True

pyautogui.FAILSAFE = False

def get_logger():
    return logging.getLogger("clicker")

def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    pass


def on_release(key):

    global running

    if key == keyboard.Key.esc:
        # Stop listener
        running=False
        get_logger().warning("ESC pressed. Ending program..")
        return False

    try:
        pass
        # if (key.char == 'e'):
        #     running=False
    except AttributeError:
        pass


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


def move_mouse():
    pyautogui.moveTo(random.randint(0, width), random.randint(0, height), random.randint(0, 3))

if __name__ == "__main__":
    # main method
    random.seed(secrets.randbelow(100000))

    logging.basicConfig(level = logging.INFO) # makes it so info level information is logged

    get_logger().info("Press ESC to exit the program!")

    while(running):
        move_mouse()
        max = random.randint(MIN_WAIT,MAX_WAIT)
        get_logger().info("Waiting " + str(max) + " seconds before next movement.")
        counter = 0
        while(counter <= max and running):
            time.sleep(1.0)
            counter+=1
    
    logging.info("Program ended!")