import berserk # парсер для личесса
import ndjson # джейсон специально для лича Lichess.org
import requests # реквесты

from config import * #  # инициализируем все из конфига


def hack(team):
    session = berserk.TokenSession(TOKEN) # делаем сессию с токеном
    client = berserk.Client(session=session) # делаем клиентскую сессию с этим токеном

    r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}') # получаем список пользователей указанной команды
    data = r.json(cls=ndjson.Decoder) # декодируем полученную инфу

    print(green + "[+] Список пользователей получен!") # печатаем об успешном получении пользователей

    session.post(f'https://{SERVER}/{TEAM}/' + team + f'/{PM_ALL}', data={'message': msg}, headers=HEADS).json() # рассылка, сообщение указано в config.py
    print("[+] Рассылка успешна отправлена!") # сообщаем об успешном отправлении рассылки

    for i in data: # перебор пользователей
        user = i[f'{JSON_USERNAME}'] # получаем имя каждого пользователя
        client.teams.kick_member(team, user) # кикаем пользователя за пользователем
        print(f"[+] {user} кикнут!") # сообщаем о кике


if __name__ == "__main__":
    hack(team=input(magenta + "[?] ID команды: " + white)) # первичная попытка
