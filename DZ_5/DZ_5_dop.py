def print_pole(dict: dict):
    num = 1
    while num <= 9:
        print(f'{dict[num]} | {dict[num+1]} | {dict[num+2]}')
        print('---------')
        num += 3

cell = {1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9'}

def computer_running(dict: dict, count: int):
    if dict[5] == '5':
        dict[5] = 'O'
    elif dict[5] == 'X':
        if dict[1] == '1' and count == 1:
            dict[1] = 'O'
        elif (dict[3] == '3' or dict[7] == '7') and count == 3:
            if dict[3] == '3':
                dict[3] = 'O'
            else:
                dict[7] = 'O'
        elif (dict[3] == 'O' or dict[7] == 'O') and count == 5:
            if dict[3] == 'O':
                if dict[2] == '2':
                    dict[2] = 'O'
                    game_ower = True
                elif dict[2] == 'X':
                    dict[8] = 'O'
            elif dict[7] == 'O':
                if dict[4] == '4':
                    dict[4] = 'O'
                    game_ower = True
                elif dict[4] == 'X' :
                    dict[6] = 'O'
        if dict[7] == 'O' and (dict[4] =='O' or dict[6] =='O') and count == 7:
            if dict[2] == '2':
                dict[2] = 'O'
            else:
                dict[8] = 'O'
        elif dict[3] == 'O'and (dict[2] =='O' or dict[8] =='O') and count == 7:
            if dict[4] == '4':
                dict[4] = 'O'
            else:
                dict[6] = 'O'
    else:
        print

game_over = False
count = 0
while game_over == False:
    print_pole(cell)

    while True:
        cell_number = int(input("Введите номер ячейки: "))
        if cell[cell_number] == f'{cell_number}':
            cell[cell_number] = 'X'
            break
        else:
            print('неверна выбрана ячейка!')
        

    count += 1
    print_pole(cell)
    print()
    
    if count == 9:
        game_over = True
        print_pole(cell)

    computer_running(cell, count)
    count += 1
    
else:
    print('game over')
