# 
# Задача 1. Вода
# Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных магазинах стоит по-разному.

# Напишите программу, которая три раза вызывает функцию about_water, передаёт в неё один аргумент — цену на воду и выводит на экран название воды, производителя и цену.

 # Пример:

# Название: КлирВотер

# Производитель: ВодЗавод

# Цена: 25

#water_price

def about_water(price):
    print(f'\n Название: КлирВотер')
    print(f'\n Производитель: ВодЗавод')
    print(f'\n Цена:  {price}')


about_water(25)
about_water(30)
about_water(40)