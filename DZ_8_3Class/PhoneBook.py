from copy import deepcopy

class PhoneBook():
    '''Клас для работты с Телефонной книгой, 
    хранит в себе все функции по изменению телефонной книги 
    и копию самой телефонной книги с внесёнными изменениями 
    в переменной(буфере)'''

    def __init__(self, path = 'pb.txt'):
        self.path = path
        self.phones_book = []
        self.new_pb = []

    def open_file(self):
        '''открытее файла и запись его содержимого в переменную'''
        self.phones_book = []
        with open(self.path,'r',encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {}
                new_contact['name'] = new[0]
                new_contact['phone'] = new[1]
                new_contact['comment'] = new[2]
                self.phones_book.append(new_contact)
            self.new_pb = deepcopy(self.phones_book)

    def seve_file(self):
        '''запись изменнённой переменной в файл'''
        data = []
        for contact in self.phones_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.new_pb = deepcopy(self.phones_book)

    def get(self):
        return self.phones_book

    def add(self, new_contact: dict):
        self.phones_book.append(new_contact)

    def change_contact(self, index: int, contact: dict):
        '''Замена контакта'''
        for key, value in contact.items():
            if value == '':
                contact[key] = self.phones_book[index-1].get(key)
        self.phones_book.pop(index-1)
        self.phones_book.insert(index-1, contact)

    def delite_contact(self, index: int):
        self.phones_book.pop(index-1)

    def comparison(self) ->bool:
        '''проверка на наличее не сохранёных изменений'''
        if self.new_pb == self.phones_book:
            return False
        return True

    def file_dont_open(self) ->bool:
        '''проверка на открытее файла'''
        if self.phones_book == []:
            return True
        return False