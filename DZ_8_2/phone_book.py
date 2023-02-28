from copy import deepcopy

path = 'pb.txt'
phones_book = []
new_pb = []

def open_file():
    global phones_book
    global path
    global new_pb
    with open(path,'r',encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {}
            new_contact['name'] = new[0]
            new_contact['phone'] = new[1]
            new_contact['comment'] = new[2]
            phones_book.append(new_contact)
        new_pb = deepcopy(phones_book)

def seve_file():
    global phones_book
    global path
    global new_pb
    data = []
    for contact in phones_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    new_pb = deepcopy(phones_book)

def get():
    global phones_book
    return phones_book

def add(new_contact: dict):
    global phones_book
    phones_book.append(new_contact)

def change_contact(index: int, contact: dict):
    global phones_book
    phones_book.pop(index-1)
    phones_book.insert(index-1, contact)

def delite_contact(index: int):
    global phones_book
    phones_book.pop(index-1)

def comparison() ->bool:
    global phones_book
    global path
    global new_pb
    if new_pb == phones_book:
        return False
    return True

