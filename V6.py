# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # wyzx
def columns(z, y, x, w):
    return ((z <= y) <= x) or (not w)

for holes in product([0, 1], repeat=7):
    table = [(holes[0], 0, holes[1], 0), (holes[2], 1, 0, holes[3]), (holes[4], holes[5], 1, holes[6])]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('zyxw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 

print("№6:")  # Ответ: 6488, в сборнике опечатка, проверено Александром Павловым
screensize(10000, 10000)
tracer(0)
ht()
speed(10)
pensize(0.1)
color("brown", "red")
scale = 100
counter6 = 0

begin_fill()
lt(90)
for rep in range(3):
    fd(123 * scale)
    rt(120)
end_fill()
up()

canvas = getcanvas()
for X in range(-300 * scale, 300 * scale, scale):
    for Y in range(-300 * scale, 300 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 968551148
@lru_cache(None)
def F(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 != 0:
        return 4 * n + F(n - 1) - F(2)
    elif n > 1 and n % 2 == 0:
        return 3 * F(n - 1)
print(F(35))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 639
func23 = lambda start, end: func23(start + 2, end) + func23(start + 7, end) if start < end else start == end
print(func23(7, 51))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
