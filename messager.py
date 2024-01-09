import time

import berserk


def hack(token, users, msg, spammer_mode):
    heads = {'Authorization': f'Bearer {token}'}

    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    if spammer_mode == "y" or spammer_mode == "Y":
        spammer_mode = True

    else:
        spammer_mode = False

    if spammer_mode:
        while True:
            time.sleep(1)
            for user in users:
                r = session.post(f'https://lichess.org/inbox/{user}', data={'text': msg}, headers=heads).json()
                if r["ok"]:
                    print(f"{user} sended!")
    else:
        for user in users:
            r = session.post(f'https://lichess.org/inbox/{user}', data={'text': msg}, headers=heads).json()
            if r["ok"]:
                print(f"{user} sended!")


if __name__ == "__main__":
    hack(token=input("Напишите свой токен: "), users=input("Напишите список пользователей: "),
         spammer_mode=input("Включить spammer_mode?(y/N) "),
         msg=input("Напишите сообшение, которое хотите отправить? "))
