# 1 - Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# 54 7 234 90 12 5


# s = input('Введите числа через пробел: ')

# data = s.split(' ')
# data = list(map(int,data))

# min_num = data[0]
# max_num = data[0]

# for i in data:
#     if i > max_num:
#         max_num=i
#     elif i < min_num:
#         min_num=i

# print(data)
# print(f'минимальный элемент {min_num}, максимальный элемент {max_num}')


# 2 - Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел. НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def NOD(a,b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif a > b:
        return NOD(a%b, b)
    else:
        return NOD(b%a, a)


def NOK(a, b):
    return  a*b / NOD(a, b)
print(int(NOK(a, b)))





# 3 - Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Число N вводится пользователем. Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку, то в файле вряд ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.
