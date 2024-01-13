# MADE BY Tevajs AKA f5base
# Orgiginal github: https://github.com/Tevajs/LichAccInfoChecker/blob/main/Checkergitvar.py

import json

import requests
from config import *

def parser(lichess):
    # НЕ АКТУАЛЬНО #lichess = lichess + "_" # Решение проблемы неправильного айди аккаунта

    # Отправляем GET-запрос к API lichess.org
    response = requests.get(f"https://{SERVER}/{API}/{USER}/{lichess}")

    if response.status_code == 200:  # Проверяем успешный ответ от сервера
        user_data = response.json()
        rating_ultrabullet = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_ULTRABULLET}", {}).get(f"{JSON_RATING}")
        rating_bullet = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_BULLET}", {}).get(f"{JSON_RATING}")
        rating_blitz = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_BLITZ}", {}).get(f"{JSON_RATING}")
        rating_rapid = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_RAPID}", {}).get(f"{JSON_RATING}")
        rating_classic = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_CLASSIC}", {}).get(f"{JSON_RATING}")
        rating_correspondence = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_CORRESPONDENCE}", {}).get(f"{JSON_RATING}")

        if rating_blitz is not None:
            rating_blitz = int(rating_blitz)

        if rating_rapid is not None:
            rating_rapid = int(rating_rapid)

        if rating_bullet is not None:
            rating_bullet = int(rating_bullet)

        register_date_timestamp = user_data.get(f"{JSON_CREATEDAT}")

        if register_date_timestamp:
            register_date = datetime.fromtimestamp(register_date_timestamp / 1000).strftime("%d/%m/%Y")
        else:
            register_date = "Дата регистрации не доступна"

        total_games = user_data.get(f"{JSON_COUNT}", {}).get("all")

        print(cyan + "Рейтинг (Ultrabullet):" + green, rating_ultrabullet)
        print(cyan + "Рейтинг (Bullet):" + green, rating_bullet)
        print(cyan + "Рейтинг (Blitz):" + green, rating_blitz)
        print(cyan + "Рейтинг (Rapid):" + green, rating_rapid)
        print(cyan + "Рейтинг (Classic):" + green, rating_classic)
        print(cyan + "Рейтинг (Correspondence):" + green, rating_correspondence)
        print(cyan + "Дата регистрации:" + green, register_date)
        print(cyan + "Количество партий:" + green, total_games)

        # Проверяем наличие титула у аккаунта
        title = user_data.get(f"{JSON_TITLE}")

        if title:
            print("Титул:", title)
        else:
            print(red + "[ERR] У аккаунта нет титула")

        # Проверяем наличие био у аккаунта
        try:
            if json.loads(response.text).get(f"{JSON_PROFILE}").get(f"{JSON_BIO}") == None:  # если нет био
                print(red + "[ERR] Био неизвестно")

            else:
                print(green + "Био:", json.loads(response.text).get(f"{JSON_PROFILE}").get(f"{JSON_BIO}")) # если био есть
        except: # если нет био
            print(red + "[ERR] Био неизвестно")


    else:
        print(red + "[ERR] Не удалось получить информацию об аккаунте")

    time.sleep(1)  # чтобы не получить превышение запросов


if __name__ == "__main__":
    parser(input("Введите имя пользователя: "))
