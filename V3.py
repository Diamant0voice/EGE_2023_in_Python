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
for N in range(1, 100):
    B = bin(N)[2:]
    if len(B) % 2 == 0:
        B = B[:len(B) // 2] + '1' + B[len(B) // 2:]  # Не совсем логично, но пихаем в середину 1
    R = int(B, 2)
    if R >= 26:
        print(N, "а само число такое", R)
        break

print("№6:")  # 1200
screensize(10000, 10000)
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
exitonclick()

print("№8")  # 72
counter = 0
for let1, let2, let3, let4, let5, let6 in product("КНОРСЯ", repeat=6):  # Считываем алфавит ИЗ ПРИМЕРА
    word = let1 + let2 + let3 + let4 + let5 + let6
    counter += 1  # Здесь мы просто нумеруем слова, счётчик не функциональный
    if word.count('К') <= 3 and word.count('Я') == 2:
        print(counter, word)
        break

print("№12:")  # 121222
string12 = '22' + '1' * 2024 + '22'
while '2111' in string12 or '1112' in string12:
    string12 = string12.replace('111', '1', 1)
    string12 = string12.replace('21', '12', 1) if '21' in string12 else string12.replace('12', '1', 1)
print(string12)

print("№14:") # 1071
bruh = 243**540 - 6 * 9**530 + 21 * 3**511 - 3 * 3**70 - 200 
counter = 0
while bruh > 0:
    if bruh % 9 == 8:
        counter += 1
    bruh //= 9
print(counter)

print("№15:")  # 24
def treug(n, m, k):
    return n + m > k and n + k > m and m + k > n  # функция по смыслу, кукож тот ещё


for A in range(1, 1000):
    while True:  # Как в предыдущем варианте, только НЕ МАКС изменили по информации из примечания
        if all(not((treug(x, 11, 18) == (max(x, 5) <= 15)) and (treug(x, A, 5))) for x in range(1, 1000)):
            print(A)
        break
    A  -= 1  # Чтобы прога не уходила в отрицательные числа из-за особенностей ТРЕУГ функции

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

print("№17")  # 203 99820
counter = sums = 0
with open('C:/for типовые 20 вариантов/17/17var03.txt') as file17:
    sequence = [int(numbers) for numbers in file17]
    maximum = max(number for number in sequence)
    for elem1, elem2, elem3 in zip(sequence, sequence[1:], sequence[2:]):
        last_digits = str(elem1 % 10) + str(elem2 % 10) + str(elem3 % 10)
        if last_digits.count('0') == 1 and elem1 + elem2 + elem3 < maximum:
            counter += 1
            sums = max(sums, elem1 + elem2 + elem3)
    print(counter, sums)

print("№19:")  # 76
def heap19(rocks1, positions):
    if rocks1 >= 153 or positions > 3:
        return positions == 3
    elif positions % 2 == 0:
        return heap19(rocks1 + 1, positions + 1) or heap19(rocks1 * 2, positions + 1)
    else:
        return heap19(rocks1 + 1, positions + 1) and heap19(rocks1 * 2, positions + 1)


for answer19 in range(1, 152 + 1):
    print(answer19) if heap19(answer19, 1) else None

print("№20:")  # 38 75
def heap20(rocks1, positions):
    if rocks1 >= 153 or positions > 4:
        return positions == 4
    elif positions % 2 != 0:
        return heap20(rocks1 + 1, positions + 1) or heap20(rocks1 * 2, positions + 1)
    else:
        return heap20(rocks1 + 1, positions + 1) and heap20(rocks1 * 2, positions + 1)


for answer20 in range(1, 152 + 1):
    print(answer20) if heap20(answer20, 1) else None

print("№21:")  # 74
def heap21(rocks1, positions):
    if rocks1 >= 153 or positions > 5:
        return positions == 3 or positions == 5
    elif positions % 2 == 0:
        return heap21(rocks1 + 1, positions + 1) or heap21(rocks1 * 2, positions + 1)
    else:
        return heap21(rocks1 + 1, positions + 1) and heap21(rocks1 * 2, positions + 1)


for answer21 in range(1, 152 + 1):
    print(answer21) if heap21(answer21, 1) else None

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
    print(counterMin + 21 * 2)

print("№25:")  # Ответ верный
digits = '0123456789'
for length in range(4):
    for asterisk in product(digits, repeat=length):
        for question_mark in digits:
            mask = int(f"32{''.join(asterisk)}21{question_mark}4")
            print(mask, mask // 2049) if mask % 2049 == 0 else None

print("№27:")  # 
