run = False

while not run:
    exitt = input('Вы хотите выйти? да/нет ' ).lower()
    if exitt == 'да':
        run = True
        print('Выход')
    elif exitt == 'выход':
        print('Программа завершена')
        break
    
    elif exitt != 'да' and exitt != 'нет':
        print('Введите только да/нет')
        continue
    