#Задача 30:  Заполните массив элементами арифметической прогрессии.
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки

#firstElement = int(input("Введите первый элемент арифметической прогрессии: "))

#difference = int(input("Введите разность арифметической прогрессии: "))

#amountElements = int(input("Введите количество элементов: "))

#searchMember = [firstElement + (element - 1) * difference for element in range(1, amountElements + 1)]
#for searchMem in searchMember:
    #print(searchMem)
    
#Задача 32: Определить индексы элементов массива (списка),
#значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

amountElements = int(input("Введите количество элементов: "))

listElements = [random.randint(1, 100) for val in range(amountElements)]

minElement = int(input("Введите минимальный элемент: "))

maxElement = int(input("Введите максимальный элемент: "))

listIndex = [index for index, val in enumerate(listElements) if val >= minElement and val <= maxElement]

for listEl in listElements:
    print(f"{listEl}", end =" ")

print("\n")

for listId in listIndex:
    print(f"{listId}", end =" ")