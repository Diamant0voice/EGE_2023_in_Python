# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # zxwy
def columns(z, w, x, y):
    return not(z <= w) or x or (not y)

for holes in product([0, 1], repeat=5):
    table = [(1, 0, holes[0], holes[1]), (0, 0, 0, holes[2]), (0, 0, holes[3], holes[4])]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('zwxy'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 

print("№6:")  # 120
screensize(5000, 5000)  # Да, параметры окна можно задавать любые
ht()
speed(10)
color("pink", "red")
scale = 85
counter6 = 0
pensize(0.1)
tracer(0)

begin_fill()
lt(90)
for rep in range(2):
    rt(120)
    fd(12 * scale)
    rt(60)
    fd(12 * scale)
end_fill()
up()

canvas = getcanvas()
for X in range(-150 * scale, 150 * scale, scale):
    for Y in range(-150 * scale, 150 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 6142
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 3 * F(n - 1)
    elif n > 1 and n % 2 != 0:
        return 2 + 2 * F(n - 2)
print(F(23))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 171
func23 = lambda start, end: func23(start - 1, end) + func23(start // 2, end) if start > end else start == end
print(func23(31, 12) * func23(12, 2))

print("№24:")  # 

print("№25:")  # 
