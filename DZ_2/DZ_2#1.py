# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
from random import randint


number_of_coins = int(input('введите количество монет: '))

count_one = 0
count_zero = 0

for _ in range(number_of_coins):
    number = randint(0,1)
    print(number)
    if number == 0:
        count_zero += 1
    elif number == 1:
        count_one += 1

if count_zero > count_one:
    print(f'надо перевернуть {count_one} монет')
else:
    print(f'надо перевернуть {count_zero} монет')