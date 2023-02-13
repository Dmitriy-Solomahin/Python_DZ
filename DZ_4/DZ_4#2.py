# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9
from random  import randint

size = int(input('введите количество кустов: '))
harvest = []

for _ in range(size):
    harvest.append(randint(1,11))

print(harvest)
max_sum_berry = 0

for i in range(len(harvest)):
    if i == 0:
        sum_berry = harvest[i] + harvest[i+1] + harvest[-1]
    elif i == (size - 1):
        sum_berry = harvest[i] + harvest[0] + harvest[i-1]
    else:
        sum_berry = harvest[i] + harvest[i+1] + harvest[i-1]
    if sum_berry > max_sum_berry:
        max_sum_berry = sum_berry

print(max_sum_berry)