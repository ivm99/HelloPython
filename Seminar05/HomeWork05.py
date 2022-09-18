# 1 - Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# def delete_word(text1, text2):
#     list1 = text1.split()
#     list2 = list(filter(lambda x: text2 not in x, list1))
#     text3 = ""
#     for i in list2:
#         text3 = text3 + " " + i
#     return(text3[1:])
    
# text1 = input('Введите текст: ')
# text2 = input('Введите часть слова, которое нужно удалить: ')

# print(delete_word(text1,text2))

##################################################################################################
# 2 - Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# import random

# def imput_game_mode():
#     while True:
#         try:
#             game_mode = int(input('Введите 1 если хотите играть с ботом и 2 если хотите играть с человеком: '))
#             if 1 <= game_mode <=2:
#                 break
#             else:
#                 print('Вы ввели другое число. Попробуйте еще раз')
#         except ValueError:
#             print('Вы ввели не число. Попробуйте еще раз')
#     return game_mode


# def input_limit():
#     while True:
#         try:
#             limit = int(input('Введите максимальное количество конфет, которое будете забирать за раз: '))
#             if limit > 0:
#                 break
#             else:
#                 print('Количество должно быть больше ноля. Попробуйте еще раз')
#         except ValueError:
#             print('Вы ввели не число. Попробуйте еще раз')
#     return limit

# def input_total():
#     while True:
#         try:
#             total = int(input('Введите общее количество конфет: '))
#             if total > limit:
#                 break
#             else:
#                 print('Слишком мало конфет для этой игры. Попробуйте еще раз')
#         except ValueError:
#             print('Вы ввели не число. Попробуйте еще раз')
#     return total

# def draw():
#     queue = random.randint(1,2)
#     if queue == 1:
#         print('Первым ходит первый игрок')
#     else:
#         print('Первым ходит второй игрок')
#     return queue

# def step(total, limit, player):
#     if player == 1:
#         while True:
#             try:
#                 m = int(input(f'Первый игрок берет(не более {limit} конфет): '))
#                 if 0 < m < limit+1:
#                     break
#                 else:
#                     print(f'Введенное число {m} не входит в указанный диапазон (1-{limit}).\nПопробуйте еще раз')
#             except ValueError:
#                 print('Вы ввели не число. Попробуйте еще раз')
#     else:
#         while True:
#             try:
#                 m = int(input(f'Второй игрок берет(не более {limit} конфет): '))
#                 if 0 < m < limit+1:
#                     break
#                 else:
#                     print(f'Введенное число {m} не входит в указанный диапазон (1-{limit}).\nПопробуйте еще раз')
#             except ValueError:
#                 print('Вы ввели не число. Попробуйте еще раз')
#     total = total - m
#     print(f'Осталось конфет: {total}')
#     return total

# def step_bot(total, limit):
#     m = (total-1)%(limit+1)
#     total = total - m
#     print(f'Бот взял конфет: {m}')
#     print(f'Осталось конфет: {total}')
#     return total

# game_mode = imput_game_mode()
# limit = input_limit()
# total = input_total()

# if game_mode == 1:
#     player = 1
#     if total > limit:
#         while total > limit:
#             if player == 1:
#                 total = step(total, limit, player)
#                 player = 2
#             else:
#                 total = step_bot(total, limit)
#                 player = 1
#     if total <= limit:
#         while total > 0:
#             limit = total
#             if player == 1:
#                 total = step(total, limit, player)
#                 player = 2
#             else:
#                 total = step_bot(total, limit)
#                 player = 1
#     if player == 1:
#         print('Выиграл первый игрок!')
#     else:
#         print ('Выиграл бот!')
    
# else:
#     player = draw()
#     if total > limit:
#         while total > limit:
#             total = step(total, limit, player)
#             if player == 1:
#                 player = 2
#             else:
#                 player = 1
#     if total <= limit:
#         while total > 0:
#             limit = total
#             total = step(total, limit, player)
#             if player == 1:
#                 player = 2
#             else:
#                 player = 1
#     if player == 1:
#         print('Выиграл первый игрок!')
#     else:
#         print ('Выиграл второй игрок!')

###########################################################################################

# 3-Создайте два списка — один с названиями языков программирования, другой — с числами 
# от 1 до длины первого.
# ['python', 'c#']
# [1, 2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера 
# и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в
# делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на
# сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# Дополнительно(по желанию):
# 1 - Создайте программу для игры в ""Крестики-нолики"".
# 2 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.



def make_kortege_list(list1):
    list1 = list(map(lambda item: item.upper(), list1))
    list1 = list(enumerate(list1,1))
    return list1

def transfer_name_to_number(language_name):
    number = 0
    for i in language_name:
        number += ord(i)
    return number
    
def replace_languages_to_numbers(list4):
    list4 = list(map(list, list4))
    for i in list4:
        i[1] = transfer_name_to_number(i[1])
    list4 = list(map(tuple,list4))
    return list4

def list_filter(list_names, list_numbers):
    list_names = list(map(list, list_names))
    list3 = []
    for i, item in enumerate(list_numbers):
        if item[1]%item[0] == 0:
            list_names[i][0] = item[1]
            list3.append(list_names[i])
    list3 = list(map(tuple, list3))
    return list3

language_list = ['Abap',	'Ada',	'C#',	'C', 'C++',	'Cobol',	'Dart',	'Delphi',
                 'Pascal',	'Go', 'Groovy',	'Haskell',	'Java',	'JavaScript',	'Julia',
                 'Kotlin',	'Lua',	'Matlab', 'Objective-C',	'Perl',	'PHP',	'Python',
                 'R',	'Ruby',	'Rust',	'Scala', 'Swift',	'TypeScript',	'VBA',
                 'Visual Basic']

list_with_names = make_kortege_list(language_list)
print('Исходный список:')
print(list_with_names)
list_with_numbers = replace_languages_to_numbers(list_with_names)
final_list = list_filter(list_with_names,list_with_numbers)
print('Итоговый список:')
print(final_list)
