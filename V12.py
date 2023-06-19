# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # wxyz
def columns(z, x, w, y):
    return (z <= x) and (not w) and y


for holes in product([0, 1], repeat=5):
    table = [(0, 0, holes[0], 0), (0, 0, holes[1], holes[2]), (0, 1, holes[3], holes[4])]; F = [1, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('zxwy'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variables))) for variables in table] == F else None

print("№5:")  # 

print("№6:")  # Ответ: 318, в сборнике опечатка. Размером с задание.
screensize(7000, 7000)
speed(10)
ht()
pensize(0.1)
tracer(0)
color("grey", "red")
scale = 150
counter6 = 0

begin_fill()
lt(90)
rt(10)
fd(4 * scale)
rt(90)
fd(48 * scale)
rt(90)
fd(4 * scale)
rt(30)
for rep in range(8):
    fd(6 * scale)
    rt(120)
    fd(6 * scale)
    rt(240)
end_fill()
up()

canvas = getcanvas()
for X in range(-100 * scale, 450 * scale, scale):
    for Y in range(-100 * scale, 450 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 
counter = 0
for digit in product('01234', repeat=3):
    number = ''.join(digit)
    counter += 1 if number[0] != '0' and number[0] >= number[1] >= number[2] else 0
print(counter)    

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 49197
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + F(n - 1)
    elif n > 1 and n % 2 != 0:
        return F(n - 1) + 2 * F(n - 2)
print(F(19))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 54
func23 = lambda start, end: func23(start - 1, end) + func23(start // 3, end) if start > end else start == end
print(func23(37, 10) * func23(10, 2))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
