# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log
from itertools import product, permutations
from functools import lru_cache
from string import ascii_uppercase

print("№2:")  # xwyz
def columns(x, y, z, w):
    return not((x == y) or (x == z)) or w or (not(y <= z))

for holes in product({0, 1}, repeat=7):  # да. скобы не важны, главное - не строкой
    table = [(0, holes[0], 0, 0), (1, holes[1], holes[2], 1), (0, holes[3], holes[4], holes[5]), (1, holes[6], 1, 1)]; F = [0, 0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xyzw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№6:")  # 391
screensize(10000, 10000)
speed(10)
shape('turtle')
tracer(0)
color("white", "red")
pensize(0.1)
scale = 50
counter6 = 0

begin_fill()
lt(90)
rt(180)
fd(2 * scale)
rt(90)
fd(80 * scale)
rt(90)
fd(2 * scale)
for rep in range(8):  # Алгоритм исполнения "дуг". Правильный. Как делал г. Крылов, остаётся лишь гадать...
    circle(-5 * scale, 180)  # "-" для вращения по часовой
    rt(180)
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

print("№14:")  # 47594
print(ascii_uppercase)  # Забыли алфавитный порядок латиницы? Выведите её на экран!
for X in "0123456789ABCDEFGHIJK":
    for Y in "0123456789ABCDEFGHIJK":
        operand = int(f'12{Y}{X}9', 21) + int(f'36{Y}99', 21)
        print(operand // 18) if operand % 18 == 0 and Y == "5" else None  # Y - строковый тип, и вся прога - о строках, помним

print("№16:")  # 1450
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return 2 + F(n - 1)
    elif n > 2 and n % 2 != 0:
        return 3 * n + F(n - 2)
print(F(43))

print("№23:")  # 58
func23 = lambda start, end: func23(start + 3, end) + func23(start + 4, end) + func23(start * 3, end) if start < end else start == end
print(func23(1, 7) * func23(7, 30))
