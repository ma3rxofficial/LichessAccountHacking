import random
from config import *

def start(number, length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for n in range(int(number)):
        password =''
        for i in range(int(length)):
            password += random.choice(chars)

        print(cyanlight +  password)
        with open("passwords.txt", "a", encoding="utf-8") as passwords:
            passwords.write(f"{password} \n")

if __name__ == "__main__":
    start(number=input(magenta + "[?] Количество паролей: "), length=input(magenta + "[?] Длина пароля: "))
