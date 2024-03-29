# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
#
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом,
# и вывести получившуюся статистику.
#
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
# число его повторений (без учёта регистра) в формате "слово количество".
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿должно выводиться только один раз.

s = list(input().lower().split())
d = dict()
for i in range(len(s)):
    if s[i] in d.keys():
        d[s[i]] += 1
    else:
        d[s[i]] = 1
for i in d:
    print(i, d[i])
