# while True Флаг

rate_chek = False

while True:
    active = int(input('Продолжаем раюоать? 1/0: '))
    if active == 0:
        print('Работа завершается!')
        break
    rate = int(input('Поставите оценку приложению? 1/0: '))
    if rate == 1:
        rate_chek = True
    
print('Работа завершается!')   
if rate_chek == True:
    print('Пользователь поставит оценку. ')





        