from uttt_main import UTTT
import player
import sys

def game_loop(player1, player2, printing):
    game = UTTT()
    while game.winner == 0:
        if game.player_turn == 1:
            player1.make_move(game)
        else:
            player2.make_move(game)
        if printing:
            game.print_board()
            print("\nValid Moves: ", game.valid_moves)
    
    if game.winner == -1:
        print("\nIt's a Tie!")
    else:
        print("\nPlayer ", game.winner, " Won!")
    return game.winner
    
def create_players(player1, player2):
    ret = []
    for p in [player1, player2]:
        if p == 'random':
            ret.append(player.RandomPlayer())
        elif p == 'player':
            ret.append(player.UserPlayer())
        elif p == 'monte-carlo':
            ret.append(player.MonteCarloPlayer())
    return ret
if __name__ == "__main__":
    # run this file with 2 arguments to select the agent type of the first and second player
    # options are:
    #   player -> human player, will input commands to the command line on their turn
    #   random -> random AI agent. Will randomly select a legal move on its turn
    #   monte-carlo -> monte carlo decision tree AI agent. Will run random simulations to determine its next move on its turn
    #

    if len(sys.argv) == 3:
        p1 = sys.argv[1]
        p2 = sys.argv[2]
    else:
        p1 = 'random'
        p2 = 'random'
    player1, player2 = create_players(p1, p2)
    print('When making your moves input two integers seperated by a space (ie. "1 2")')

    winner_dict = {-1: 0, 1: 0, 2: 0}

    for i in range(0, 100):
        winner_dict[game_loop(player1, player2, False)] += 1
    
    print(winner_dict)
