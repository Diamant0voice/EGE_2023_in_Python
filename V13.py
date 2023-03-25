# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # xzyw 
def columns(x, y, z, w):
    return ((x == (not y)) or (x == (not z))) and w and (y <= z)


for holes in product([0, 1], repeat=7):
    table = [(0, 1, holes[0], holes[1]), (0, holes[2], 0, holes[3]), (holes[4], 0, 0, holes[5]), (1, 1, 0, holes[6])]; F = [1, 1, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('xyzw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations)))for variations in table] == F else None

print("№6:")  # 91
screensize(10000, 10000)
speed(15)
ht()
color("blue", "red")
tracer(0)
pensize(0.1)
scale = 100
counter6 = 0

begin_fill()
lt(90)
rt(60)
for rep in range(4):
    fd(8 * scale)
    rt(120)
    fd(4 * scale)
    rt(240)
rt(120)
fd(2 * scale)
rt(90)
fd(16*sqrt(3) * scale)  # Квадратный корень. Или 16 * 3**0.5
rt(90)
fd(2 * scale)
end_fill()
up()

canvas = getcanvas()
for X in range(-600 * scale, 600 * scale, scale):
    for Y in range(-600 * scale, 600 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№14:")  # 31027
for X in "0123456789ABCDE":  # Цифр всего 10, дальше ЗАГЛАВНЫЕ буквы латиницы
    operand = int(f'135{X}7', 15) + int(f'7{X}531', 15)  # перебираем X из символов 15 сс, вставляя в переводимые в 10 сс операнды
    print(operand // 14) if operand % 14 == 0 else None  # И выбираем первое, break тут не в тему

print("№16:")  # 88120680
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * F(n - 1)
print(int(F(446) / F(443)))

print("№23:")  # 40
func23 = lambda start, end: func23(start + 2, end) + func23(start * 2, end) + func23(start * 3, end) if start < end else start == end
print(func23(1, 6) * func23(6, 24))
