# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_number = int(input('Введите первый элемент прогрессии: '))
difference = int(input('Ведите разность: '))
size = int(input('Ведите длину прогрессии: '))

number_list = []


for i in range(size):
    number_list.append(first_number + (difference) * i)

print(number_list)

