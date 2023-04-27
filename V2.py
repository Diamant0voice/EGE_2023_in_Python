# Solved by Ostap Baranov in preparation for the Russian Unified State Exam in CS, 2023.
#
# All tasks were developed by Krulov S. S. in 2023 and belongs to the © National Education Publishing, LLC.

from turtle import *
from math import floor, ceil, log, sqrt
from itertools import product, permutations
from functools import lru_cache

print("№2:")  # xzyw
def columns(y, x, w, z):
    return y and (x <= w) and ((not x) <= ((not w) == z))


for holes in product([0, 1], repeat=5):
    table = [(0, 0, holes[0], holes[1]), (0, holes[2], holes[3], 0), (1, 1, 1, holes[4])]; F = [1, 1, 0]
    if len(table) == len(set(table)):
        for answer2 in permutations('yxwz'):
            print(*answer2, sep='') if [columns(**dict(zip(answer2, variation))) for variation in table] == F else None

print("№5:")  # 25
for N in range(1, 1000):
    B = bin(N)[2:]
    B += '0' if N % 2 == 0 else '1'
    B = B.replace(B[:2],'11', 1) if B.count('1') % 3 == 0 else B.replace(B[:2], '10', 1)
    R = int(B, 2)
    print(N) if R <= 37 else None

print("№6:")  # 882
screensize(4000, 4000)
tracer(0)
hideturtle()  # Если рисунок ясен, можно скрыть исполнителя вовсе. Немного ускорит вывод
speed(10)
color("green", "red")
scale = 60
counter6 = 0

up()
left(90)
forward(100 * scale)
right(90)
forward(100 * scale)
right(45)
down()
begin_fill()
for repeat in range(4):
    forward(30 * scale)
    right(90)
end_fill()
up()

canvas = getcanvas()
for X in range(-250 * scale, 250 * scale, scale):
    for Y in range(-250 * scale, 250 * scale, scale):
        scanner = canvas.find_overlapping(X, Y, X, Y)
        counter6 += 1 if len(scanner) == 1 and scanner[0] == 5 else 0  # Переписано через тернарку

print(counter6)
update()
exitonclick()

print("№8:")  # 174
counter = 0
for digits in product('0123', repeat=5):
    number = ''.join(digits)
    if number.count('3') == 1 and number[0] != '0' and all(number.count(fail) == 0 for fail in {'03', '30'}):
        counter += 1
print(counter)

print("№12:")  # 1212122
string = '22' + "1" * 2050 + '22'
while '211' in string or '112' in string:
    string = string.replace('11', '1', 1)
    if '21' in string:
        string = string.replace('21', '12', 1)
    else:
        string = string.replace('12', '1', 1)
print(string)

print("№14:")  # 1015
def in8(number):  # Альтернативное решение функцией, дольше, но корректнее
    sys = 8
    convert = changed = " "
    while number > 0:
        convert += str(number % sys); number //= sys
    convert = list(reversed(convert))  # Элемент [-1] (последний) становится [0] (первым), и так со всеми, типа [::-1]
    for digits in range(len(convert)):
        changed += convert[digits]
    return str(changed)
print(in8(4**2022 - 6 * 4**522 + 5 * 64**510 - 3 * 2**330 - 100).count('7'))

print('№15:')  # 80
def logic(x, A):
    return ((x % 20 == 0) <= (x % 11 != 0)) or (x + A >= 300)

for A in range(1, 1000):
    if all(logic(x, A) for x in range(1, 1000)):
        print(A)
        break
    A -= 1

print("№16:")  # 987
@lru_cache(None)
def F(n):
    if n < 3:  # Альтернативный способ, пошустрее: создаём функцию под выражение
        return n  # Перебираем удачные варианты для подстановки
    elif n > 2 and n % 2 == 0:
        return 3 * (n - 1) + F(n - 1) + 5
    elif n > 2 and n % 2 != 0:
        return 3 * (n + 1) + F(n - 2) - 2
print(F(35))

print("№17:")  # 4 9994000936
counter = squares = 0
with open('C:/for типовые 20 вариантов/17/17var02.txt') as file17:
    file17 = [int(num) for num in file17]
    maximum = max(file17)
    for number, number_next in zip(file17, file17[1:]):
        if number + number_next == maximum:
            counter += 1
            squares = max(squares, number ** 2 + number_next ** 2)
print(counter, squares)

print("№19:")  # 150
def heap19(rocks1, positions):
    if rocks1 >= 301 or positions > 3:
        return positions == 3
    if positions % 2 == 0:
        return heap19(rocks1 + 1, positions + 1) or heap19(rocks1 * 2, positions + 1)
    else:
        return heap19(rocks1 + 1, positions + 1) and heap19(rocks1 * 2, positions + 1)
    

for answer19 in range(1, 300 + 1):
    print(answer19) if heap19(answer19, 1) else None

print("№20:")  # 75 149
def heap20(rocks1, positions):
    if rocks1 >= 301 or positions > 4:
        return positions == 4
    if positions % 2 != 0:
        return heap20(rocks1 + 1, positions + 1) or heap20(rocks1 * 2, positions + 1)
    else:
        return heap20(rocks1 + 1, positions + 1) and heap20(rocks1 * 2, positions + 1)
   

for answer20 in range(1, 300 + 1):
    print(answer20) if heap20(answer20, 1) else None

print("№21:")  # 148
def heap21(rocks1, positions):
    if rocks1 >= 301 or positions > 5:
        return positions == 3 or positions == 5
    if positions % 2 == 0:
        return heap21(rocks1 + 1, positions + 1) or heap21(rocks1 * 2, positions + 1)
    else:
        return heap21(rocks1 + 1, positions + 1) and heap21(rocks1 * 2, positions + 1)


for answer21 in range(1, 300 + 1):
    print(answer21) if heap21(answer21, 1) else None

print("№23:")  # 1956
func23 = lambda start, end: func23(start - 1, end) + func23(start // 2, end) if start > end else start == end
print(func23(60, 10) * func23(10, 2))

print("№24:")  # 40
with open('C:/for типовые 20 вариантов/24/24var02.txt') as file24:
    f = file24.read().strip()  
    array = list()  # Создаём пустой список для индексов букв А
    min_len = float('inf')  # Ищем меньшее - ставим большее, бесконечность - в самый раз
    for index in range(len(f)):
        if f[index] == 'A':  # Дальше 2 варианта событий:
            if len(array) < 35 - 1:  # Мест в списке хватает, тогда
                array.append(index) # Сохраняем индекс буквы
            else:  # Места кончились, значит можем сравнивать длины
                min_len = min(index - array[0] + 1, min_len)   # Первое в min'е - НЕСТРОГАЯ длина текущей строки
                array = array[1:] + [index]  # Выкидываем старейший индекс для усл. 'len == 35' и заново
print(min_len)

print("№25:")  # Ответ верный
for length in range(4):
    for random_digit in product('0123456789', repeat=length):
        mask = int(f"32{''.join(random_digit)}823")
        print(mask, mask // 123) if mask % 123 == 0 else None

print("№26:")  # 

print("№27:")  # 
