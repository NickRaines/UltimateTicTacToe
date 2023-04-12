from uttt_main import UTTT
import random
import time
import copy

class Player:
    def __init__(self, index=0):
        self.index = index

    def make_move(self, state: UTTT):
        return


class RandomPlayer(Player):
    def __init__(self, index=0):
        self.index = index

    def make_move(self, state: UTTT):
        start_time = time.perf_counter()

        random_index = random.randrange(len(state.valid_moves))
        board_ai = state.valid_moves[random_index][0]
        cell_ai = state.valid_moves[random_index][1]

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        state.make_move(board_ai, cell_ai)
        print("Random AI has made the move (", board_ai,", ", cell_ai,") in ", elapsed_time, " seconds")


class UserPlayer(Player):
    def make_move(self, state: UTTT):
        input_str = input("Make Your Move: ")
        board, cell = map(int, input_str.split())
        if(state.make_move(board, cell) is False):
            print("That move was invalid, please make a valid move")

class MonteCarloPlayer(Player):
    def __init__(self, index=0):
        self.index = index

    def make_move(self, state: UTTT):
        start_time = time.perf_counter()

        simulation_scores = MonteCarloPlayer.simulate_games(state, 25)
        index_choice = simulation_scores.index(max(simulation_scores))
        board_ai = state.valid_moves[index_choice][0]
        cell_ai = state.valid_moves[index_choice][1]

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        state.make_move(board_ai, cell_ai)
        print("Monte Carlo AI has made the move (", board_ai,", ", cell_ai,") in ", elapsed_time, " seconds")

    def simulate_games(state: UTTT, simulation_count: int):
        possible_moves = state.valid_moves

        games = [0] * len(possible_moves)
        for i in range(len(possible_moves)):
            for _ in range(simulation_count):
                temp_game = state.generate_next_uttt(possible_moves[i][0], possible_moves[i][1])
                games[i] += MonteCarloPlayer.run_simulation(temp_game)
        return games

    def run_simulation(temp_state: UTTT):
        player_id = 3 - temp_state.player_turn
        while temp_state.winner == 0:
            random_index = random.randrange(len(temp_state.valid_moves))
            board_ai = temp_state.valid_moves[random_index][0]
            cell_ai = temp_state.valid_moves[random_index][1]
            temp_state.make_move(board_ai, cell_ai)
        return 1 if player_id == temp_state.winner else 0 if temp_state.winner == -1 else -1
    