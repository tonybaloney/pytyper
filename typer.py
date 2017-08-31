from __future__ import print_function

import sys
import pyautogui
import time
import random


def calc_pause(character=None):
    return random.uniform(0.1, 0.2)

print("Before the timer finishes, set your mouse cursor to the IDE")
for i in range(1, 5):
    time.sleep(1)
    print("Starting in {0}".format(5-i))

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        pyautogui.typewrite(line, interval=calc_pause)
