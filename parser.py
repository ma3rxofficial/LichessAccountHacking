# MADE BY Tevajs AKA f5base
# Orgiginal github: https://github.com/Tevajs/LichAccInfoChecker/blob/main/Checkergitvar.py

import json
import time
from datetime import datetime

import requests
from config import *

def parser(lichess):
    # НЕ АКТУАЛЬНО #lichess = lichess + "_" # Решение проблемы неправильного айди аккаунта

    # Отправляем GET-запрос к API lichess.org
    response = requests.get(f"https://{SERVER}/api/{USER}/{lichess}")

    if response.status_code == 200:  # Проверяем успешный ответ от сервера
        user_data = response.json()
        rating_blitz = user_data.get("perfs", {}).get("blitz", {}).get("rating")
        rating_rapid = user_data.get("perfs", {}).get("rapid", {}).get("rating")
        rating_bullet = user_data.get("perfs", {}).get("bullet", {}).get("rating")

        if rating_blitz is not None:
            rating_blitz = int(rating_blitz)

        if rating_rapid is not None:
            rating_rapid = int(rating_rapid)

        if rating_bullet is not None:
            rating_bullet = int(rating_bullet)

        register_date_timestamp = user_data.get("createdAt")

        if register_date_timestamp:
            register_date = datetime.fromtimestamp(register_date_timestamp / 1000).strftime("%d/%m/%Y")
        else:
            register_date = "Дата регистрации не доступна"

        total_games = user_data.get("count", {}).get("all")

        print("Рейтинг (Blitz):", rating_blitz)
        print("Рейтинг (Rapid):", rating_rapid)
        print("Рейтинг (Bullet):", rating_bullet)
        print("Дата регистрации:", register_date)
        print("Количество партий:", total_games)

        # Проверяем наличие титула у аккаунта
        title = user_data.get("title")

        if title:
            print("Титул:", title)
        else:
            print("У аккаунта нет титула")

        # Проверяем наличие био у аккаунта
        try:
            print("Био:", json.loads(response.text).get("profile").get("bio"))
        except:
            print("Био неизвестно")

    else:
        print("Не удалось получить информацию об аккаунте")

    time.sleep(1)  # чтобы не получить превышение запросов


if __name__ == "__main__":
    parser(input("Введите имя пользователя: "))
