import random # рандомизатор
import time # время
import platform # платформа(для определения системы пользователя)
from datetime import datetime # вторая импорта времени))
from rich.console import Console # консоль ричовская
from rich.markdown import Markdown # система rich-markdown

from colorama import Fore # цветной текст

all_col = [Fore.RED,                # красный
           Fore.CYAN,               # голубой
           Fore.LIGHTCYAN_EX,       # светло-голубой
           Fore.BLUE,               # синий
           Fore.LIGHTCYAN_EX,       # светло-голубой 2 вариант
           Fore.LIGHTMAGENTA_EX,    # светло-фиолетовый(малиновый)
           Fore.YELLOW,             # желтый
           Fore.GREEN,              # зеленый
           Fore.WHITE,              # белый

           ] # все цвета

ran = random.choice(all_col) # случайный цвет

# COLORS

red = all_col[0] # красный
cyan = all_col[1] # голубой
cyanlight = all_col[2] # светло-голубой
blue = all_col[3] # синий
cyanlight2 = all_col[4] # светло-голубой 2 вариант
magenta = all_col[5] # светло-фиолетовый(малиновый)
yellow = all_col[6] # желтый
green = all_col[7] # зеленый
white = all_col[8] # белый(дефолтный)

# MENU
VERSION = "2.2.3" # версия
MENU = blue + f""" 
        {yellow}

                ██╗     ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
                ██║     ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝
                ██║     ██║███████║███████║██║     █████╔╝ 
                ██║     ██║██╔══██║██╔══██║██║     ██╔═██╗ 
                ███████╗██║██║  ██║██║  ██║╚██████╗██║  ██╗
                ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                                                          {yellow}[Разработчик: {green}Ma3rX{yellow}]
                                                          {yellow}[Версия: {green}{VERSION}{yellow}]
                                                          {yellow}Ваша система - [{green}{platform.system()}{yellow}]

      __________________________________________________________________________________________
      |                                                                                        |
      | [{green}Discord{yellow}] - @Ma3rX                                                                     |
      |                                                                                        |
      | [{green}YouTube{yellow}] - https://www.youtube.com/channel/UC-c6q0jLeUd6XrtfCvzQotQ                   |
      |________________________________________________________________________________________|

    """ # баннер меню, основной

MENU_FUNCS = f"""
        [{green}1{yellow}] Хак аккаунтов(мултипарт)
        [{green}2{yellow}] Кик участников из команды
        [{green}3{yellow}] Генератор паролей
        [{green}4{yellow}] Проверка паролем
        [{green}5{yellow}] Деанон клуба
        [{green}6{yellow}] Взлом по цифровой части
        [{red}0{yellow}] Выход
""" # вывод функций

# SERVER SETTINGS
SERVER = "lichess.org" # адрес сервера

# API SETTINGS
API = "api"  # апи
TEAM = "team" # тима
LOGIN = "login" # логин
USERS = "users" # юзеры
USER = "user" # юзер
PM_ALL = "pm-all" # рассылка
KICK = "kick" # кикнуть юзера

# JSON GETTING SETTINGS
JSON_PROFILE = "profile" # профиль
JSON_USERNAME = "id" # исходное имя юзера
JSON_PROXY_USERNAME = "username" # имя юзера со стороны прокси
JSON_PROXY_PASSWORD = "password" # пароль юзера со стороны прокси
JSON_NAME = "name" # имя юзера с поддержкой заглавных букв
JSON_BIO = "bio" # био юзера в профиле
JSON_FIRSTNAME = "firstName" # имя
JSON_LASTNAME = "lastName" # фамилия
JSON_PERFS = "perfs" # инфа о рейтингах
JSON_RATING = "rating" # рейтинг
JSON_ULTRABULLET = "ultrabullet" # ультрапуля
JSON_BULLET = "bullet" # пуля
JSON_BLITZ = "blitz" # блиц
JSON_RAPID = "rapid" # рапид
JSON_CLASSIC = "classic" # классика
JSON_CORRESPONDENCE = "correspondence" # игра по переписке
JSON_CREATEDAT = "createdAt" # создано в
JSON_COUNT = "count" # количество
JSON_TITLE = "title" # заголовок


# PATHS
CHECKING_PATH = "hacked_checking" # папка где сохраняются взломанные акки проверкой пароля
HACKEDREAL_PATH = "hacked_real" # папка где сохраняются взломанные акки мультипартным хаком

# TIMEOUT FOR BRUTEFORCE SETTINGS
PASSWORDCHECK_TIMEOUT = 20 # таймоаут при каждом 10м подборе в проверке пароля
HACKMULTIPART_TIMEOUT = 20 # таймоаут при каждом 10м подборе в мультипартном хаке
SAVE_EVERYTHING_MULTIPART = True # сохранять невзломанные аккаунты в мультипартном хаке
SAVE_EVERYTHING_CHECK = True # сохранять невзломанные аккаунты в проверке паролем

# LOGIN SETTINGS
USER_AGENT =  "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" # поддельная инфа(от нашего лица)
USER_FISH_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 GLS/100.10.9939.100" # доп. поддельная инфа о подключаемом юзере
X_REQUESTED_WITH = "XMLHttpRequest" # X-запрос
REMEMBER = "true" # запоминать логин

# TEAM HACK SETTINGS
msg = """
    Team was destroyed by Ma3rX programm eZZ
    github: https://github.com/ma3rxofficial/LichessAccountHacking
""" # сообщение рассылки при захвате клуба
TOKEN = "CHANGEME" # токен
HEADS = {'Authorization': f'Bearer {TOKEN}'} # html-заголовки

# RESPONSE SETTINGS
OK_RESPONSE = 200 # номер нормального запроса
ERROR_RESPONSE = 401 # номер ошибки
BLOCKED_RESPONSE = 429 # номер заблокированного запроса

# PASSWORDS PATHS
PASSWORDS_DICT_PATH = "./passwords.txt" # путь к словарю паролей
PASSWORDS_POPULAR_PATH = "./mb_passwords.txt" # путь к популярным паролям

# GENERATOR PASSWORDS SETTINGS
GENERATOR_CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890' # символы для генератора

"""
    К сожалению, дорогие защитники СВЧ, сюда можно добавить любые символы, так что ваши способы защиты немножко не будут работать ))
    Слава НБ!
"""

### TIMESAMP GETTING ###
def get_ts():
    timestamp = time.time() # получение времени
    # конвертация в нормальное время
    date_time = datetime.fromtimestamp(timestamp)

    # конвертация dd-mm-yyyy HH:MM:SS

    str_dt = date_time.strftime("%d-%m-%Y, %H:%M:%S") # конвертируем

    return f"| {str_dt} |" # вывод функции
