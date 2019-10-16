# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

import requests

with open('dataset_3378_3.txt') as f:
    r = requests.get(f.readline().strip())
s = r.text.split()
while s[0] != 'We':
    r_new = 'https://stepic.org/media/attachments/course67/3.6.3/' + s[0]
    r = requests.get(r_new)
    s = r.text.split()
print(r.text)
