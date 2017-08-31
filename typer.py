'''
    PyTyper

    usage: python typer.py <path to source file>

    Requires: pyautogui and requirements for OS.
'''

from __future__ import print_function

import sys
import pyautogui
import time
import random


class Speeds:
    INSTANT = 0.0
    FAST = 0.05
    NORMAL = 0.1
    SLOW = 0.2


CHAR_MAP = {
    ' ': Speeds.INSTANT,
    '(': Speeds.SLOW,
    ')': Speeds.SLOW
}


def calc_pause(character=None):
    try:
        return CHAR_MAP[character]
    except KeyError:
        return random.uniform(0.05, 0.1)

print("Before the timer finishes, set your mouse cursor to the IDE")

for i in range(1, 5):
    time.sleep(1)
    print("Starting in {0}".format(5-i))

with open(sys.argv[1], 'r') as input_file:
    for line in input_file.readlines():
        for c in line:
            time.sleep(calc_pause(c))
            if c == '\n': #  Helps with autocomplete in IDE's
                pyautogui.keyDown('escape')
            pyautogui.press(c)
