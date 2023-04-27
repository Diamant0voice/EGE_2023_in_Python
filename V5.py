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
for N in range(100, 1001):
    dig1 = N // 100; dig2 = N // 10 % 10; dig3 = N % 10  # Остатком отщепляем последнюю цифру, цельняком - первую
    sum1 = dig1**2 + dig2**2; sum2 = dig2**2 + dig3**2  # Суммы квадратов
    R = str(max(sum1, sum2)) + str(min(sum1, sum2)) # В порядке невозрастания 
    print(N) if R == '9752' else None  # Выбираем наибольшее

print("№6:")  # 5280
screensize(10000, 10000)
tracer(0)
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

print("№8:")  # 129
counter = 0
for let1, let2, let3, let4 in product('АМОТ', repeat=4):
    counter += 1
    word = let1 + let2 + let3 + let4
    if word[0] == "О":
        break
print(counter, word)

print("№10:")  # 5
kr = 0  # ну а почему бы и нет?
with open('C:/for типовые 20 вариантов/10/Отцы и дети.txt', 'r') as book:
    for word in book:
        if "Деньги" in word or "деньги" in word:
            kr += 1
print(kr)

print("№12:")  # 5511
string = '1' * 2022
while '11111' in string or '555' in string:
    string = string.replace('11111', '555', 1) if '11111' in string else string.replace('555', '5', 1)
print(string)

print("№14:")  # 690
cr = 5**2022 - 2 * 5**1010 + 25**850 + 2500
counter = 0
while cr > 0:
    if cr % 5 == 4:
        counter += 1
    cr //= 5    
print(counter)

print("№15:")  # 17
def logic(x):
    return not(((x in B) or (x in C)) <= (x in A))  # Перебиваем выражение, стандарт

A = list()  # Создаём отрезок и пилим имеющиеся
B = [points for points in range(10, 15 + 1)]
C = [points for points in range(20, 27 + 1)]

for points in range(1, 1000):  # Базовый перебор
    if logic(points):
        A.append(points)  # (НЕ) подходящие точки в новый отрезок
print(A[-1] - A[0])  # Длина отрезка - его модуль - разность конца с началом, это и просят

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
with open('C:/for типовые 20 вариантов/17/17var05.txt') as file17:
    numbers = [int(index) for index in file17]
    squares = [index ** 2 for index in range(1, 100 + 1)]
    counter = max_sum = 0
    for elem1, elem2 in zip(numbers, numbers[1:]):
        if elem1 in squares or elem2 in squares:
            counter += 1
            max_sum = max(max_sum, elem1 + elem2)
print(counter, max_sum)    

print("№19:")  # 90
def heap19(rocks, position):
    if rocks >= 181 or position > 3:
        return position == 3
    elif position % 2 == 0:
        return heap19(rocks + 1, position + 1) or heap19(rocks * 2, position + 1)
    else:
        return heap19(rocks + 1, position + 1) and heap19(rocks * 2, position + 1)

for answer19 in range(1, 180 + 1):
    print(answer19) if heap19(answer19, 1) else None

print("№20:")  # 45 89
def heap20(rocks, position):
    if rocks >= 181 or position > 4:
        return position == 4
    elif position % 2 != 0:
        return heap20(rocks + 1, position + 1) or heap20(rocks * 2, position + 1)
    else:
        return heap20(rocks + 1, position + 1) and heap20(rocks * 2, position + 1)

for answer20 in range(1, 180 + 1):
    print(answer20) if heap20(answer20, 1) else None

print("№21:")  # 88
def heap21(rocks, position):
    if rocks >= 181 or position > 5:
        return position == 3 or position == 5
    elif position % 2 == 0:
        return heap21(rocks + 1, position + 1) or heap21(rocks * 2, position + 1)
    else:
        return heap21(rocks + 1, position + 1) and heap21(rocks * 2, position + 1)

for answer21 in range(1, 180 + 1):
    print(answer21) if heap21(answer21, 1) else None

print("№23:")  # 639
func23 = lambda start, end: func23(start + 2, end) + func23(start + 7, end) if start < end else start == end
print(func23(5, 49))

print("№24:")  # 977
with open('C:/for типовые 20 вариантов/24/24var05-08.txt') as file24:
    f = file24.read().strip()
    cur_len = max_len = 0
    for index in range(len(f) - 1):
        if f[index] + f[index - 1] == '00':
            cur_len = 1
        else:
            cur_len += 1
            max_len = max(cur_len, max_len)
print(max_len)

print("№25:")  # Ответ верный
def divs(number):
    s = set()  # Во множестве будем сохранять выявленные делители числа
    for divider in range(2, int(number ** 0.5) + 1):  # "Не считая 1"
        if number % divider == 0:
            s.add(divider); s.add(number // divider)  # Пройдясь до корня, повторяем с конца (делители симметричны)
    return sorted(s)  # Делаем красоту

for number in range(860_000, 870_001):
    d = divs(number)
    if len(d) > 0:  # ОЧЕНЬ важное ограничение
        M = max(d) - min(d)
        print(number, M) if M % 100 == 18 else None  # Берём крайние пять пар

print("№26:")  # 

print("№27:")  # 
