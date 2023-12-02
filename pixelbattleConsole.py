"""Main module"""

# = Import =

from colorama import Fore, Back, Style
from pbConfig import *


# = Global Variables =

Canvas = [[" " for _ in range(SizeX)] for _ in range(SizeY)]
"""Global canvas"""


# = Functions =

def ClearCanvas():
    """Clear canvas"""
    global Canvas
    Canvas = [[" "]*SizeX]*SizeY

def SetPixel(x:int, y:int, color:str):
    """Set one pixel"""
    global Canvas
    if (x < 0) or (y < 0) or (x >= SizeX) or (y >= SizeY):
        return
    try:
        Canvas[y][x] = getattr(Back, color) + " " + Back.RESET
    except AttributeError:
        print(Fore.BLACK + 'BLACK')
        print(Fore.BLUE + 'BLUE')
        print(Fore.CYAN + 'CYAN')
        print(Fore.GREEN + 'GREEN')
        print(Fore.LIGHTBLACK_EX + 'LIGHTBLACK_EX')
        print(Fore.LIGHTBLUE_EX + 'LIGHTBLUE_EX')
        print(Fore.LIGHTCYAN_EX + 'LIGHTCYAN_EX')
        print(Fore.LIGHTGREEN_EX + 'LIGHTGREEN_EX')
        print(Fore.LIGHTMAGENTA_EX + 'LIGHTMAGENTA_EX')
        print(Fore.LIGHTRED_EX + 'LIGHTRED_EX')
        print(Fore.LIGHTWHITE_EX + 'LIGHTWHITE_EX')
        print(Fore.LIGHTYELLOW_EX + 'LIGHTYELLOW_EX')
        print(Fore.MAGENTA + 'MAGENTA')
        print(Fore.RED + 'RED')
        print(Fore.RESET + 'RESET')
        print(Fore.WHITE + 'WHITE')
        print(Fore.YELLOW + 'YELLOW', Fore.RESET)

def Fill(x1:int, y1:int, x2:int, y2:int, color:(int, int, int)):
    """Fill rectangle"""
    global Canvas
    for x in range(x1, x2):
        for y in range(y1, y2):
            SetPixel(x, y, color)

def Show():
    """Show canvas"""
    global Canvas
    for line in Canvas:
        print("".join(line), end="")
        print()