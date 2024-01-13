import os
from rich.traceback import install
from rich.console import Console
from rich.markdown import Markdown

import hack_multipart_account
import password_check
import team_deanon
import team_hack
import wordlist
from config import *

console = Console()

install(show_locals=True) # инициализация вывода ошибок с помощью рича
os.system("title LiHack by Ma3rX") # ставим название окна терминала

def start():
    print(MENU)
    print(MENU_FUNCS) # вывод меню
    func = input(yellow + f'[{green}?{yellow}] Выберите функцию: ' + white)

    if func == '1':
        os.system('cls')
        print(MENU)
        with open("passwords.txt", "r") as passwords:
            hack_multipart_account.start(passwords.readlines())
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? " + white)
        os.system('cls')
        start()

    elif func == '2':
        os.system('cls')
        print(MENU)
        token = input(magenta + "[?] Введите токен жертвы: " + white)
        id = input(magenta + "[?] ID команды: " + white)
        team_hack.hack(team=id)
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? " + white)
        os.system('cls')
        start()

    elif func == '3':
        os.system('cls')
        print(MENU)
        print(cyanlight + "Генерация паролей.")
        choose_4 = input(
            magenta + "Генерация паролей может вызвать теоретическое снижение производительности вашего компьютера. Хотите продолжить? [y/N]")
        if choose_4 == "y" or choose_4 == "Y":
            wordlist.start(number=input(magenta + "[?] Количество паролей: " + white),
                           length=input(magenta + "[?] Длина пароля: " + white))
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? " + white)
            os.system('cls')
            start()

        else:
            os.system('cls')
            start()


    elif func == '4':
        os.system('cls')
        print(MENU)
        print(cyanlight + "Проверка участников по паролю")
        password_check.start(password=input(green + "Введите пароль, которым вы хотите проверить клуб: " + white),
                             team=input(yellow + "Введите ID клуба: " + white))

        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? " + white)
        os.system('cls')
        start()

    elif func == '5':
        os.system('cls')
        print(MENU)
        print(cyanlight + "Получение информации о всех участниках клуба")
        team_deanon.start()

        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? " + white)
        os.system('cls')
        start()

    elif func == '6':
        os.system('cls')
        print(MENU)
        print(white)
        md = Markdown(AUTHOR_MSG)
        console.print(md)
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? " + white)
        os.system('cls')
        start()

    elif func == '0':
        os.system('cls')
        print(MENU)
        print(white)
        exit()


if __name__ == '__main__':
    start()