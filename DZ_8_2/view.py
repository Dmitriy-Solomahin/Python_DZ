

def menu() -> int:
    print('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Найти контакт
    5. Добавить контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        try:
            num = int(input('введите номер операции: '))
            if 0 < num < 9:
                return num
            else:
                print('Ошибка. Введите число от 1 до 8')
        except:
            print('Используй буквы')

def print_coment (num: int):
    match num:
        case 1:
            opiration = 'открыт'
        case 2:
            opiration = 'сохранён'
        case 6:
            opiration = 'изменён'
    print('файл ' + opiration)

def print_PB(phone_book: list[dict]):
    for i, contact in enumerate(phone_book, 1):
        name = contact.get('name')
        phone = contact.get('phone')
        comment = contact.get('comment')
        print(f'{i}. {name:20}{phone:<15}{comment:<20}')

def new_contact_input() ->dict:
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_contact = {'name': name,
                   'phone': phone,
                   'comment': comment}
    return new_contact
        
def search_phone_number(phone_book: list[dict]):
    flag = False
    user_info = input('Ввидите данные для поиска: ')
    for i, contact in enumerate(phone_book):
        for value in contact.values():
            if user_info in value:
                j = phone_book[i]
                name = j.get('name')
                phone = j.get('phone')
                comment =j.get('comment')
                print(f'{i+1}. {name:20}{phone:<15}{comment:<20}')
                flag = True
    if flag == False:
        print('такой контакт не найден')

def contact_id() -> int:
    index = int(input('введите индекс: '))
    return index

def confirm(opiration: str) ->bool:
    while True:
        answer = input(f'Вы точно хотите {opiration}? (y - да, n - нет)')
        if answer.lower() == 'y' or answer.lower() == 'да':
            return True
        elif answer.lower() == 'n' or answer.lower() == 'нет':
            return False
        else:
            print('Неверный ввод!')
            
def file_dont_save():
    print('Файл не сохранен!!!')

def file_dont_open(phone_book: list) ->bool:
    if phone_book == []:
        print('Телефонная книга пуста или файл не открыт!')
        return True
    return False

def no_changes():
    print('файл не изменялся')