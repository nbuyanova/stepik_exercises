# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке, как показано в примере (здесь n = 5):
#
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
b = 1
n1 = 0
n2 = n
while b <= n * n:
    for i in range(n1, n2):
        a[n1][i] = b
        b += 1
    for i in range(n1 + 1, n2):
        a[i][n2 - 1] = b
        b += 1
    for i in range(n2 - 2, n1 - 1, -1):
        a[n2 - 1][i] = b
        b += 1
    for i in range(n2 - 2, n1, -1):
        a[i][n1] = b
        b += 1
    n1 += 1
    n2 -= 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
