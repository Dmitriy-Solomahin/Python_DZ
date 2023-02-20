# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

string = input('введите стихотворение с пробелом между фразами и - между словами: ')

string = string.split()


def counting_vowels(list_string: list) -> list:
    volwels = ['а', 'я', 'о', 'ё', 'э', 'е', 'ы', 'и', 'у', 'ю' ]
    new_list = []
    for item in list_string:
        num = 0
        item = item.lower()
        for i in item:
            if i in volwels:
                num += 1
        new_list.append(num)
    return new_list

def phrases_equal(number_list: list) -> bool:
    number = number_list[0]
    for i in number_list:
        if i != number:
            return False
    return True

number_list = counting_vowels(string)
result = phrases_equal(number_list)


if result:
    print('Парам пам-пам')
else:
    print('Пам парам')

