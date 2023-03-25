# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # xzyw
def columns(x, y, z, w):
    return (x <= y) and z and (not w)

for holes in product([0, 1], repeat=5):
    table = [(0, holes[0], 0, 0), (1, holes[1], holes[2], 0), (0, holes[3], holes[4], 0)]; F = [1, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('xyzw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations)))for variations in table] == F else None

print("№6:")  # 101
screensize(4000, 4000)
tracer(0)
ht()
speed(10)
pensize(0.1)
color("beige", "red")
scale = 45
counter6 = 0

begin_fill()
lt(90)
rt(180)
fd(2 * scale)
rt(90)
fd(30 * scale)
rt(90)
fd(2 * scale)
rt(30)
for rep in range(6):
    fd(5 * scale)
    rt(120)
    fd(5 * scale)
    rt(240)
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

print("№16:")  # 78731
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + F(n - 1)
    elif n > 1 and n % 2 != 0:
        return 2 * F(n - 1) + F(n - 2)
print(F(20))

print("№23:")  # 72
func23 = lambda start, end: func23(start - 1, end) + func23(start // 3, end) if start > end else start == end
print(func23(33, 9) * func23(9, 1))
