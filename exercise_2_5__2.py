# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента
# этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей
# считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список
# "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
#
# Если на вход пришло только одно число, надо вывести его же.
#
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

a = input().split()
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        if i < len(a) - 1:
            print((int(a[i - 1]) + int(a[i + 1])), end=" ")
        else:
            print((int(a[i - 1]) + int(a[0])), end=" ")
