import random # рандо
from config import *

def start(number, length):
    for n in range(int(number)): # перебор количество паролей, указанном пользователем
        password = '' # изначально пароль пустой
        for i in range(int(length)): # длина пароля, метод с sOF
            password += random.choice(GENERATOR_CHARS) # рандомно выбираем символы

        print(cyanlight +  password) # печатаем пароли
        with open("passwords.txt", "a", encoding="utf-8") as passwords: # открываем словарь паролей
            passwords.write(f"{password} \n") # заносим в него новый пароль

if __name__ == "__main__":
    start(number=input(magenta + "[?] Количество паролей: " + white), length=input(magenta + "[?] Длина пароля: " + white)) # первичная попытка