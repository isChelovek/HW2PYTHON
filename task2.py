# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from tkinter.tix import NoteBook
from os import system
system("cls")

def Get_Num():
    done = True
    while done:
        strUser = input('Введите число - ')
        done = not strUser.isdigit()
        userNum = int(strUser)
        return userNum

def Fact(userNum):
  if(userNum == 0):
    return 1
  else:
    return userNum * Fact(userNum - 1)

userNumer = Get_Num()
factorial = Fact(userNumer)
print(f'Факторил числа {userNumer} = {factorial}')