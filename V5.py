# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # wyxz
def columns(x, y, w, z):
    return not(((x <= y) <= w)) and z

for holes in product([0, 1], repeat=7):
    table = [(0, 0, holes[0], holes[1]), (holes[2], 1, 0, holes[3]), (holes[4], holes[5], 1, holes[6])]; F = [1, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('xywz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations)))for variations in table] == F else None

print("№5:")  # 946
for N in range(100, 1000):
    dig1 = N // 100; dig2 = N // 10 % 10; dig3 = N % 10  # Остатком отщепляем последнюю цифру, цельняком - первую
    sum1 = dig1**2 + dig2**2; sum2 = dig2**2 + dig3**2
    output = str(max(sum1, sum2)) + str(min(sum1, sum2))  # Соединяем части, а не просто складываем
    if output == '9752':
        print(N)  # Выбираем последнее

print("№6:")  # 5280
screensize(10000, 10000)
tracer(0)
pensize(0.1)
color("cyan", "red")
scale = 100
counter6 = 0
speed(10)
hideturtle()

begin_fill()
left(90)
for rep in range(3):
    fd(111 * scale)
    rt(120)
up()
end_fill()

canvas = getcanvas()
for X in range(-250 * scale, 250 * scale, scale):
    for Y in range(-250 * scale, 250 * scale, scale):
        scan = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scan) == 1 and scan[0] == 5 else 0

print(counter6)
update()
exitonclick()

print("№8:")  # 

print("№10:")  # 5
kr = 0  # ну а почему бы и нет?
with open('C:/for типовые 20 вариантов/10/Отцы и дети.txt', 'r') as book:
    for word in book:
        if "Деньги" in word or "деньги" in word:
            kr += 1
print(kr)

print("№12:")  # 

print("№14:")  # 

print("№15:")  # 

print("№16:")  # 2214271
@lru_cache(None)
def F(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 != 0:
        return 5 * n + F(n - 1) + F(2)
    elif n > 1 and n % 2 == 0:
        return 3 * F(n - 1)
print(F(23))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 639
func23 = lambda start, end: func23(start + 2, end) + func23(start + 7, end) if start < end else start == end
print(func23(5, 49))

print("№24:")  # 

print("№25:")  # 

print("№26:")  # 

print("№27:")  # 
