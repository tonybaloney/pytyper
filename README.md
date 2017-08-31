# PyWriter

Writes source code to the keyboard buffer and randomises the entry to make it look like you're
typing code directly. 

## Installation

To use this module on Mac OS X, you need the PyObjC module installed.
For Python 3, run:
    sudo pip3 install pyobjc-core
    sudo pip3 install pyobjc
For Python 2, run:
    sudo pip install pyobjc-core
    sudo pip install pyobjc
(There's some bug with their installer, so install pyobjc-core first or else
the install takes forever.)
To use this module on Linux, you need Xlib module installed.
For Python 3, run:
    sudo pip3 install python3-Xlib
For Python 2, run:
    sudo pip install Xlib
To use this module on Windows, you do not need anything else.
You will need PIL/Pillow to use the screenshot features.

## Usage

`python typer.py <path to source file>`