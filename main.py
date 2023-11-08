import os

import hack_multipart_account
import password_check
import team_deanon
import team_hack
import wordlist
from config import *


def funcs_print():
    menu = blue + f"""
        {cyanlight2}
           ,--,                                                                             
        ,---.'|                                         ,--,                                
        |   | :                        ,---,          ,--.'|                           ,-.  
        :   : |     ,--,             ,--.' |       ,--,  | :                       ,--/ /|  
        |   ' :   ,--.'|             |  |  :    ,---.'|  : '                     ,--. :/ |  
        ;   ; '   |  |,              :  :  :    |   | : _' |                     :  : ' /   
        '   | |__ `--'_       ,---.  :  |  |,--.:   : |.'  |  ,--.--.     ,---.  |  '  /    
        |   | :.'|,' ,'|     /     \ |  :  '   ||   ' '  ; : /       \   /     \ '  |  :    
        '   :    ;'  | |    /    / ' |  |   /' :'   |  .'. |.--.  .-. | /    / ' |  |   \   
        |   |  ./ |  | :   .    ' /  '  :  | | ||   | :  | ' \__\/: . ..    ' /  '  : |. \  
        ;   : ;   '  : |__ '   ; :__ |  |  ' | :'   : |  : ; ," .--.; |'   ; :__ |  | ' \ \ 
        |   ,/    |  | '.'|'   | '.'||  :  :_:,'|   | '  ,/ /  /  ,.  |'   | '.'|'  : |--'  
        '---'     ;  :    ;|   :    :|  | ,'    ;   : ;--' ;  :   .'   \   :    :;  |,'     
                  |  ,   /  \   \  / `--''      |   ,/     |  ,     .-./\   \  / '--'       
                   ---`-'    `----'             '---'       `--`---'     `----'                            1.8.0

         {blue}                                                   Functions by Ma3rX, Python_UT, Tevajs.
                                                                With you after first SVC vs MARCO war!{yellow}
        [1] Хак аккаунтов(мултипарт)
        [2] Кик участников из команды
        [3] Генератор паролей
        [4] Проверка паролем
        [5] Деанон клуба
        [6] Сообщение от автора
        [7] Выход

    """

    print(menu)


def start():
    func = input(magenta + '[?] Выберите функцию: ')

    if func == '1':
        os.system('cls')
        with open("passwords.txt", "r") as passwords:
            hack_multipart_account.start(list(passwords.read()))
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        funcs_print()
        start()

    elif func == '2':
        os.system('cls')
        token = input(magenta + "[?] Введите токен жертвы: ")
        id = input(magenta + "[?] ID команды: ")
        team_hack.hack(token=token, team=id)
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        funcs_print()
        start()

    elif func == '3':
        os.system('cls')
        print(cyanlight + "Генерация паролей.")
        choose_4 = input(
            magenta + "Генерация паролей может вызвать теоретическое снижение производительности вашего компьютера. Хотите продолжить? [y/N]")
        if choose_4 == "y" or choose_4 == "Y":
            wordlist.start(number=input(magenta + "[?] Количество паролей: "),
                           length=input(magenta + "[?] Длина пароля: "))
            print(green + "[+] Готово.")
            input(magenta + "[?] Продолжить? ")
            os.system('cls')
            funcs_print()
            start()

        else:
            os.system('cls')
            funcs_print()
            start()


    elif func == '4':
        os.system('cls')
        print(cyanlight + "Проверка участников по паролю")
        password_check.start(password=input(green + "Введите пароль, которым вы хотите проверить клуб: " + magenta),
                             team=input(yellow + "Введите ID клуба: " + magenta))

        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        funcs_print()
        start()

    elif func == '5':
        os.system('cls')
        print(cyanlight + "Получение информации о всех участниках клуба")
        team_deanon.start()

        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        funcs_print()
        start()

    elif func == '6':
        os.system('cls')
        print("Я ДАУН!!!")
        print(green + "[+] Готово.")
        input(magenta + "[?] Продолжить? ")
        os.system('cls')
        funcs_print()
        start()

    elif func == '7':
        os.system('cls')
        print("--------------Выход--------------")
        exit()


if __name__ == '__main__':
    funcs_print()
    start()