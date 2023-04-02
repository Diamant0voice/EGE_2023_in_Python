# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # ywzx
def columns(w, x, y, z):
    return not((w <= (not(x <= y)))) and ((not x) <= ((not y) == z))

for holes in product([0, 1], repeat=5):
    tables = [(holes[0], 1, 1, 1), (holes[1], holes[2], 0, 0), (0, holes[3], holes[4], 0)]; F = [0, 1, 1]
    if len(tables) == len(set(tables)):
        for answer2 in permutations('wxyz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in tables] == F else None

print("№5:")  # 
for N in range(1, 100):
    B = bin(N)[2:]
    if len(B) % 2 == 0:
        B = B[:len(B) // 2] + '1' + B[len(B) // 2:]
    R = int(B, 2)
    print(N) if R <= 26 else None


print("№6:")  # 588
screensize(10000, 10000)
speed(10)
hideturtle()
tracer(0)
pensize(0.1)
color("blue", "red")
scale = 100
counter6 = 0

up()
left(90)
forward(100 * scale)
right(90)
forward(100 * scale)
right(45)
down()
begin_fill()
for repeat in range(2):
    forward(20 * scale)
    right(90)
    forward(30 * scale)
    right(90)
end_fill()
up()

canvas = getcanvas()
for X in range(-250 * scale, 250 * scale, scale):
    for Y in range(-250 * scale, 250 * scale, scale):
        scanner = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scanner) == 1 and scanner[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№16:")  # 41518080
@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 != 0:
        return F(n - 1) - F(n - 2)
    elif n > 2 and n % 2 == 0:
        return sum(F(i) for i in range(1, n))
print(F(39))

print("№23:")  # 1760
func23 = lambda start, end, exc: func23(start - 1, end, exc) + func23(start // 2, end, exc) if start > end and start != exc else start == end
print(func23(60, 20, 4) * func23(20, 1, 4))

print("№24:")  # 10007
with open('C:/for типовые 20 вариантов/24/24var04.txt') as file24:
    f = file24.read().split('AB')
    counterMax = 0
    for index in range(len(f)):
        correct_string = ''.join(f[index:index + 22])
        counterMax = max(counterMax, len(correct_string))
    print(counterMax + 22 * 2)
