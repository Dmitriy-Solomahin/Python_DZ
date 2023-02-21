from classes.board import Board
from classes.bot import Bot

game = Board()
bot1 = Bot('Василий')
bot2 = Bot('Геннадий')

def game_over():
    if message := game.check_win():
        game.draw()
        print(message)
        exit()

def bot_move(bot):
    
    game.draw()
    move = int(input('Куда будете ходить: '))
    # print(f'Ходит {bot.name}')
    game.move(move)
    game_over()
    game.switch_mark()

    game.move(bot.move(game) + 1)
    game_over()
    game.switch_mark()
    

while True:
    bot_move(bot1)
    bot_move(bot2)