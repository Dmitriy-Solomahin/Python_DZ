# Определить индексы элементов списка, значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

size = int(input('Введите длину списка: '))
min_n = int(input('Ведите мин элемент: '))
max_n = int(input('Ведите макс элемент: '))

number_list = []
new_list = []

for _ in range(size):
    number_list.append(random.randint(-10,10))

print(number_list)


for i in range(len(number_list)):
    if min_n <= number_list[i] <= max_n:
        new_list.append(i)

print(new_list)