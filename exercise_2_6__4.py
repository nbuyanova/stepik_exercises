# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
# заканчивающихся строкой, содержащей только строку "end" (без кавычек).
#
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
# первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
# с противоположной стороны матрицы.
#
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
n = len(a)
m = len(a[0])
b = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i < n - 1 and j < m - 1:
            b[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1]
            print(b[i][j], end=' ')
        elif i >= n - 1 and j < m - 1:
            b[i][j] = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j + 1]
            print(b[i][j], end=' ')
        elif i < n - 1 and j >= m - 1:
            b[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0]
            print(b[i][j], end=' ')
        else:
            b[i][j] = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][0]
            print(b[i][j], end=' ')
    print()