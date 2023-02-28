import view
import phone_book as pb

def start():
    while True:
        choise = view.menu()
        match choise:
            case 1:
                pb.open_file()
                view.print_coment(choise)
            case 2:
                if pb.comparison():
                    pb.seve_file()
                    view.print_coment(choise)
                else:
                    view.no_changes
            case 3:
                get_pb = pb.get()
                if not view.file_dont_open(get_pb):
                    view.print_PB(get_pb)
            case 4:
                get_pb = pb.get()
                if not view.file_dont_open(get_pb):
                    view.search_phone_number(get_pb)
            case 5:
                new = view.new_contact_input()
                pb.add(new)
            case 6:
                get_pb = pb.get()
                if not view.file_dont_open(get_pb):
                    view.search_phone_number(get_pb)
                    ind = view.contact_id()
                    new = view.new_contact_input()
                    pb.change_contact(ind, new)
                    view.print_coment(choise)
            case 7:
                get_pb = pb.get()
                if not view.file_dont_open(get_pb):
                    view.search_phone_number(get_pb)
                    ind = view.contact_id()
                    if view.confirm('удалить'):
                        pb.delite_contact(ind)
            case 8:
                if pb.comparison():
                    view.file_dont_save()
                    if view.confirm('выйти'):
                        print('Досвидания')
                        break
                else:
                    break
            