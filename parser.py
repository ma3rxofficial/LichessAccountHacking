# MADE BY Tevajs AKA f5base
# Orgiginal github: https://github.com/Tevajs/LichAccInfoChecker/blob/main/Checkergitvar.py

import json # импорт парсера с личесса

import requests # реквесты
from config import * # активация конфига

def parser(lichess):
    # НЕ АКТУАЛЬНО #lichess = lichess + "_" # Решение проблемы неправильного айди аккаунта

    # Отправляем GET-запрос к API lichess.org
    response = requests.get(f"https://{SERVER}/{API}/{USER}/{lichess}")

    if response.status_code == 200:  # Проверяем успешный ответ от сервера
        user_data = response.json() # получаем информацию о пользователе
        rating_ultrabullet = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_ULTRABULLET}", {}).get(f"{JSON_RATING}") # рейтинг в ультрапулю
        rating_bullet = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_BULLET}", {}).get(f"{JSON_RATING}") # рейтинг в пулю
        rating_blitz = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_BLITZ}", {}).get(f"{JSON_RATING}") # рейтинг в блиц
        rating_rapid = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_RAPID}", {}).get(f"{JSON_RATING}") # рейтинг в рапид
        rating_classic = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_CLASSIC}", {}).get(f"{JSON_RATING}") # рейтинг в классику
        rating_correspondence = user_data.get(f"{JSON_PERFS}", {}).get(f"{JSON_CORRESPONDENCE}", {}).get(f"{JSON_RATING}") # рейтинг в игру по переписке

        if rating_blitz is not None: # если получили рейтинг в блице
            rating_blitz = int(rating_blitz) # делаем вывод не строкой, а числом

        if rating_rapid is not None: # если получили рейтинг в рапиде
            rating_rapid = int(rating_rapid) # делаем вывод не строкой, а числом

        if rating_bullet is not None: # если получили рейтинг в пуле
            rating_bullet = int(rating_bullet) # делаем вывод не строкой, а числом

        register_date_timestamp = user_data.get(f"{JSON_CREATEDAT}") # дата регистрации

        if register_date_timestamp: # если получили дату регистрации
            register_date = datetime.fromtimestamp(register_date_timestamp / 1000).strftime("%d/%m/%Y") # вычисляем правильную дату регистрации
        else: # если не получили
            register_date = "Дата регистрации не доступна"

        total_games = user_data.get(f"{JSON_COUNT}", {}).get("all") # все игры пользователя

        print(cyan + "Рейтинг (Ultrabullet):" + green, rating_ultrabullet) # Тут думаю все понятно, выводим полученную инфу ))
        print(cyan + "Рейтинг (Bullet):" + green, rating_bullet)
        print(cyan + "Рейтинг (Blitz):" + green, rating_blitz)
        print(cyan + "Рейтинг (Rapid):" + green, rating_rapid)
        print(cyan + "Рейтинг (Classic):" + green, rating_classic)
        print(cyan + "Рейтинг (Correspondence):" + green, rating_correspondence)
        print(cyan + "Дата регистрации:" + green, register_date)
        print(cyan + "Количество партий:" + green, total_games)

        # Проверяем наличие титула у аккаунта
        title = user_data.get(f"{JSON_TITLE}")

        if title: # если есть титул
            print("Титул:", title) # печатаем его
        else: # если нет титула
            print(red + "[ERR] У аккаунта нет титула") # печатаем что нет

        # Проверяем наличие био у аккаунта
        try: # попытка
            if json.loads(response.text).get(f"{JSON_PROFILE}").get(f"{JSON_BIO}") == None:  # если нет био
                print(red + "[ERR] Био неизвестно") # печатаем что био нету

            else: # если есть
                print(green + "Био:", json.loads(response.text).get(f"{JSON_PROFILE}").get(f"{JSON_BIO}")) # печатаем био полученное
        except: # если нет био
            print(red + "[ERR] Био неизвестно") # печатаем что био неизвестно)


    else: # не получилось получить инфу об акке
        print(red + "[ERR] Не удалось получить информацию об аккаунте") # печатаем об этом

    time.sleep(1)  # чтобы не получить превышение запросов


if __name__ == "__main__":
    parser(input("Введите имя пользователя: ")) # первичная проверка на им. пользователя
