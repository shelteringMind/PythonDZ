#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

#import random

#n = int(input("Введите количество чисел в первом списке: "))
#m = int(input("Введите количество чисел во втором списке: "))

#spn = [random.randint(-10, 100) for i in range(n)]
#spm = [random.randint(-10, 100) for i in range(m)]

#print(*spn, sep=' ')
#print(*spm, sep=' ')
#print(*list(sorted(set(spn + spm))), sep=' ')

#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
#Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
#находясь перед некоторым кустом заданной во входном файле грядки.
    
#import random

#def sumBerBush(arr, runner):
    #summaThree = 0
    #n = len(arr)
    #if n < 3:
        #summaThree = sum(arr)
    #else:
        #for iter in range(runner - 1, runner + 2):
            #if iter > n - 1:
                #iter = 0
            #elif iter < 0:
                #iter = n - 1
            #summaThree += arr[iter]
    #return summaThree   
    
#n = int(input("Введите количество кустов на грядке: "))    
#numBerries = [random.randint(1, 100) for i in range(n)]

#if n <= 3: qVar = 1
#else: qVar = n
    
#for iter in range(0, len(numBerries)):
    #print(f"{iter + 1} -> {numBerries[iter]}")
    
#sumThreeBush = [sumBerBush(numBerries, it) for it in range(qVar)]
#print(f"Максимум за один заход модуль может собрать {max(sumThreeBush)} ягод черники")