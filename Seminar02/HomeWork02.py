# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

# while True:

#     numberStr = input('Введите число: ')

#     try:
#         print (f'{numberStr} -> ', end='')

#         numberStr = numberStr.replace('.', '')
#         numberStr = numberStr.replace(',', '')
#         numberStr = numberStr.replace('-', '')

#         sum = 0

#         for i in numberStr:
#             i = int(i)
#             sum += i

#         print(sum)

#         break

#     except:
#         print ('Введенное значение не является числом!')

###############################################################################################################################################

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# while True:
#     try:
#         number = int(input('Введите число: '))

#         setNumber = []
#         factorial = 1

#         for i in range(1,number+1):
#             factorial *= i
#             setNumber.append(factorial)

#         print(f'пусть N = {number}, тогда {setNumber}')

#         break

#     except:

#         print('Введенное значение не является числом!')

######################################################################################################################

# Задача 3. Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

# def NumberTransform(number):
#             newNumber = 0
#             while number%10>0:
#                 ostatok = number%10
#                 number = number//10
#                 newNumber = newNumber*10+ostatok
#             return newNumber

# while True:
#     try:

#         number = int(input('Введите число: '))

#         newNumber = NumberTransform(number)

#         while number != newNumber:
#             number +=newNumber
#             newNumber = NumberTransform(number)

#         print(f'Палиндром равен {number}')

#         break

#     except:

#          print('Введенное значение не является числом!')

#######################################################################################################################
# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def random(min, max):
    range = max - min
    randomNumber = int(time.time()*1000)
    randomNumber %= range
    randomNumber += min
    return randomNumber

while True:
    try:
        min = int(input('Введите начало диапазона для генерации случайного числа: '))
        max = int(input('Введите конец диапазона для генерации случайного числа: '))
        print(random(min, max))
        break
    except:
        print('Введенное значение не является числом!')

