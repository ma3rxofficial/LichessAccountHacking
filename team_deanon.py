import ndjson # джейсон специально для лича Lichess.org

from config import * # инициализируем все из конфига
from parser import * # активируем парсер

def deanon_default(team):
    r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}') # посылаем запрос на получение всех пользователей тимы
    data = r.json(cls=ndjson.Decoder) # декодируем полученную инфу

    print(green + "[+] Список пользователей получен!") # печатаем об успешном получении пользователей

    for member in data: # перебор всех участников
        print(yellow + f"""
------------------------------------------------------------
               {member[JSON_NAME]} - Информация
------------------------------------------------------------
        """) # отстранение
        parser(member[JSON_NAME]) # печатаем им. пользователя

    print("------------------------------------------------------------") # Отстранение, линия

def deanon_multipart(team_list):
        print(team_list.split()) # печатаем сплитированный список команд
        for team in team_list.split(): # перебор всех команд
            print(team) # печатаем команду
            r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}') # посылаем запрос на получение всех пользователей тимы
            data = r.json(cls=ndjson.Decoder) # декодируем полученную инфу

            print(green + f"[+] Список пользователей получен!") # печатаем об успешном получении пользователей

            for member in data: # перебор всех участников
                print(yellow + f"""
            ------------------------------------------------------------
                           {member[JSON_NAME]} - Информация
            ------------------------------------------------------------
                    """) # отстранение
                parser(member[JSON_NAME]) # печатаем им. пользователя

            print("------------------------------------------------------------") # Отстранение, линия

def start():
    answer = input(cyan + "Выберите режим [multipart/DEFAULT]: " + white) # выбор режима

    if answer == "":
        deanon_default(team=input(magenta + "[?] ID команды: " + white)) # дефолтный режим, спрашиваем айди команды

    elif answer == "default":
        deanon_default(team=input(magenta + "[?] ID команды: " + white)) # дефолтный режим, спрашиваем айди команды

    elif answer == "DEFAULT":
        deanon_default(team=input(magenta + "[?] ID команды: " + white)) # дефолтный режим, спрашиваем айди команды

    elif answer == "multipart":
        deanon_multipart(team_list=input(magenta + "Введите список клубов(через пробел): " + white)) # мультипартный режим, спрашиваем список клубов

    elif answer == "MULTIPART": # multipart CAPS LOCK <--- пример капслока, заглавные буквы
        deanon_multipart(team_list=input(magenta + "Введите список клубов(через пробел): " + white))  # мультипартный режим, спрашиваем список клубов

if __name__ == "__main__":
    start() # основная функция старт
