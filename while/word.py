#Попробуй написать код, который: ✅ Запрашивает число
#✅Если число больше 10, говорит "Большое число!"
#✅ Если число чётное, пишет "Это чётное число"
#✅ Если число нечётное, пишет "Это нечётное число"
#✅ Если число меньше или равно 10, говорит "Маленькое число"

#⚡ Сможешь сделать? Пробуй, а я потом помогу! 🚀

while True:
    num = int(input('Запрашивает число ? '))
    if num > 10:
        print('Большое число!')
    else:
        print('Маленькое число')

    if num % 2 == 0:
        print('Это чётное число')
    else:
        print('Это нечётное число')
  