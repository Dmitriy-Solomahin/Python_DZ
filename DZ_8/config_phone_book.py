phone_book = []

def print_menu():
    print('1. Открыть файл')
    print('2. Сохранить файл')
    print('3. Показать контакты')
    print('4. Добавить контакт')
    print('5. Найти контакт')
    # print('5. Изменить контакт')
    # print('7. Удалить контакт')
    print('6. Выход')
    num = int(input('введите номер операции: '))
    return num

def work_menu():
    while True:
        num = print_menu()
        match num:
            case 1:
                open_phone_number()
            case 2:
                save_phone_number()
            case 3:
                show_phone_number()
            case 4:
                add_phone_number()
            case 5:
                search_phone_number()
            case 6:
                user_answer = input('все несохранённые данные будут утерены! Сохранить файл?(y - да, n - нет): ')
                if user_answer.lower() == 'y' or user_answer.lower() == 'да':
                    save_phone_number()
                print('Досвидания')
                break
            case _:
                print('неверна выбрана операция!')

def open_phone_number():
    with open('phones_book.txt', 'r', encoding='utf-8') as data:
        phone_book.extend(data.readlines())  
        print('Файл открыт')
        
def save_phone_number():
    with open('phones_book.txt', 'w', encoding='utf-8') as data:
        for i in phone_book:
            data.write(str(i))
        print('Файл сохранён')

def show_phone_number():
    if len(phone_book) == 0:
        print('Вы не открыли файл или файл пуст')
    else: 
        for i in phone_book:
            print(' '.join(i.split(';')))

def add_phone_number():
    if len(phone_book) == 0:
        print('Вы не открыли файл или файл пуст')
    else:
        user_info_name = input('Ввидите ФИО нового контакта: ')
        user_info_phone = input('Ввидите номер контакта: ')
        user_info_coment = input('Ввидите коментарий к новому контакту: ')
        user_info = f'{user_info_name};{user_info_phone};{user_info_coment}'
        phone_book.append('\n' + user_info)

def change_phone_number(i:int):
    bufer = phone_book[i].split(';')
    while True:
        user_answer = int(input('что именно вы хотите изменить? 1 - ФИО. 2 - нимер. 3 - коментарий. 4 - всё: '))
        match user_answer:
            case 1:
                user_info_name = input('Ввидите новые ФИО контакта: ')
                bufer[1] = user_info_name
                phone_book[i] = ';'.join(bufer)
                break
            case 2:
                user_info_phone = input('Ввидите новый номер контакта: ')
                bufer[2] =  user_info_phone
                phone_book[i] = ';'.join(bufer)
                break
            case 3:   
                user_info_coment = input('Ввидите новый коментарий к контакту: ')
                bufer[3] = user_info_coment
                phone_book[i] = ';'.join(bufer)
                break
            case 4:
                user_info_name = input('Ввидите новые ФИО контакта: ')
                user_info_phone = input('Ввидите новый номер контакта: ')
                user_info_coment = input('Ввидите новый коментарий к контакту: ')
                new_user_info = f'{str(len(phone_book) + 1)} ; {user_info_name} ; {user_info_phone} ; {user_info_coment}'
                phone_book[i] = new_user_info
                break
            case _:
                print('неверна выбрана операция!')

def search_phone_number():
    if len(phone_book) == 0:
        print('Вы не открыли файл или файл пуст')
    user_info = input('Ввидите данные для поиска: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(' '.join(phone_book[i].split(';')))
            user_answer = input('Вы ищите этот контакт?(y - да, n - нет): ')
            if user_answer.lower() == 'y' or user_answer.lower() == 'да':
                user_answer = int(input('что именно вы хотите сделать с этим номером? 1 - изменит. 2 - удалить. 3 - выйти: '))
                match user_answer:
                    case 1:
                        change_phone_number(i)
                    case 2:
                        delete_phone_number(i)
                    case 3:
                        break
                    case _:
                        print('неверна выбрана операция!')
                break
    else:
        print('Видемо такого кантакта нет, попробуйте ещё раз.')

def delete_phone_number(i:int):
    print('Вы точно хотите удалить данный кантакт?')
    user_answer = input('Вы точно хотите удалить данный кантакт?(y - да, n - нет): ')
    if user_answer.lower() == 'y' or user_answer.lower() == 'да':
        phone_book.pop(i)