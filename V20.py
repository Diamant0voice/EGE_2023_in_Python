# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # wzxy
def columns(w, x, z, y):
    return not(w <= x) or ((not z) <= (not y)) or z


for holes in product((0, 1), repeat=6):
    table = [(holes[0], 0, 1, 1), (1, holes[1], 1, holes[2]), (holes[3], holes[4], holes[5], 1)]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('wxzy'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 

print('№6:')  # Ответ: 64
screensize(4000, 4000)
ht()
speed(500)  # Без заполнения выходит дольше, но мы не ждём
color("orange")
pensize(0.1)
tracer(0)
scale = 50

lt(90)
rt(300)
for rep in range(6):  # Звездулька - типа подарка за труды?) Вот спасибо...
    fd(5 * scale)  
    rt(120)
    fd(5 * scale)
    rt(330 * scale)
up()

for X in range(-50, 50):
    for Y in range(-50, 50):
        goto(X * scale, Y * scale)  # Равномерно скачем на поле по сетке
        dot(3, "green")  # И оставляем там видимые следы, чтобы вручную посчитать

update()
exitonclick()
# По ЗАДУМКЕ, так решаться должно было всё, но по факту, данный способ актуален лишь пару раз, да и не стоит он затрачиваемых усилий.

print("№10:")  # 2
kr = 0
with open('C:/for типовые 20 вариантов/10/Отцы и дети.txt', 'r') as book:
    for word in book:
        if "Россия" in word:
            kr += 1
print(kr)

print("№8:")  # 

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 50
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return (8 * n + F(n - 3)) // 9
    elif n > 2 and n % 2 != 0:
        return (4 * n + F(n - 1) + F(n - 2)) // 7
print(F(52))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 28
func23 = lambda start, end, exc: func23(start + 1, end, exc) + func23(start * 2, end, exc) if start < end and start != exc else start == end
print(func23(2, 10, 19) * func23(10, 26, 19))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
