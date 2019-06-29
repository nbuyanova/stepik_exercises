# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы 𝐴 часов в сутки, но пересыпать тоже вредно
# и не стоит спать более 𝐵 часов. Сейчас Аня спит 𝐻 часов в сутки. Если режим сна Ани удовлетворяет
# рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее 𝐴 часов, выведите “Недосып”,
# если же более 𝐵 часов, то выведите “Пересып”.
# Получаемое число 𝐴 всегда меньше либо равно 𝐵.

A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print('Это нормально')
elif H < A:
    print('Недосып')
else:
    print('Пересып')