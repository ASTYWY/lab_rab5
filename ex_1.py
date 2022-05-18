#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    s = input("что бы узнать длину слова, нyжно само слово. Введи ее ")
    print("введенное слово имеет",len(s),"символов")

    #3 задание, сделанно
    s.replace("o", " ")
    if "o" in s[0]:
        print(s.replace("o", ""))
    s.replace("l", " ")
    if "l" in s[-1]:
        print(s.replace("l", ""))
        
    #2
    s = s.replace(" ", "")
    if s == s[::-1]:
        print("'YES',  ваше слово является палиндромом")
    else:
        print("'NO dear', ваше слово не является палиндромом")
        
    #задание 1
    s = s[::-1]
    print("заданнове вами словоб в перевернутом виде: "+ s)