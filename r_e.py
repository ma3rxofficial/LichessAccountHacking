# -*- coding: utf-8 -*-

def translit(string):
    letters = {u'А': u'A',
               u'Б': u'B',
               u'В': u'V',
               u'Г': u'G',
               u'Д': u'D',
               u'Е': u'E',
               u'Ё': u'E',
               u'З': u'Z',
               u'И': u'I',
               u'Й': u'Y',
               u'К': u'K',
               u'Л': u'L',
               u'М': u'M',
               u'Н': u'N',
               u'О': u'O',
               u'П': u'P',
               u'Р': u'R',
               u'С': u'S',
               u'Т': u'T',
               u'У': u'U',
               u'Ф': u'F',
               u'Х': u'H',
               u'Ъ': u'',
               u'Ы': u'Y',
               u'Ь': u'',
               u'Э': u'E',
               u'Ж': u'Zh',
               u'Ц': u'Ts',
               u'Ы': u'Y',
               u'Ч': u'Ch',
               u'Ш': u'Sh',
               u'Щ': u'Sch',
               u'Ю': u'Yu',
               u'Я': u'Ya',
               u'а': u'a',
               u'б': u'b',
               u'в': u'v',
               u'г': u'g',
               u'д': u'd',
               u'е': u'e',
               u'ё': u'e',
               u'ж': u'zh',
               u'з': u'z',
               u'и': u'i',
               u'й': u'y',
               u'к': u'k',
               u'л': u'l',
               u'м': u'm',
               u'н': u'n',
               u'о': u'o',
               u'п': u'p',
               u'р': u'r',
               u'с': u's',
               u'т': u't',
               u'у': u'u',
               u'ф': u'f',
               u'х': u'h',
               u'ц': u'ts',
               u'ч': u'ch',
               u'ш': u'sh',
               u'щ': u'sch',
               u'ъ': u'',
               u'ы': u'y',
               u'ь': u'',
               u'э': u'e',
               u'ю': u'yu',
               u'я': u'ya'}

    string2 = ''

    for i in string:
        try:
            string2 = string2 + letters[i]
        except:
            string2 = string2 + i

    return string2

MARKDOWN = """
# This is an h1

- huy
- chlen
- pizda
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)