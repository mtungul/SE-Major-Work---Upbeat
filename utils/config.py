import os
import sys

width = 1350
height = 750

def resource_path(relative_path): #makes game not crash if app is not opened from terminal or vscode
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)