# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 6782 -> 23
# 0,56 -> 11 


from os import system
system("cls")

def GetNumberFloat():
   while type:
      print('Вещественная часть должна быть отделенная точкой')
      input_string = input('Введите число  - ')
      try:
         number_float = float(input_string)
         return number_float
      except ValueError:
         print('Это не число') 

def FindSummDigit(numFloat):
   strFloat = str(abs(numFloat)).replace('.', '')
   summ = 0
   for i in range(len(strFloat)):
      summ += int(strFloat[i])
   return summ

print()
print('Программа принимает на вход вещественное число и показывает сумму его цифр')


print(FindSummDigit(GetNumberFloat()))