
class ViewPB():
    '''Класс для вывода и ввода информации от пользователя 
    при работе с телефонной книгой'''

    staticmethod
    def menu() -> int:
        '''печать меню и запрос от пользователя выбранного пункта меню'''
        print('''\nГлавное меню:
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Найти контакт
        5. Добавить контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход\n''')
        while True:
            try:
                num = int(input('введите номер операции: '))
                print()
                if 0 < num < 9:
                    return num
                else:
                    print('\nОшибка! Введите число от 1 до 8\n')
            except:
                print('\nИспользуй буквы\n')

    staticmethod
    def print_coment (num: int):
        '''Список сообщений о работе программы'''
        match num:
            case 0:
                message = 'Файл уже был открыт, либо есть несохранёные изменения.'
            case 1:
                message = 'Файл открыт'
            case 2:
                message = 'Файл сохранён'
            case 5:
                message = 'Контакт добавлен'
            case 6:
                message = 'Контакт изменён'
            case 7:
                message = 'Контакт удалён'
        print(message)

    staticmethod
    def opiration_massage(num_opiration: int) -> str:
        '''список предупреждающих сообщений о выполняемых операциях'''
        match num_opiration:
            case 1:
                massage = 'открыть файл'
            case 7:
                massage = 'удалить контакт'
            case 8:
                massage = 'выйти'
        return massage

    staticmethod
    def print_PB(phone_book: list[dict]):
        '''вывод в консоль списка контактов'''
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                f'{contact.get("phone"):<15} '
                f'{contact.get("comment"):<20}')

    staticmethod
    def new_contact_input() ->dict:
        '''Запрос от пользователя новых данных'''
        name = input('Введите имя и фамилию: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        new_contact = {'name': name,
                    'phone': phone,
                    'comment': comment}
        return new_contact

    staticmethod
    def search_phone_number(phone_book: list[dict]):
        '''поиск данных в книге'''
        flag = False
        user_info = input('Ввидите данные для поиска: ')
        print()
        for i, contact in enumerate(phone_book):
            for value in contact.values():
                if user_info in value:
                    print(f'{i+1}. {phone_book[i].get("name"):20} '
                    f'{phone_book[i].get("phone"):<15} '
                    f'{phone_book[i].get("comment"):<20}')
                    flag = True
                    break
        if flag == False:
            print('Такой контакт не найден')

    staticmethod
    def contact_id() -> int:
        '''запрос idшника'''
        index = int(input('введите индекс нужного контакта: '))
        return index

    staticmethod
    def confirm(num_opiration: int) ->bool:
        '''запрос подтверждения о выполнении операции'''
        massage = ViewPB.opiration_massage(num_opiration)
        while True:
            answer = input(f'Вы точно хотите {massage}? (y - да, n - нет): ').strip().lower()
            if answer == 'y' or answer == 'да':
                return True
            elif answer == 'n' or answer == 'нет':
                return False
            else:
                print('Неверный ввод!')

    staticmethod
    def file_dont_open(answer: bool):
        if answer == []:
            print('Телефонная книга пуста или файл не открыт!')

    staticmethod
    def file_dont_save():
        print('Файл не сохранен!!!')

    staticmethod
    def no_changes():
        print('файл не изменялся')

    staticmethod
    def goodbye():
        print('Досвидания')