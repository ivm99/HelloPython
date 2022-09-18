# Задача 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# def find_prime_factors(n):
#     '''Функция состаляет список простых множителей числа N'''
#     data = []
#     if n%2 == 0:                                        #проверка на кратность 2-м
#        data.append(2)                                   #деление исходного числа на 2
#        n = int(n/2)
#     i=3
#     while i < n:                                        #проверка на кратность нечетных чисел начиная с 3-х
#         if n%i == 0:
#             if all(i != item for item in data):         #проверка содержится ли данное число в списке data
#                 data.append(i)
#             n = int(n / i)                              #деление исходного числа на проверяемое кратное число
#         if n%i !=0:                                     #проверка делится ли оставшееся число на тоже самое кратное число еще раз, если нет, то берем следующее число
#             i+=2
#     if any(n%i == 0 for i in data):                     #Проверка итогового остатка от деления, возможно он является также является простым множеством
#         return data
#     else:
#         data.append(n)
#         return data


# while True:
#     try:
#         n = int(input('Введите число: '))
#         print(f'N = {n} -> ', find_prime_factors(n))
#         break
#     except:
#         print('Введенное значение не является числом')


##################################################################################################################################################


# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


# def sort_list_identical(data):
#     new_data = []
#     for i in data:
#         if all(i != item for item in new_data):                 #Проверка входит ли число из изначального списка в новый список
#             new_data.append(i)
#     return new_data

# data = [1,1,1,1,2,2,2,3,3,3,4]

# print(data, ' -> ', sort_list_identical(data))


#################################################################################################################################################

# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4


# data = []
# file = open('Students.txt', 'r', encoding='utf-8')
# for line in file:
#     if '5' in line:
#         line = line.upper()
#     data.append(line)
# file.close()
# file = open('Students.txt', 'w', encoding='utf-8')
# for i in data:
#     file.write(i)
# file.close()


##################################################################################################################################################

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def encrypt_text(user_text:str, n:int):
    original = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" 
    new = original[-n*2:]+original[:-n*2]
    new_text = ""
    index = 0
    for i in user_text:
        for j in original:
            if i == j:
                index = original.index(i)
        if i!=" " and i!="." and i!="," and i!="!" and i!="?" and i!= "-" and not i.isdigit():
            i = i.replace(i,new[index])
        new_text += i
    return(new_text)

def decrypt_text(text:str, n:int):
    original = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" 
    new = str(original[-n*2:]+original[:-n*2])
    new_text = ""
    index = 0
    for i in text:
        for j in new:
            if i == j:
                index = new.index(j)
        if i!=" " and i!="." and i!="," and i!="!" and i!="?" and i!= "-" and not i.isdigit():
            i = i.replace(i,original[index])
        new_text += i
    return(new_text)

user_text = input('Введите текст для шифрования: ') 
n=int(input('Введите ключ шифрования (число): '))%26

new_text = encrypt_text(user_text, n)
print(new_text)
with open('encrypted_file.txt', 'w') as data:
    data.write(new_text)
    
m = int(input('Введите ключ дешифрования (число): '))%26

with open('encrypted_file.txt', 'r') as data:
    text = data.read()

print(decrypt_text(text,m))

##################################################################################################################################################
# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

# def RLE_compression(user_text):
#     new_list=[]
#     count = 1
#     i = 1
#     while i < len(user_text):
#         if user_text[i-1] == user_text[i]:
#             count +=1
#         else:
#             count = str(count)
#             char = user_text[i-1]+count
#             new_list.append(char)
#             count = 1
#         i+=1 
#     i=0
#     count = 1
#     while user_text[-1-i] == user_text[-2-i]:
#         count+=1
#         i+=1
#     count = str(count)
#     char = user_text[-1]+count
#     new_list.append(char)  
#     return new_list
    
# def RLE_restore(compressed_text):
#     text = ""
#     print(compressed_text)
#     new_list = []
#     i=0
#     while i < len(compressed_text):
#         new_list.append(compressed_text[i][1:])
#         new_list[i] = int(new_list[i])
#         i+=1
#     for index, element  in enumerate(compressed_text):
#         element = element[:1]
#         j=0
#         while j < new_list[index]:
#             text = text + element
#             j+=1
#     return(text)
        
# with open('file1.txt', 'r') as data:
#     us_text = data.read()
        
# text = str(RLE_compression(us_text))

# with open('file2.txt', 'w') as data:
#     data.write(text)
        
    
    
    



# with open('initial_file.txt', 'r') as data:
#         text = data.read()


