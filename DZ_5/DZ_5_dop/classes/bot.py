import random

from .board import Board

class Bot:

    def __init__(self, name: str):
        self.name = name
        self.first = True

    def move(self, board: Board):
        if self.first:
            self.first = False
            if board.get()[4].isdigit():
                return 4
            else:
                while True:
                    cell = random.choice([0,2,6,8])
                    if board.get()[cell].isdigit():
                        return cell
        else:
            bot_win = self.check_prewin(board, board.mark)
            if bot_win:
                return bot_win
            enemy_win = self.check_prewin(board, board.enemy_mark())
            if enemy_win:
                return enemy_win
            while True:
                turn = random.randint(0, 8)
                if board.get()[turn].isdigit():
                    return turn


    @staticmethod
    def check_prewin(board: Board, mark: str):
        for option in Board.WIN_COND:
            if board.get()[option[0]] == board.get()[option[1]] == mark and board.get()[option[2]].isdigit():
                return option[2]
            elif board.get()[option[1]] == board.get()[option[2]] == mark and board.get()[option[0]].isdigit():
                return option[0]
            elif board.get()[option[0]] == board.get()[option[2]] == mark and board.get()[option[1]].isdigit():
                return option[1]