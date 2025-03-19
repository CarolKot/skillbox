count = 0

while count < 3:
    word = input('Введи слово?! python ' ).lower()
    if word != 'python':
        print('Неверно! Пробуй ещё раз!')
        count += 1
    elif word == 'python':
        print("Верно! Выход...")
        break
else:
    print("Слишком много ошибок! Выход...")

