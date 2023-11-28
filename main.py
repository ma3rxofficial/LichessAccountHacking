import os

import hack_multipart_account
import password_check
import team_deanon
import team_hack
import wordlist
from config import *

def start():
    print(MENU)
    print(MENU_FUNCS) # вывод меню
    func = input(magenta + '[?] Выберите функцию: ')

    if func == '1':
        os.system('cls')
        print(MENU)
        with open("passwords.txt", "r") as passwords:
            hack_multipart_account.start(list(passwords.read()))
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        start()

    elif func == '2':
        os.system('cls')
        print(MENU)
        token = input(magenta + "[?] Введите токен жертвы: ")
        id = input(magenta + "[?] ID команды: ")
        team_hack.hack(team=id)
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        start()

    elif func == '3':
        os.system('cls')
        print(MENU)
        print(cyanlight + "Генерация паролей.")
        choose_4 = input(
            magenta + "Генерация паролей может вызвать теоретическое снижение производительности вашего компьютера. Хотите продолжить? [y/N]")
        if choose_4 == "y" or choose_4 == "Y":
            wordlist.start(number=input(magenta + "[?] Количество паролей: "),
                           length=input(magenta + "[?] Длина пароля: "))
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? ")
            os.system('cls')
            start()

        else:
            os.system('cls')
            start()


    elif func == '4':
        os.system('cls')
        print(MENU)
        print(cyanlight + "Проверка участников по паролю")
        password_check.start(password=input(green + "Введите пароль, которым вы хотите проверить клуб: " + magenta),
                             team=input(yellow + "Введите ID клуба: " + magenta))

        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        start()

    elif func == '5':
        os.system('cls')
        print(MENU)
        print(cyanlight + "Получение информации о всех участниках клуба")
        team_deanon.start()

        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        start()

    elif func == '6':
        os.system('cls')
        print(MENU)
        print("Я ДАУН!!!")
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        start()

    elif func == '0':
        os.system('cls')
        print(MENU)
        exit()


if __name__ == '__main__':
    start()