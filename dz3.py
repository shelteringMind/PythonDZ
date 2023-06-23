# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:*
#5
    #1 2 3 4 5
#3
    #-> 1

#import collections
#import random

#print(f"Введите количество чисел в списке:", end = ' ')
#N = int(input())
#print(f"Введите значение числа, которое необходимо найти в списке:", end = ' ')
#X = int(input())

#sp = [random.randint(1, 100) for i in range(N)]
#num_count = collections.Counter(sp)
#print(*sp, sep=' ')
#print(f"{X} -> {num_count[X]}")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:*
#5
    #1 2 3 4 5
#6
    #-> 5
    
#import random
#import time
        
#print(f"Введите количество чисел в списке:", end = ' ')
#N = int(input())
#print(f"Введите значение элемента,\nсамый близкий по величине элемент к которому требуется найти:", end = ' ')
#X = int(input())

#sp = [random.randint(1, 100) for i in range(N)]

#start_set = time.time_ns()        
#sp_new =list(set(sp))        
#val_comp = abs(X-sp_new[0])
#val_save = sp_new[0]        
#for val in sp_new:
    #if abs(val-X) < val_comp:
        #val_save = val
        #val_comp = abs(X-val)       
#end_set = time.time_ns() - start_set

#start_list = time.time_ns()
#val_comp = abs(X-sp[0])
#val_save = sp[0]
#for val in sp:
    #if abs(val-X) < val_comp:
        #val_save = val
        #val_comp = abs(X-val)
#end_list = time.time_ns() - start_list

#print(*sp, f"-> {val_save}", sep=' ')

#try:
    #speed_diff = end_list/end_set
#except ZeroDivisionError:
    #speed_diff = 1
    
#print(f"Алгоритм с использованием множества в {speed_diff:.{2}f} раз быстрее")


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

#*Пример:*
#ноутбук
#12

#one_cost = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
#two_cost = dict.fromkeys(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2)
#three_cost = dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
#four_cost = dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы' ], 4)
#five_cost = dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч' ], 5)
#eight_cost = dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8)
#ten_cost  = dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10)
#merged_dict = one_cost | two_cost | three_cost | four_cost | five_cost | eight_cost | ten_cost

#print(f"Введите слово:", end = ' ')
#str = input()
#str_print = str

#str = str.strip()
#str = str.upper()
#str_list = list(str)
#cost_counter = 0;

#for iter, letter in enumerate(str_list): 
    #cost_counter += merged_dict.get(letter, 0)
    
#print(f"{str_print} стоит {cost_counter}")