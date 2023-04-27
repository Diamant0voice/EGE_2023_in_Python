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

print("№5:")  # 26
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

print("№8:")  # 1599
counter = 0
for let1, let2, let3, let4, let5, let6 in product('АЗЛОПЬ', repeat=6):
    counter += 1
    word = let1 + let2 + let3 + let4 + let5 + let6
    if word.count('Ь') <= 1 and word.count('А') == 1 and word.count('З') <= 2:
        print(counter, word)
        break

print("№12:")  # 1121211
string = '22' + '1' * 2023
while '2111' in string or '1112' in string:
    string = string.replace('111', '1', 1)
    string = string.replace('21', '12', 1) if '21' in string else string.replace('12', '1', 1)
print(string)

print("№14:")  # 1236
cringe = 1331**650 - 55 * 121**610 + 77 * 11 **510 - 3 * 11**100 - 221
counter = 0
while cringe > 0:
    counter += 1 if cringe % 11 == 10 else 0  # Разводка десятичным эквивалентом буквы относительно её положения в 16-ричной с.с.
    cringe //= 11
print(counter)

print("№15:")  # 6
def treug(n, m, k):
    return n + m > k and n + k > m and m + k > n


for A in range(1, 1000):
    while True:
        if all(not((treug(x, 12, 20) == (max(x,5) <= 28)) and treug(x, A, 3)) for x in range(1, 1000)):
               print(A)
        break
    A -= 1

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

print("№17:")  # 2936 75058186
counter, trio_min = 0, float('inf')
with open('C:/for типовые 20 вариантов/17/17var04.txt') as file17:
    sequence = [int(num) for num in file17]
    maximum = max(number for number in sequence)
    for elem1, elem2, elem3 in zip(sequence, sequence[1:], sequence[2:]):
        last_digits = str(elem1 % 10) + str(elem2 % 10) + str(elem3 % 10)
        if last_digits.count('3') == 0 and elem1**2 + elem2**2 + elem3**2 > maximum:
            counter += 1
            trio_min = min(trio_min, elem1**2 + elem2**2 + elem3**2)
print(counter, trio_min)

print("№19:")  # 80
def heap19(rocks, position):
    if rocks >= 161 or position > 3:
        return position == 3
    elif position % 2 == 0:
        return heap19(rocks + 1, position + 1) or heap19(rocks * 2, position + 1)
    else:
        return heap19(rocks + 1, position + 1) and heap19(rocks * 2, position + 1)

for answer19 in range(1, 160 + 1):
    print(answer19) if heap19(answer19, 1) else None

print("№20:")  # 40 79
def heap20(rocks, position):
    if rocks >= 161 or position > 4:
        return position == 4
    elif position % 2 != 0:
        return heap20(rocks + 1, position + 1) or heap20(rocks * 2, position + 1)
    else:
        return heap20(rocks + 1, position + 1) and heap20(rocks * 2, position + 1)

for answer20 in range(1, 160 + 1):
    print(answer20) if heap20(answer20, 1) else None

print("№21:")  # 78
def heap21(rocks, position):
    if rocks >= 161 or position > 5:
        return position == 3 or position == 5
    elif position % 2 == 0:
        return heap21(rocks + 1, position + 1) or heap21(rocks * 2, position + 1)
    else:
        return heap21(rocks + 1, position + 1) and heap21(rocks * 2, position + 1)

for answer21 in range(1, 160 + 1):
    print(answer21) if heap21(answer21, 1) else None

print("№23:")  # 1760
func23 = lambda start, end, exc: func23(start - 1, end, exc) + func23(start // 2, end, exc) if start > end and start != exc else start == end
print(func23(60, 20, 4) * func23(20, 1, 4))

print("№24:")  # 10007
with open('C:/for типовые 20 вариантов/24/24var04.txt') as file24:
    f = file24.read().strip().split('AB')  # ВАЖНО: "сплит" формирует список, действуем нетипично
    max_len = 0
    for index in range(len(f)):
        cur_string = ''.join(f[index:index + 21 + 1])  # Потому что учёт разделённых и нестрого
        max_len = max(max_len, len(cur_string))  # Здесь лежат НЕ "AB"
print(max_len + 21 * 2 + 2)  # Cамо кол-во AB и мусор по бокам интервала

print("№25:")  # Ответ верный
digits = '0123456789'
for length in range(4):
    for asterisk in product(digits, repeat=length):
        for question_mark in digits:
            mask = int(f"33{''.join(asterisk)}21{question_mark}7")
            print(mask, mask // 2079) if mask % 2079 == 0 else None

print("№26:")  # 

print("№27:")  # 
