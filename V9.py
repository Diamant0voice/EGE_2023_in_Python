# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # zywx
def columns(x, y, z, w):
    return not(x <= y) or (not z) or w

for holes in product([0, 1], repeat=5):
    table = [(holes[0], holes[1], 0, 1), (holes[2], holes[3], 0, 0), (holes[4], 0, 0, 0)]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xyzw'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations)))for variations in table] == F else None

print("№5:")  # 66
for N in range(1, 35):
    N -= N % 4
    N = bin(N)[2:]
    N += str(N.count('1') % 2)
    N += str(N.count('1') % 2)
    if int(N, 2) > 60:
        print(int(N, 2)) 
        break

print("№6:")  # 750
screensize(10000, 10000)
ht()
tracer(0)
speed(10)
color("indigo", "red")
pensize(0.1)
scale = 80
counter6 = 0

begin_fill()
lt(90)
rt(30)
for rep in range(2):
    fd(30 * scale)
    rt(60)
    fd(30 * scale)
    rt(120)
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

print("№12:")  # 22
string = '1' * 70
while '1111' in string or '2222' in string:
    string = string.replace('1111', '22', 1) if '1111' in string else string.replace('2222', '11', 1)
print(string)

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 9841
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 2 * F(n - 1)
    elif n > 1 and n % 2 != 0:
        return 1 + 3 * F(n - 2)
print(F(17))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 360
func23 = lambda start, end: func23(start - 1, end) + func23(start // 2, end) if start > end else start == end
print(func23(30, 10) * func23(10, 1))

print("№24:")  # 

print("№25:")  # 
