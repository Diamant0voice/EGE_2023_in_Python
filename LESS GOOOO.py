from itertools import combinations

print("№27A v1:")  # Простейший способ, через вложенные циклы
N, K, *numbers = map(int, open('27A.txt')) # первые 2 числа в свои переменные, другие в распаковывающийся список
minimum_multip_triple = float('inf')
for index0 in range(N):
    for index1 in range(index0 + K, N):  # ВАЖНО! Если бы K было разностью индексов, то + 1
        for index2 in range(index1 + K, N):
            minimum_multip_triple = min(minimum_multip_triple, number[index0] * number[index1] * number[index2])
print(minimum_multip_triple)

print("№27A v2:")  # То же самое, но короче
N, K, *numbers = map(int, open('27A.txt'))
minimum_multip_triple = float('inf')
print(min(numbers[i0] * numbers[i1] * numbers[i2] for i0, i1, i2 in combinations(range(N), 3) if K <= i1 - i0 <= i2 - i1))

print("№27B:")
N, K, *numbers = map(int, open('27B.txt'))
far_left_num = min_multip_pair = min_multip_triple = float('inf')
for index in range(2 * K, N):  # т. к. длина между числами пары = К, то между числами тройки - х2 больше
    far_left_num = min(far_left_num, numbers[index - 2 * K])  # крайний левый элемент
    min_multip_pair = min(min_multip_pair, far_left_num * numbers[index - K])  # Средний * на крайний левый
    min_multip_triple = min(min_multip_triple, min_multip_pair * numbers[index])  # Крайний правый * средний * крайний левый, ответ
print(min_multip_triple) 

print("№24v1")  # МАКСИМАЛЬНОЕ количество идущих подряд символов среди которых Y не более 150 раз
with open("24.txt") as file24:
    f = file24.read().strip().split('Y')
    maximum = float('-inf')
    for index in range(len(s) - 150 + 1):
        string = 'Y'.join(f[index:index + 150 + 1])
        maximum = max(maximum, len(string))
print(maximum)

print("№24v2")  # МИНИМАЛЬНОЕ количество идущих подряд символов среди которых Y не более 150 раз
with open("24.txt") as file24:
    f = file24.read().strip().split('Y')
    minimum = float('inf')
    for index in range(len(s) - 150 + 1):
        string = 'Y'.join(f[index + 1:index + 150])
        minimum = max(minimum, len(string))
print(minimum)

# ПЕРЕВОД В СИСТЕМЫ СЧИСЛЕНИЯ:
def SS(number):
    itog = ''
    while number > 0:
        itog = str(number % 3) + itog
        number //= 3
    return itog

print("№14v1:")
for X in '0123456789ABCDEFGHI':
    operand = int(f'98{X}79641', 19) + int(f'36{X}14', 19) + int(f'73{X}4', 19)
    print(operand // 19) if operand % 19 == 0 else None

print("№14v2:")
cringe = 1331**650 - 55 * 121**610 + 77 * 11 **510 - 3 * 11**100 - 221
counter = 0
while cringe > 0:
    counter += 1 if cringe % 11 == 10 else 0  # Разводка десятичным эквивалентом буквы относительно её положения в 16-ричной с.с.
    cringe //= 11
print(counter)

print("№17:")
with open('17.txt') as file17:
    sequence = [int(number) for number in file17]
    maximum_15 = max([index for index in sequence if index % 100 == 15])
    count = checker_4 = 0
    maximum_sum = float('-inf')
    for index in range(len(sequence) - 2):
        checker_4 += 1000 <= sequence[index] <= 9999
        checker_4 += 1000 <= sequence[index + 1] <= 9999
        checker_4 += 1000 <= sequence[index + 2] <= 9999
        if checker_4 == 1 and sequence[index] + sequence[index + 1] + sequence[index + 2] >= maximum_15:
            counter += 1
            maximum_sum = max(maximum_sum, sequence[index] + sequence[index + 1] + sequence[index + 2])
print(counter, maximum_sum)

print("№15:")
def logic(x):
    ...
def logic(x):
    return not(((x in B) or (x in C)) <= (x in A))  # Перебиваем выражение, стандарт

A = list()  # Создаём отрезок и пилим имеющиеся
B = [points for points in range(10, 15 + 1)]
C = [points for points in range(20, 27 + 1)]

for points in range(1, 1000):  # Как обычно перебираем
    if logic(points):
        A.append(points)  # (НЕ) подходящие точки в новый отрезок
print(A[-1] - A[0])  # Длина отрезка - его модуль - разность конца с началом, это и просят

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

print("№2:")
def columns(x, y, w, z):
    return not(((x <= y) <= w)) and z

for holes in product([0, 1], repeat=7):
    table = [() () () ()]; F = [1, 1, 1]
    if len(table) == len(set(table)):
        for answer2 in permutations('xywz'):
            print(*anwer2, sep='') if [columns(**dict(zip(answer2, variables))) for variables in table] == F else None








