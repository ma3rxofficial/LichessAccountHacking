import ndjson

from config import *
from parser import *


def deanon_default(team):
    r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}')
    data = r.json(cls=ndjson.Decoder)

    print(green + "[+] Список пользователей получен!")
    if DEANON_SAVING:
        print(yellow + f"[{red}!{yellow}]В конфиге было включено сохранение информации")

    for member in data:
        print(cyan + f"""
------------------------------------------------------------
               {member["username"]} - Информация
------------------------------------------------------------
        """)
        parser(member["username"])

    print("------------------------------------------------------------")

def deanon_multipart(team_list):
        print(team_list.split())
        for team in team_list.split():
            print(team)
            r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}')
            data = r.json(cls=ndjson.Decoder)

            print(green + f"[+] Список пользователей получен!")

            for member in data:
                print(cyan + f"""
            ------------------------------------------------------------
                           {member["username"]} - Информация
            ------------------------------------------------------------
                    """)
                parser(member["username"])
            print("------------------------------------------------------------")

def start():
    answer = input(cyan + "Выберите режим [multipart/DEFAULT]: ")

    if answer == "":
        deanon_default(team=input(magenta + "[?] ID команды: "))

    elif answer == "default":
        deanon_default(team=input(magenta + "[?] ID команды: "))

    elif answer == "DEFAULT":
        deanon_default(team=input(magenta + "[?] ID команды: "))

    elif answer == "multipart":
        deanon_multipart(team_list=input(magenta + "Введите список клубов(через пробел): "))

    elif answer == "MULTIPART":
        deanon_multipart(team_list=input(magenta + "Введите список клубов(через пробел): "))

if __name__ == "__main__":
    start()
