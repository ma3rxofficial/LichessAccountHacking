import random
import time
from datetime import datetime

from colorama import Fore, Style

all_col = [Style.BRIGHT + Fore.RED,
           Style.BRIGHT + Fore.CYAN,
           Style.BRIGHT + Fore.LIGHTCYAN_EX,
           Style.BRIGHT + Fore.LIGHTBLUE_EX,
           Style.BRIGHT + Fore.LIGHTCYAN_EX,
           Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
           Style.BRIGHT + Fore.LIGHTYELLOW_EX,
           Style.BRIGHT + Fore.LIGHTGREEN_EX,

           ] # list of colors

ran = random.choice(all_col) # random color

# COLORS

red = all_col[0]
cyan = all_col[1]
cyanlight = all_col[2]
blue = all_col[3]
cyanlight2 = all_col[4]
magenta = all_col[5]
yellow = all_col[6]
green = all_col[7]

# SERVER SETTINGS

SERVER = "lichess.org"

# TEAM HACK SETTINGS
msg = """
    Team was destroyed by Ma3rX programm eZZ
    github: https://github.com/ma3rxofficial/LichessAccountHacking
"""

# SOME FUNCS

### TIMESAMP GETTING ###
def get_ts():
    timestamp = time.time()
    # convert to datetime
    date_time = datetime.fromtimestamp(timestamp)

    # convert timestamp to string in dd-mm-yyyy HH:MM:SS

    str_dt = date_time.strftime("%d-%m-%Y, %H:%M:%S")

    return f"| {str_dt} |"
