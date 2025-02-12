#navigator


import math

def my_distance(x,y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)

def bitweenDistance(x_1,y_1,x_2,y_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2-y_1) ** 2)
    print(distance)

chois = int(input('1 - расстояние до точки; 2 - расстаяние между двумя точками'))
if chois == 1:
    x = int(input('Введите Х: '))
    y = int(input('Введите У: '))
    my_distance(x,y)
elif chois == 2:
    x_1 = int(input('Введите Х первой точки: '))
    y_1 = int(input('Введите У первой точки: '))
    x_2 = int(input('Введите Х второй точки: '))
    y_2 = int(input('Введите У второй точки: '))
    bitweenDistance(x_1,y_1,x_2,y_2)
else:
    print('Ошибка ввода!')



