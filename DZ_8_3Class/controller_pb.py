from view_pb import ViewPB as view
from PhoneBook import PhoneBook

pb = PhoneBook()

def start():
    while True:
        choise = view.menu()
        match choise:
            case 1:
                if pb.file_dont_open() and not pb.comparison():
                    pb.open_file()
                    view.print_coment(choise)
                else:
                    view.print_coment(choise-1)
                    if view.confirm(choise):
                        pb.open_file()
                        view.print_coment(choise)
            case 2:
                if pb.comparison():
                    pb.seve_file()
                    view.print_coment(choise)
                else:
                    view.no_changes()
            case 3:
                get_pb = pb.get()
                answer = pb.file_dont_open()
                if answer:
                    view.file_dont_open(answer)
                else:
                    view.print_PB(get_pb)
            case 4:
                get_pb = pb.get()
                answer = pb.file_dont_open()
                if answer:
                    view.file_dont_open(answer)
                else:
                    view.search_phone_number(get_pb)
            case 5:
                new = view.new_contact_input()
                pb.add(new)
                view.print_coment(choise)
            case 6:
                get_pb = pb.get()
                answer = pb.file_dont_open()
                if answer:
                    view.file_dont_open(answer)
                else:
                    view.search_phone_number(get_pb)
                    ind = view.contact_id()
                    new = view.new_contact_input()
                    pb.change_contact(ind, new)
                    view.print_coment(choise)
            case 7:
                get_pb = pb.get()
                answer = pb.file_dont_open()
                if answer:
                    view.file_dont_open(answer)
                else:
                    view.search_phone_number(get_pb)
                    ind = view.contact_id()
                    if view.confirm(choise):
                        pb.delite_contact(ind)
                        view.print_coment(choise)
            case 8:
                if pb.comparison():
                    view.file_dont_save()
                    if view.confirm(choise):
                        view.goodbye()
                        break
                else:
                    view.goodbye()
                    break
            