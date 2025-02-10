# functions skillbox



# print(f'Обезьяны')
# fruits = int(input('Сколько фруктов? '))
# vegetables = int(input('Сколько овощей? '))
# print(f'Всего: {fruits+vegetables}')

# print(f'\nЖирафы')
# fruits = int(input('Сколько фруктов? '))
# vegetables = int(input('Сколько овощей? '))
# print(f'Всего: {fruits+vegetables}')

# print(f'\nСлоны')
# fruits = int(input('Сколько фруктов? '))
# vegetables = int(input('Сколько овощей? '))
# print(f'Всего: {fruits+vegetables}')
    

# # Сокращаем

# def count_food():
#     fruits = int(input('Сколько фруктов? '))
#     vegetables = int(input('Сколько овощей? '))
#     print(f'Всего: {fruits+vegetables}')


# print(f'\nОбезьяны')
# count_food()
# print(f'\nЖирафы')
# count_food()
# print(f'\nСлоны')
# count_food()


# Задача: Пользователь делает выбор, что вывести на экран
# 1 - треугольник 2 прямогугольник
# На выходе должна получиться фигура из *, ровно из 5 строк

def triangel():
    srats = 1
    for line in range(5):
        print(' ' * (5 - line -1), end = '')
        print('*' * srats)
        srats += 2

def rectangel():
    for line in range(5):
        if line == 0 or line == 4:
         print('*' * 5)
        else:
            print('*' + ' ' * 3 + '*')
        

choice = int(input('Сделайте выбор: '))
if choice == 1:
    triangel()
elif choice == 2:
    rectangel()
else:
    print(f'Неверный ввод!')


