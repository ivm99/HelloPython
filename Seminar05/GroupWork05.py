import random
n = random.randint(1,10)
print(f"Натуральная степень {n}")
list1 = [random.randint(1,100)]
for i in range(1, n + 1):
    list1.append(random.randint(0,100))
print(f"Список коэффициентов: {list1}")
list_x = []
for i in range(n + 1):
    list_x.insert(0, "x**" + str(i))
print(list_x)

polinom = list(zip(list1, list_x))
print(polinom)

s=str("")
for i, element in enumerate(polinom):
    for j in element:
        s = s + str(j)
    s = s + "+"
s = s[]
    
        
print(s)

####################################################################################

n = input_testing_number("Введите число целое: ")

list_of_coef = random_list(0, 3, n)
list_of_coef.append(random_list(1, 100, 1).pop())

print(list_of_coef)
str = f"{list_of_coef[n]}*x^{n}"
i = n-1
while i > 0:
    if list_of_coef[i] == 0:
        i -= 1
        continue
    elif i == 1:
        str += f" + {list_of_coef[i]}*x"
    else:
        str += f" + {list_of_coef[i]}*x^{i}"
    i -= 1
else:
    str += f" + {list_of_coef[0]}"
print(str)

with open("Our_polynom.txt", 'w', encoding='utf-8') as file:
        print(str + " = 0", file=file)
