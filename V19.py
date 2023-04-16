# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # zwyx
def columns(y, x, w, z):
    return not(y <= x) or (y == w) or z


for holes in product((0, 1), repeat=6):
    table = [(holes[0], 1, holes[1], 1), (0, holes[2], 1, 1), (holes[3], 1, holes[4], holes[5])]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('yxwz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 

print("№6:")  # 269
screensize(5000, 5000)
ht()
tracer(0)
speed(10)
color("white", "red")
scale = 40
counter6 = 0

begin_fill()
lt(90)
rt(300)
for rep in range(4):  # И всё вновь работает
    fd(10 * scale)
    rt(120)
    fd(10 * scale)
    rt(330)
end_fill()
up()

canvas = getcanvas()
for X in range(-200 * scale, 200 * scale, scale):
    for Y in range(-200 * scale, 200 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 43
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return (7 * n + F(n - 3)) // 9  # Простенькая реализация взятия целой части числа
    elif n > 2 and n % 2 != 0:
        return (5 * n + F(n - 1) + F(n - 2)) // 7
print(F(50))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 12
func23 = lambda start, end, exc: func23(start + 1, end, exc) + func23(start * 2, end, exc) if start < end and start != exc else start == end
print(func23(3, 12, 23) * func23(12, 27, 23))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
