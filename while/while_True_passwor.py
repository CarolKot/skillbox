# Вирус

#Дима написал программу-вирус специально для того,
# чтобы проучить своего друга-должника, который никак не хочет возвращать скейтборд.
# Программа не даёт работать за компьютером и постоянно выводит на экран
# сообщение “Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!”.
# Как только вводится правильный код: вирус удаляется. Напишите такую же программу,
# которую написал Дима. Код не может начинаться с цифры 0.

print("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!")

while True:
    password = int(input("Введите код: "))
    if password != 550:
        print("Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!")
    else:
        print("Код верный, завершаю работу...")
        break




# ИЛИ
exit_code = 550
while True:
    print("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!")
    user_code = int(input("Введите код: "))
    if user_code == exit_code:
        print("Код верный, завершаю работу...")
        break



        