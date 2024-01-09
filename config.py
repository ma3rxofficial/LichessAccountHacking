import random
import time
import platform
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

# MENU
MENU = blue + f"""
        {yellow}

                ██╗     ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
                ██║     ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝
                ██║     ██║███████║███████║██║     █████╔╝ 
                ██║     ██║██╔══██║██╔══██║██║     ██╔═██╗ 
                ███████╗██║██║  ██║██║  ██║╚██████╗██║  ██╗
                ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                                                          {yellow}[Разработчик: {green}Ma3rX{yellow}]
                                                          {yellow}[Версия: {green}2.1.6{yellow}]
                                                          {yellow}Ваша система - [{green}{platform.system()}{yellow}]

      __________________________________________________________________________________________
      |                                                                                        |
      | [{green}Discord{yellow}] - @Ma3rX                                                                     |
      |                                                                                        |
      | [{green}YouTube{yellow}] - https://www.youtube.com/channel/UC-c6q0jLeUd6XrtfCvzQotQ                   |
      |________________________________________________________________________________________|

    """

MENU_FUNCS = f"""
        [{green}1{yellow}] Хак аккаунтов(мултипарт)
        [{green}2{yellow}] Кик участников из команды
        [{green}3{yellow}] Генератор паролей
        [{green}4{yellow}] Проверка паролем
        [{green}5{yellow}] Деанон клуба
        [{green}6{yellow}] Сообщение от автора
        [{red}0{yellow}] Выход
"""

# SERVER SETTINGS

SERVER = "lichess.org"
API = "api"
TEAM = "team"
LOGIN = "login"
USERS = "users"
USER = "user"
PM_ALL = "pm-all"

# JSON GETTING SETTINGS
JSON_PROFILE = "profile"
JSON_USERNAME = "username"
JSON_BIO = "bio"
JSON_FIRSTNAME = "firstName"
JSON_LASTNAME = "lastName"
JSON_PERFS = "perfs"
JSON_RATING = "rating"
JSON_ULTRABULLET = "ultrabullet"
JSON_BULLET = "bullet"
JSON_BLITZ = "blitz"
JSON_RAPID = "rapid"
JSON_CLASSIC = "classic"
JSON_CORRESPONDENCE = "correspondence"
JSON_CREATEDAT = "createdAt"
JSON_COUNT = "count"
JSON_TITLE = "title"


# PATHS
CHECKING_PATH = "hacked_checking"
HACKEDREAL_PATH = "hacked_real"
DEANON_PATH = "deanon_saves"

# TIMEOUT FOR BRUTEFORCE SETTINGS
PASSWORDCHECK_TIMEOUT = 20
HACKMULTIPART_TIMEOUT = 20

# LOGIN SETTINGS
USER_AGENT =  "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
X_REQUESTED_WITH = "XMLHttpRequest"
REMEMBER = "true"

# TEAM HACK SETTINGS
msg = """
    Team was destroyed by Ma3rX programm eZZ
    github: https://github.com/ma3rxofficial/LichessAccountHacking
"""
TOKEN = "CHANGEME"
HEADS = {'Authorization': f'Bearer {TOKEN}'}

# RESPONSE SETTINGS
OK_RESPONSE = 200
ERROR_RESPONSE = 401
BLOCKED_RESPONSE = 429

# DEANON SETTINGS
DEANON_SAVING = True

# PASSWORDS PATHS
PASSWORDS_DICT_PATH = "./passwords.txt"
PASSWORDS_POPULAR_PATH = "./mb_passwords.txt"

# GENERATOR PASSWORDS SETTINGS
GENERATOR_CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

### TIMESAMP GETTING ###
def get_ts():
    timestamp = time.time()
    # convert to datetime
    date_time = datetime.fromtimestamp(timestamp)

    # convert timestamp to string in dd-mm-yyyy HH:MM:SS

    str_dt = date_time.strftime("%d-%m-%Y, %H:%M:%S")

    return f"| {str_dt} |"
