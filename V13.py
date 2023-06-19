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

print("№5:")  # 96
for N in range(1, 100):
    N = bin(N - N % 8 + N % 2)[2:]
    for rep in range(2):
        N += str((N.count('1') % 2))
    if int(N, 2) > 90:
        print(int(N, 2))
        break

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

print("№8:") # 882
counter = 0
for d1, d2, d3, d4 in product('01234567', repeat=4):
    number = d1 + d2 + d3 + d4
    counter += 1 if number[0] != '0' and \
                    ((d1 == d2 and d2 != d3 and d2 != d4 and d3 != d4) or
        (d2 == d3 and d1 != d3 and d1 != d4 and d3 != d4) or
         (d3 == d4 and d1 != d2 and d1 != d3 and d2 != d3)) else 0
print(counter)

print("№12:")  # 76
string = '1' + '5' * 25
while '15' in string or '1' in string:
    string = string.replace('15', '5551', 1) if '15' in string else string.replace('1', '5', 1)
print(string.count('5'))

print("№14:")  # 31027
for X in "0123456789ABCDE":  # Цифр всего 10, дальше ЗАГЛАВНЫЕ буквы латиницы
    operand = int(f'135{X}7', 15) + int(f'7{X}531', 15)  # перебираем X из символов 15 сс, вставляя в переводимые в 10 сс операнды
    print(operand // 14) if operand % 14 == 0 else None  # И выбираем первое, break тут не в тему

print("№15:")  # 15
def logic(x, y, A):
    return ((x >= A) or (y >= A) or (x * y <= 200))

for A in range(1, 100):
    if all(logic(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
           print(A)

print("№16:")  # 88120680
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * F(n - 1)
print(int(F(446) / F(443)))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 40
func23 = lambda start, end: func23(start + 2, end) + func23(start * 2, end) + func23(start * 3, end) if start < end else start == end
print(func23(1, 6) * func23(6, 24))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
