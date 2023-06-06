#Задача 30:  Заполните массив элементами арифметической прогрессии.
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки

firstElement = int(input("Введите первый элемент арифметической прогрессии: "))

difference = int(input("Введите разность арифметической прогрессии: "))

amountElements = int(input("Введите количество элементов: "))

searchMember = [firstElement + (element - 1) * difference for element in range(1, amountElements + 1)]
for searchMem in searchMember:
    print(searchMem)