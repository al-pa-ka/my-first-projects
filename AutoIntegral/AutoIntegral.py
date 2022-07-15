from math import * #used in eval


def right_rectangles(table, step):
    total = 0
    for y in table[0:len(table)-1:]:
        total = total + y
    result = step * total
    print('(({}-{})/{})*({})={}'.format(b, a, n, total, round(result, 3)))
    return round(result, 3)


def left_rectangles(table, step):
    total = 0
    for y in table[1:len(table):]:
        total = total + y
    result = step * total
    print('(({}-{})/{})*({})={}'.format(b, a, n, total, round(result, 3)))
    return round(result, 3)


def trapezoid(table, step):
    total = 0
    
    for y in table[1:len(table)-1:]:
        total = total + y
    
    total = round(total, 3)
    total *= 2
    result = (step/2)*(total + table[0] + table[len(table) - 1])
    print('(({}-{})/(2*{}))*({}+{}+2*{})={}'.format(b, a, n, table[0], table[len(table)-1],
                                                    total / 2, round(result, 3)))
    return round(result, 3)


def parabola(table, step):
    sum1 = 0
    sum2 = 0

    for count, y in enumerate(table[1:n]):
        if count % 2 != 0:
            sum1 = sum1+y

    sum1 = sum1*2    
    sum1 = round(sum1, 3)
    
    for count, y in enumerate(table[1:n]):
       
        if count % 2 == 0:
            sum2 = sum2+y
    
    sum2 = sum2*4
    sum2 = round(sum2, 3)
   
    result = (step/3)*(table[0] + table[len(table)-1] + sum1 + sum2)

    print('(({}-{})/(3*{}))*({}+{}+2*{}+4*{})={}'.format(b, a, n, table[0], table[len(table)-1],
                                                         sum1/2, sum2/4, round(result, 3)))

    return round(result, 3)


table = [[], []]

a = float(input("Введите a: "))
b = float(input("Введите b: "))

f = str(input("Введите подинтегральное выражение: "))

n = int(input("Введите n: "))

x = round(a, 3)

step = (b-a)/n

for i in range(n+1):
    print('\t', i, end='')

print('\n') 

for i in range(n+1):
    print('\t', x, end='')
    table[0].append(x)
    x = round((x+step), 3)

print('\n')

for x in table[0]:
    result = round(eval(f), 3)
    table[1].append(result)
    print('\t', result, end='')

print('\n')
print('Метод правых прямоугольников: ')
right_rectangles(table[1], step)

print('\n')
print('Метод левых прямоугольников: ')
left_rectangles(table[1], step)

print('\n')

print('Метод трапеций: ')
trapezoid(table[1], step)

print('\n')

print('Метод парабол: ')
parabola(table[1], step)

print('\n')

input()
