from games import *

ttt = TicTacToe()
ttt.display(ttt.initial)

my_state = GameState(
    to_move = 'X',
    utility = 0,
    board = {(1,1): 'X', (1,2): 'O', (1,3): 'X',
             (2,1): 'O',             (2,3): 'O',
             (3,1): 'X',
            },
    moves = [(2,2), (3,2), (3,3)]
    )

ttt.set_state(my_state)
ttt.display(ttt.initial)

print(ttt.play_game_custom(alphabeta_player, alphabeta_player))
