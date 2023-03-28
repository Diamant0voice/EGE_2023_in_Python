# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

import math
from turtle import *
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # ywzx
def columns(y, z, w, x):
    return not(y <= (not(z <= w))) and ((not z) <= ((not w) == x))

for holes in product([0, 1], repeat=5):
    table = [(1, holes[0], 1, 1), (holes[1], holes[2], 0, 0), (holes[3], 0, 0, holes[4])]; F = [0, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('yzwx'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variables))) for variables in table] == F else None

print("№5:")  # 12
for N in range(1, 300):
    B = bin(N)[2:]
    if len(B) % 2 == 0:
        B = B[:len(B) // 2] + '1' + B[len(B) // 2:]  # Не совсем логично, но пихаем в середину 1
    R = int(B, 2)
    if R >= 26:
        print(N, "а само число такое", R)
        break

print("№6:")  # 1200
'''screensize(10000, 10000)
tracer(0)
hideturtle()
speed(10)
pensize(0.1)
color("black", "red")
scale = 100
counter6 = 0

up()
left(90)
forward(100 * scale)
right(90)
forward(100 * scale)
right(30)
down()
begin_fill()
for repeat in range(2):
    forward(30 * scale)
    right(90)
    forward(40 * scale)
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
exitonclick()'''

print("№8")  #
counter = 0
for let1, let2, let3, let4, let5, let6 in product("КНОРСЯ", repeat=6):
    word = let1 + let2 + let3 + let4 + let5 + let6
    counter += 1  # Здесь мы просто нумеруем слова, счётчик не функциональный
    if word.count('К') <= 3 and word.count('Я') == 2:
        print(counter, word)
        break

print("№16:")  # 887040
@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 != 0:
        return F(n - 1) + F(n - 2)
    elif n > 2 and n > 2 and n % 2 == 0:
        return sum(F(i) for i in range(1, n))  # Преобразуем сигму по смыслу, ничего особенного
print(F(24))

print("№23:")  # 1620
func23 = lambda start, end, exception: func23(start - 1, end, exception) + func23(start // 2, end, exception) if start > end and start != exception else start == end
print(func23(50, 20, 10) * func23(20, 1, 10))  # Ради одного "не равно" буквами сорим, но что поделать

print("№24:")  # 55
with open('C:/for типовые 20 вариантов/24/24var03.txt') as file24:
    f = file24.read().split('AB')
    counterMin = float('inf')
    for index in range(len(f)):
        correct_string = ''.join(f[index:index + 21])
        counterMin = min(counterMin, len(correct_string))  # чота не 55, пофиксить
    print(counterMin + 21 + 2)
