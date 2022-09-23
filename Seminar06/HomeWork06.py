# Задание с семинара
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

# def check_isalpha(str):
#     for i in str:  
#         if i.isalpha():
#             return True
    

# def make_list_of_numbers(statement):
#     list_of_numbers = []
#     statement = statement + ' '
#     temp = ''
#     for i in statement:
#         if i.isdigit():
#             temp += i
#         else:
#             list_of_numbers.append(temp)
#             temp = ''
#     list_of_numbers = list(filter(lambda x: x != '', list_of_numbers))
#     list_of_numbers = list(map(float,list_of_numbers))
#     return list_of_numbers

# def make_list_of_operations(statement):
#     list_of_operations = list(filter(lambda x: x == '+' or x == '-' or x == '*' or x == '/' , statement))
#     return list_of_operations

# def reduce_list(i, list1, list2):
#     del list1[i+1]
#     del list2[i]
#     return list1, list2

# def make_calculation(list_of_numbers, list_of_operations):
#     while len(list_of_operations) > 0:
#         while '/' in list_of_operations:
#             for i, element in enumerate(list_of_operations):
#                 if element == '/':
#                     list_of_numbers[i] = list_of_numbers[i] / list_of_numbers[i+1]
#                     reduce_list(i, list_of_numbers, list_of_operations)
#         while '*' in list_of_operations:
#             for i, element in enumerate(list_of_operations):
#                 if element == '*':
#                     list_of_numbers[i] = list_of_numbers[i] * list_of_numbers[i+1]
#                     reduce_list(i, list_of_numbers, list_of_operations)
#         while '-' in list_of_operations:
#             for i, element in enumerate(list_of_operations):
#                 if element == '-':
#                     list_of_numbers[i] = list_of_numbers[i] - list_of_numbers[i+1]
#                     reduce_list(i, list_of_numbers, list_of_operations)  
#         while '+' in list_of_operations:
#             for i, element in enumerate(list_of_operations):    
#                 if element == '+':
#                     list_of_numbers[i] = list_of_numbers[i] + list_of_numbers[i+1]
#                     reduce_list(i, list_of_numbers, list_of_operations)
#     return list_of_numbers[0]           

                
# while True:
#     try:
#         t_str = input('Введите выражение для расчета: ')
#         if check_isalpha(t_str):
#             print('неправильный ввод: нужны числа')
#         else:
#             list_of_numbers = make_list_of_numbers(t_str)
#             # print(f'Список чисел: {list_of_numbers}')
#             list_of_operations = make_list_of_operations(t_str)
#             # print(f'Список операций: {list_of_operations}')
#             print(f'{t_str} => {make_calculation(list_of_numbers, list_of_operations)}')
#             break
#     except:
#         print('Недостаточно числовых данных')          


######################################################################################################################################

# 1- Определить, присутствует ли в заданном списке строк, некоторое число

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwertty", "dkjsfhqwe"]
# f = 'qwe'
# result = len(list(filter(lambda x: f in x, my_list)))
# print(f'список: {my_list}, ищем {f}, ответ {result}')

#####################################################################################################################################
# 2- Найти сумму чисел списка стоящих на нечетной позиции

# my_list = input('Введите числа через пробел: ')
# my_list = list(map(int, my_list.split(' ')))
# sum_of_elements = sum(my_list[1::2])
# print(f'Исходный список: {my_list}, обработанный список: {my_list[1::2]}, сумма элементов: {sum_of_elements}')


####################################################################################################################################
# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# from math import sqrt

# t1 = input('Введите первую точку (через пробел): ')
# t1 = list(map(int, t1.split(' ')))
# t2 = input('Введите вторую точку (через пробел): ')
# t2 = list(map(int, t2.split(' ')))

# length = round(sqrt((t2[0]-t1[0])**2+(t2[1]-t1[1])**2),2)

# print (f'длина отрезка равна: {length}')

######################################################################################################################################
# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# t_str = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# f = "qwe"
# full_list = list(enumerate(t_str))
# short_list = list(filter(lambda x: f in x, full_list))
# if len(short_list) > 1:
#     print(f'список: {t_str}, ищем: "{f}", ответ: {short_list[1][0]}')
# else:
#     print(f'список: {t_str}, ищем: "{f}", ответ: -1')

######################################################################################################################################
# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from math import prod

# my_list = input('Введите числа через пробел: ')
# my_list = list(map(int, my_list.split(' ')))
# n = int(len(my_list)/2)
# print(n)
# first_half_list = my_list[0:n+1]
# second_half_list = list(reversed(my_list[n:]))
# temp_list = list(zip(first_half_list, second_half_list))
# result_list = list(map(prod, temp_list))
# print(f'Исодный список: {my_list}, произведение пар чисел: {result_list}')


#####################################################################################################################################
# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = 5
fibo_list = [(-3)**i for i in range(0,n)]
print(f'Для N = {n}: {fibo_list}')