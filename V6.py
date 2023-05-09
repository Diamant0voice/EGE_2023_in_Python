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

print("№5:")  # 753
for N in range(100, 1000):
    dig1 = N // 100; dig2 = N // 10 % 10; dig3 = N % 10
    sum1 = dig1 ** 2 + dig2 ** 2; sum2 = dig2 ** 2 + dig3 ** 2
    R = str(max(sum1, sum2)) + str(min(sum1, sum2))
    print(N) if R == '7434' else None

print("№6:")  # Ответ: 6488, в сборнике опечатка (проверено Александром Павловым)
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

print("№8:")  # 376
counter = 0
for let1, let2, let3, let4 in product('АВОПР', repeat=4):
    counter += 1
    word = let1 + let2 + let3 + let4
    if word[0] == 'П':
        break
print(counter, word)

print("№12:")  # 5
s = '1' * 2022
while '11' in s or '555' in s:
    s = s.replace('11', '555', 1) if '11' in s else s.replace('555', '5', 1)
print(s)

print("№14:")  # 89
cr = 4**2022 - 2 * 4**1111 + 16**600 + 192
counter = 0
while cr > 0:
    if cr % 4 == 3:
        counter += 1
    cr //= 4
print(counter)

print("№15:")  # 26
def logic(x):
    return not(((x in B) or (x in C)) <= (x in A))

A = list()
B = [points for points in range(30, 41 + 1)]
C = [points for points in range(50, 56 + 1)]

for points in range(1, 100):
    if logic(points):
        A.append(points)
print(A[-1] - A[0])

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

print("№17:")  # 41 -9786
with open("C:/for типовые 20 вариантов/17/17var06.txt") as file17:
    numbers = [int(index) for index in file17]
    squares = [index ** 2 for index in range(1, 100 + 1)]
    counter, min_sum = 0, float('inf')
    for elem1, elem2 in zip(numbers, numbers[1:]):
        if elem1 in squares or elem2 in squares:
            counter += 1
            min_sum = min(min_sum, elem1 + elem2)
print(counter, min_sum)            

print("№19:")  # 88
def heap19(rocks, position):
    if rocks >= 177 or position > 3:
        return position == 3
    elif position % 2 == 0:
        return heap19(rocks + 1, position + 1) or heap19(rocks * 2, position + 1)
    else:
        return heap19(rocks + 1, position + 1) and heap19(rocks * 2, position + 1)

for answer19 in range(1, 176 + 1):
    print(answer19) if heap19(answer19, 1) else None

print("№20:")  # 44 87
def heap20(rocks, position):
    if rocks >= 177 or position > 4:
        return position == 4
    elif position % 2 != 0:
        return heap20(rocks + 1, position + 1) or heap20(rocks * 2, position + 1)
    else:
        return heap20(rocks + 1, position + 1) and heap20(rocks * 2, position + 1)

for answer20 in range(1, 176 + 1):
    print(answer20) if heap20(answer20, 1) else None

print("№21:")  # 86
def heap21(rocks, position):
    if rocks >= 177 or position > 5:
        return position == 3 or position == 5
    elif position % 2 == 0:
        return heap21(rocks + 1, position + 1) or heap21(rocks * 2, position + 1)
    else:
        return heap21(rocks + 1, position + 1) and heap21(rocks * 2, position + 1)

for answer21 in range(1, 176 + 1):
    print(answer21) if heap21(answer21, 1) else None

print("№23:")  # 639
func23 = lambda start, end: func23(start + 2, end) + func23(start + 7, end) if start < end else start == end
print(func23(7, 51))

print("№24:")  # 7684
with open('C:/for типовые 20 вариантов/24/24var05-08.txt') as file24:
    f = file24.read().strip()
    cur_len = max_len = 0
    for index in range(len(f) - 2):
        if f[index] + f[index - 1] + f[index - 2] == '000':
            cur_len = 2
        else:
            cur_len += 1
            max_len = max(max_len, cur_len)
print(max_len)

print("№25:")  # Ответ верный
def divs(number):
    s = set()
    for divider in range(2, int(number ** 0.5) + 1):
         if number % divider == 0:
             s.add(divider); s.add(number // divider)
    return sorted(s)

for number in range(860_000, 870_001):
    d = divs(number)
    if len(d) > 0:
        M = max(d) - min(d)
        print(number, M) if M % 100 == 30 else None

print("№26:")  # 

print("№27:")  #
