#Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

#print("Введите число: ")
#num_str = input()
#len_num = len(num_str)
#sum = 0
#line = ""
#for i in range(0, len_num):
    #temp = int(num_str[i])
    #sum += temp
    #if i < len_num - 1:
        #line += num_str[i] + " + "
    #else:
        #line += num_str[i]
#print(f"{num_str} -> {sum} ({line})")
    
#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#*Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
    #60 -> 10  40  10
    
#print("Введите количество журавликов, сделанных детьми: ")
#s = int(input())
#if (s >= 0) and (s % 6 == 0):
    #kat = 2 * s / 3
    #pet = (s - kat) / 2
    #ser = pet
    #print(f"{s} -> {int(pet)} {int(kat)} {int(ser)}")
#else:
    #print("Задача не имеет решения.\nВведите другое число журавликов!")

#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no

print("Введите номер билета: ")
num = input()
sum1 = 0
sum2 = 0
if int(len(num)) % 2 == 0:
    for i in range(0, int(len(num) / 2)):
        sum1 += int(num[i])
        sum2 += int(num[len(num) - i - 1])
    if sum1 == sum2:
        print(f"{num} -> yes")
    else:
        print(f"{num} -> no")  
else:
    print("Нельзя определить счастливый этот билет или нет...")

#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no

