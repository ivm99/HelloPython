# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def Create_List_Of_Numbers(n):

#     ''' Функция создает список чисел от ввода пользователем в терминале'''


#     numbers = []
#     i = 0

#     while i < n:

#         print(f'Введите {i}-е число: ', end="")
#         numbers.append(input())
#         i = i + 1

#     numbers = list(map(int, numbers))
#     return numbers


# def Find_Sum_Uneven_Position(numbers):

#     '''Фнкция вычисляет сумму чисел на нечетных позициях в списке'''

#     sum_uneven = 0
#     i = 1

#     while i < len(numbers):
#         sum_uneven += numbers[i]
#         i+=2
#     return sum_uneven

# while True:
#     try:
#         n = int(input('Введите количество чисел в списке: ' ))
#         break
#     except:
#         print('Введенное значение не является числом.')


# user_numbers = Create_List_Of_Numbers(n)

# print(user_numbers)
# print(Find_Sum_Uneven_Position(user_numbers))

########################################################################################################################################

# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# def Create_List_By_User():

#     '''Функция создает список чисел из строки, введенной пользователем'''

#     data = input('Введите числа через пробел: ')

#     data = data.split(' ')

#     data = list(map(int,data))

#     return data


# def Proivz_By_Pair(numbers):

#     '''Функция создает список произведений парных чисел из списка, введенного пользователем. Парой считаются первый и последний элемент, второй и предпоследний и т.д.'''

#     new_data = []
#     i = 0
#     l = len(numbers)

#     while i < l/2:
#         new_data.append(numbers[i]*numbers[l-1-i])
#         i+=1

#     return new_data

# numbers = Create_List_By_User()
# print(numbers, ' -> ', end='')
# print(Proivz_By_Pair(numbers))


########################################################################################################################################

# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

# def Create_List_By_User_Float():

#     '''Функция создает список чисел из строки, введенной пользователем'''

#     data = input('Введите числа через пробел: ')

#     data = data.split(' ')

#     data = list(map(float,data))

#     return data

# def Find_Max_And_Min(numbers):

#     '''Функция находит разницу между максимальным и минимальным значением дробной части элементов в списке'''

#     max_number = numbers[0] % 1
#     min_number = max_number

#     for i in numbers[1:]:
#         i = i % 1
#         if i > max_number:
#             max_number = i
#         elif i < min_number:
#             min_number = i
#     return round(max_number - min_number,2)

# numbers = Create_List_By_User_Float()

# print(numbers, ' -> ', end='')
# print(Find_Max_And_Min(numbers))


############################################################################################################################################
# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

# def Convert_To_Binary(number:int) -> str:

#     '''Функция преобразовывает десятичное число в двоичное'''

#     ostatok: str =""

#     if number // 2 == 0:
#         return 1
#     else:
#         ostatok = str(Convert_To_Binary(number//2)) + str(number%2)
#         return(ostatok)

# number = int(input('Введите число: '))
# print(Convert_To_Binary(number))


#########################################################################################################################################
# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

def Make_Fibonacci_list(number):

    data = [0, 1]
    
    i = 1
    while i < number:

        data.append(data[i-1] + data[i])
        i += 1
    
    i = 0
    k=1
    while i < number*2:
        data.insert(0,data[i+1]*k)
        i+=2
        k=-k
    
    return data

number = int(input('Введите число: '))
print(Make_Fibonacci_list(number))
