# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # zyxw
def columns(x, y, w, z):
    return ((x <= y) <= w) or (z <= (y and w))

for holes in product([0, 1], repeat=7):
    table = [(1, 0, holes[0], holes[1]), (holes[2], holes[3], 1, holes[4]), (holes[5], 1, 0, holes[6])]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('xywz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 

print("№6:")  # 922
screensize(10000, 10000)
ht()
speed(10)
pensize(0.1)
tracer(0)
scale = 75
counter6 = 0
color("yellow", "red")

begin_fill()
lt(90)
for rep in range(6):
    fd(19 * scale)
    rt(60)
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
print(len([digits for digits in product('01234567', repeat=5) if digits[0] != '0' and digits.count('4') == 2
   and all('4' + fail not in (number := ''.join(digits)) and fail + '4' not in number for fail in '1357')]))

print("№12:")  # 1
string = '1' * 65
while '11111' in string or '15' in string:
    string = string.replace('11111', '15', 1) if '11111' in string else string.replace('15', '1', 1)
print(string)


print("№14:")  # 

print("№15:")  # 

print("№16:")  # 13441735782
def F(n):
    if n <= 1:
        return 2
    elif n > 1 and n % 2 != 0:
        return 1 + F(n - 1) * F(n - 2) - F(n - 1) - F(n - 2)
    elif n > 1 and n % 2 == 0:
        return 2 * F(n - 1)
print(F(12))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 4085
func23 = lambda start, end: func23(start + 2, end) + func23(start + 10, end) if start < end else start == end
print(func23(7, 71))

print("№24:")  # 

print("№25:")  # 
