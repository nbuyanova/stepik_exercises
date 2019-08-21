# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
# записана следующая информация:
#
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#
# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю
# оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
#
# Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому
# языку по всем абитуриентам.
#
# В качестве ответа на задание прикрепите полученный файл со средними оценками.
#
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']

s_list = list()
with open('dataset_3363_4.txt') as f:
    for line in f:
        s_list.append(line.strip().split(';'))
sumMiddle = 0
ouf = open('dataresult_3363_4.txt', 'w')
for el in s_list:
    sumMiddle = (int(el[1]) + int(el[2]) + int(el[3])) / 3
    ouf.write(str(sumMiddle) + '\n')
sumMaths, sumPhysics, sumRussian = 0, 0, 0
for el in s_list:
    sumMaths += int(el[1])
    sumPhysics += int(el[2])
    sumRussian += int(el[3])
sumMaths /= len(s_list)
sumPhysics /= len(s_list)
sumRussian /= len(s_list)
ouf.write(str(sumMaths) + ' ')
ouf.write(str(sumPhysics) + ' ')
ouf.write(str(sumRussian) + '\n')
ouf.close()
