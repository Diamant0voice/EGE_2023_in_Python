# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from sys import setrecursionlimit

print("№2:")  # xywz
def columns(x, y, w, z):
    return not(x <= y) or ((not w) <= (not z)) or w


for holes in product((0, 1), repeat=6):
    table = [(holes[0], 1, 0, 1), (1, 1, holes[1], holes[2]), (holes[3], holes[4], holes[5], 1)]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xywz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  #

print("№6:")  # 28
screensize(4000, 4000)
shape("turtle")
speed(10)
color("blue", "red")
tracer(0)
scale = 40
counter6 = 0
pensize(0.1)
title('Крылов намудрил')  # Опционально)))

begin_fill()  # Судя по предлагаемому ответу, имелось в виду вот это изображение. Как иметь смещение больше радиуса - вопрос открыт.
lt(90)
lt(180)
circle(-4 * scale, 180)
rt(90)
circle(-4 * scale, 180)
rt(90)
circle(-4 * scale, 180)
rt(90)
circle(-4 * scale, 180)
end_fill()
up()

canvas = getcanvas()
for X in range(-250 * scale, 250 * scale, scale):
    for Y in range(-250 * scale, 250 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 16345854
setrecursionlimit(1_000_000) # Иной способ обойти лимит рекурсии
def F(n):  # ВАЖНО: При таком методе решения кэшировать наши BigData нельзя, лично перегрузим память
    if n == 1:
        return 1
    elif n > 1:
        return n ** 2 + F(n - 1)
print(F(2023) - F(2019))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 24
func23 = lambda start, end: func23(start + 1, end) + func23(start + 3, end) + func23(start * 2, end) if start < end else start == end
print(func23(3, 8) * func23(8, 11) * func23(11, 14))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
