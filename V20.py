# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # wzxy
def columns(w, x, z, y):
    return not(w <= x) or ((not z) <= (not y)) or z


for holes in product((0, 1), repeat=6):
    table = [(holes[0], 0, 1, 1), (1, holes[1], 1, holes[2]), (holes[3], holes[4], holes[5], 1)]; F = [0, 0, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('wxzy'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variations))) for variations in table] == F else None

print("№5:")  # 106
for N in range(1, 100):
    R = N * 4 + N % 4
    if R < 111:
        print(R)
        

print('№6:')  # Ответ: 64
screensize(4000, 4000)
ht()
speed(500)  # Без заполнения выходит дольше, но мы не ждём
color("orange")
pensize(0.1)
tracer(0)
scale = 50

lt(90)
rt(300)
for rep in range(6):  # Звездулька - типа подарка за труды?) Вот спасибо...
    fd(5 * scale)  
    rt(120)
    fd(5 * scale)
    rt(330 * scale)
up()

for X in range(-50, 50):
    for Y in range(-50, 50):
        goto(X * scale, Y * scale)  # Равномерно скачем на поле по сетке
        dot(3, "green")  # И оставляем там видимые следы, чтобы вручную посчитать

update()
exitonclick()
# По ЗАДУМКЕ, так решаться должно всё, но по факту данный способ актуален лишь пару раз, и не стоит таких усилий.

print("№8:")  # 54
counter = 0
for symbol in product('ABCD', repeat=4):
    code = ''.join(symbol)
    counter += 1 if code.count('A') == 2 else 0
print(counter)

print("№10:")  # 2
kr = 0
with open('C:/for типовые 20 вариантов/DONE/10/Отцы и дети.txt', 'r') as book:
    for word in book:
        if "Россия" in word:
            kr += 1
print(kr)

print("№12:")  # 
def isP(n):
    return n > 1 and all(n % divider != 0 for divider in range(2, int(n ** 0.5) + 1))

for n in range(1, 10): 
    string = '>' + '1' * 23 + '2' * n + '3' * 25
    while '>1' in string or '>2' in string or '>3' in string:
        string = string.replace('>1', '1>', 1) if '>1' in string else string
        string = string.replace('>2', '>3', 1) if '>2' in string else string
        string = string.replace('>3', '>11', 1) if '>3' in string else string
    if isP(string.count('1') + string.count('2') + string.count('3')):
        print(n)
        break

print("№14:")  # 196
counter = 0
cr = 3**2017 + 9**1000 + 9**100 - 3**4
while cr > 0:
    if cr % 3 == 2:
        counter += 1
    cr //= 3
print(counter)

print("№15:")  # 

print("№16:")  # 50
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return (8 * n + F(n - 3)) // 9
    elif n > 2 and n % 2 != 0:
        return (4 * n + F(n - 1) + F(n - 2)) // 7
print(F(52))

print("№17:")  # 

print("№19:")  # 

print("№20:")  # 

print("№21:")  # 

print("№23:")  # 28
func23 = lambda start, end, exc: func23(start + 1, end, exc) + func23(start * 2, end, exc) if start < end and start != exc else start == end
print(func23(2, 10, 19) * func23(10, 26, 19))

print("№24:")  # 

print("№25:")  # 
def isPrime(number):
    return number > 1 and all(number % divider != 0 for divider in range(2, int(number ** 0.5) + 1))

def divs(number):
    s = set()
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            s.add(divider); s.add(number // divider)
    return sorted(s)

for number in range(550_001, 555_001):
    d = divs(number)
    S = sum([index for index in d if isPrime(index)])
    print(number, S) if S % 10 == 7 else None

print("№27:")  # 
