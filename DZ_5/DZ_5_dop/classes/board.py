class Board:
    WIN_COND =  ((0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6))
    
    def __init__(self):
        self.fields = [str(i) for i in range(1,10)]
        self.mark = 'X'

    def draw(self):
        print(f' {self.fields[0]} │ {self.fields[1]} │ {self.fields[2]} ')
        print('───┼───┼───')
        print(f' {self.fields[3]} │ {self.fields[4]} │ {self.fields[5]} ')
        print('───┼───┼───')
        print(f' {self.fields[6]} │ {self.fields[7]} │ {self.fields[8]} ')
    
    def move(self, cell: int):
        # ['1', '2', 'X', '4', 'X', '6', '7', '8', '9']
        if self.fields[cell - 1].isdigit() and 0 < cell < 10:
            self.fields[cell - 1] = self.mark
        else:
            return False

    def switch_mark(self):
        if self.mark == 'X':
            self.mark = 'O'
        else:
            self.mark = 'X'

    def enemy_mark(self):
        if self.mark == 'X':
            return 'O'
        else:
            return 'X'

    def check_win(self):
        for option in Board.WIN_COND:
            if self.fields[option[0]] == self.fields[option[1]] == self.fields[option[2]]:
                return f'Победа выиграл "{self.mark}"!'
        if all([not i.isdigit() for i in self.fields]):
            return 'Ничья!!!'
        return False

    def get(self):
        return self.fields

    def game_over(self):
        if all([not i.isdigit() for i in self.fields]):
            return True