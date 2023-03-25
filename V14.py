# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # xwyz
def columns(w, y, z, x):
    return ((w == (not y)) or (w == (not z))) and x and (y <= z)


for holes in product((0, 1), repeat=7):
    table = [(holes[0], 1 ,0, 1), (holes[1], 1, holes[2], 0), (holes[3], 0, holes[4], 1), (holes[5], holes[6], 1, 1)]; F = [1, 1, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('wyzx'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№6:")  # 125
screensize(6000, 6000)
speed(10)
ht()
pensize(0.1)
tracer(0)
color('gold', 'red')
scale = 35
counter6 = 0

begin_fill()
lt(90)
rt(60)
for rep in range(3):
    fd(10 * scale)
    rt(120)
    fd(5 * scale)
    rt(240)
rt(120)
fd(3 * scale)
rt(90)
fd(15*sqrt(3) * scale)
rt(90)
fd(3 * scale)
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

print("№14:")  # 101340
for X in '0123456789ABCDEFG':
    operand = int(f'135{X}9', 17) + int(f'9{X}531', 17)
    print(operand // 9) if operand % 9 == 0 else None # В ответ уйдёт последнее, наибольшее

print("№16:")  # 3216449665440
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return n * (n - 1) * F(n - 1)
print(int(F(123) / F(120)))

print("№23:")  # 30
func23 = lambda start, end: func23(start + 2, end) + func23(start * 2, end) + func23(start * 3, end) if start < end else start == end
print(func23(2, 6) * func23(6, 28))
