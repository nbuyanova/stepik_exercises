# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
# и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Порядок вывода команд произвольный.

GAMES = 0
WINS = 1
DRAW = 2
LOST = 3
SCORE = 4
n = int(input())
matches = [[''] * 4] * n
for i in range(n):
    matches[i] = input().split(';')
results = {}
for i in range(n):
    (team_1, _, team_2, _) = matches[i]
    results[team_1] = [0] * 5
    results[team_2] = [0] * 5
for i in range(n):
    (team_1, teamgoal_1, team_2, teamgoal_2) = matches[i]
    results[team_1][GAMES] += 1
    results[team_2][GAMES] += 1
    if teamgoal_1 > teamgoal_2:
        results[team_1][WINS] += 1
        results[team_1][SCORE] += 3
        results[team_2][LOST] += 1
    elif teamgoal_1 == teamgoal_2:
        results[team_1][DRAW] += 1
        results[team_1][SCORE] += 1
        results[team_2][DRAW] += 1
        results[team_2][SCORE] += 1
    else:
        results[team_1][LOST] += 1
        results[team_2][WINS] += 1
        results[team_2][SCORE] += 3
for i in results:
    print(i, ':', ' '.join([str(v) for v in results[i]]), sep='')
