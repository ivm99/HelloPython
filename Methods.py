# Ввод списка пользователем

def Create_List_Of_Numbers(n):
    
    numbers: int = []
    i = 0
    
    while i < n:
        
        print(f'Введите {i}-е число: ', end="")
        numbers.append(input())
        i = i + 1 
    numbers = list(map(int, numbers))
    
    return numbers

