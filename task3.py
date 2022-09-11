# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.


from os import system
import itertools
import time
system("cls")

def Get_Num():
    done = True
    while done:
        strUser = input('Введите число - ')
        done = not strUser.isdigit()
        userNum = int(strUser)
        return userNum

def reverNumerInt(userNumer):
    userStr = str(userNumer)
    result = userStr[::-1]
    return int(result)

def isLefEqalsRight(numer):
    userStr = str(numer)
    result = userStr[::] == userStr[::-1]
    return result

def isPolindrom(userNumer):
    while not isLefEqalsRight(userNumer):
        userNumer = userNumer + reverNumerInt(userNumer)
    return userNumer
    
def imitationLoad():
    for x in range(3):
        time.sleep(.5) #Задердка в 500мс
        print('.', end = ' ')

userNumer = Get_Num()
polinrom = isPolindrom(userNumer)
imitationLoad()
print()
print(f'Полиндром числа {userNumer} является {polinrom}')
print()
