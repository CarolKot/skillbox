# Рахрыв Если обнаружено число 5 выйти из программы и посчитать сумму чисел

number = int(input("Введите натуральное число? "))
summ = 0
while number != 0:
    last_num = number % 10
    print(last_num)
    if last_num == 5:
        print(f'В числе обнаружен разрыв!')
        break
    summ += last_num
    number //= 10
print(f'Сумма чисел = {summ}')
        