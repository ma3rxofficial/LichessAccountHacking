import ndjson

from config import *
from parser import *


def deanon(team):
    r = requests.get('https://lichess.org/api/team/' + team + '/users')
    data = r.json(cls=ndjson.Decoder)

    print(green + "[+] Список пользователей получен!")

    for member in data:
        print(cyan + f"""
------------------------------------------------------------
               {member["username"]} - Информация
------------------------------------------------------------
        """)
        parser(member["username"])
    print("------------------------------------------------------------")


if __name__ == "__main__":
    deanon(team=input(magenta + "[?] ID команды: "))
