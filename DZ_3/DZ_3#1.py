# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint


my_list = []
max_value = 100 
min_value = 1

size = int(input("введите длину списка: "))
number = int(input("введите искомое число: "))

for i in range((size)):
    my_list.append(randint(min_value, max_value))

print(my_list)

result = my_list.count(number)
if result == 0:
    print(f'ближайшее по значению число: {min(my_list, key=lambda x:abs(x-number))}')
else:
    print(f'искомое число встречается {result} раз')

