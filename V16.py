# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log
from itertools import product, permutations
from functools import lru_cache
from string import ascii_uppercase


print("№2:")  # wyxz
def columns(x, y, w, z):
    return not((x == y) or (x == w)) or z or (not(y <= w))


for holes in product([0, 1], repeat=9):
    table = [(1, 0, 0, holes[0]), (holes[1], holes[2], holes[3], holes[4]), (1, 1, holes[5], holes[6]), (holes[7], 0, 1, holes[8])]; F = [0, 0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xywz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 

print("№6:")  # 250
screensize(4000, 4000)
speed(10)

tracer(0)
color("purple", "red")
pensize(0.1)
scale = 25
counter6 = 0

begin_fill()
lt(90)
rt(180)
fd(3 * scale)
rt(90)
fd(48 * scale)
rt(90)
fd(3 * scale)
for rep in range(6):
    circle(-4 * scale, 180)
    lt(180)
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

print("№14:")  # 187162
for X in "0123456789ABCDEFGHIJKLMNOP":
    for Y in "0123456789ABCDEFGHIJKLMNOP":
        operand = int(f'13{Y}{X}5', 26) + int(f'24{Y}13', 26)
        print(operand // 8) if operand % 8 == 0 and Y == '2' else None

print("№15:")  # 

print("№16:")  # 884
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return 3 + F(n - 1)
    elif n > 2 and n % 2 != 0:
        return 2 * n + F(n - 2)
print(F(42))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 16
func23 = lambda start, end: func23(start + 5, end) + func23(start + 4, end) + func23(start * 3, end) if start < end else start == end
print(func23(2, 6) * func23(6, 30))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
