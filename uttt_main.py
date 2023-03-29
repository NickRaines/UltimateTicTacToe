class UTTT:
    def __init__(self):
        """
        Initializing the UTTT variable to the default settings

        """
        self.game_grid = [[0] * 9 for _ in range(9)]
        self.active_board = None
        self.winner = 0
        self.player_turn = 1
        # self.valid_moves = get_valid_moves()
        # Thought about calculating valid_moves for the next move after every move and storing in UTTT object

    def __init__(self, game_grid, active_board, winner, player_turn):
        """
        Initializing the UTTT variable given each variable

        """
        self.game_grid = game_grid
        self.active_board = active_board
        self.winner = winner
        self.player_turn = player_turn

    def get_valid_moves(self):
        """
        Returns all valid moves the player can make on their next move taking into account the active board (None if all are active) and which spaces have already been filled

        Args:
            None

        Returns:
            Array of Tuples: Returns an array of tuples (board, cell) of all legal moves the player can make

        """
        
        valid_moves = []
        if self.active_board is None:
            for board in range(len(self.game_grid)):
                for cell in range(9):
                    if self.game_grid[board][cell] == 0:
                        valid_moves.append((board, cell))
        else:
            for cell in range(9):
                if self.game_grid[self.active_board][cell] == 0:
                    valid_moves.append((self.active_board, cell))
        return valid_moves

    def make_move(self, board, cell, valid_moves):
        """
        Updates the UTTT object according to the move made

        Args:
            board (int) : The board number the player is making the move on
            cell (int) : The cell in the board the player is making the move on
            valid_moves (array of (int, int) tuples) : An array of all valid (board, cell) moves

        Returns:
            Boolean: Returns true if the move is valid and false otherwise

        """
        if (board, cell) in valid_moves:
            self.game_grid[board][cell] = self.player_turn
            if self.check_win(board, self.player_turn):
                self.winner = self.player_turn
            # make the current board the same as the cell if that board has any free spaces, otherwise place no restriction
            self.active_board = cell if 0 in self.game_grid[cell] else None
            self.player_turn = 3 - self.player_turn
            return True
        return False
    

    # This assume the move you are making is valid and not take in valid_moves as an input. Therefore the validity of the move MUST be checked before the function is called
    # If it is better for this to be changed to self validate the moves, how should I handle an invalid move?
    def generate_next_uttt(self, board, cell, valid_moves):
        """
        Generates the next UTTT object given that the 

        Args:
            board (int) : The board number the player is making the move on
            cell (int) : The cell in the board the player is making the move on
            valid_moves (array of (int, int) tuples) : An array of all valid (board, cell) moves

        Returns:
            UTTT: The new UTTT generated from the given move

        """
        next_game_state = UTTT(self.game_grid.copy(), self.active_board, self.winner, self.player_turn)
        next_game_state.make_move(board, cell, valid_moves)
        return next_game_state

    def check_win(self, board, player):
        """
        Checks to see if a given player has won the given board (therefore winning them the game)

        Args:
            board (int) : The board that the player may have won
            player (int) : The player that you are checking if they won

        Returns:
            bool: Returns true if the given player has won the board and false otherwise

        """
        # I was thinking about adding this variable: winning_combinations = [{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]
        # and using that to short hand the return statement but couldn't find a way
        b = self.game_grid[board]
        return ((b[0] == b[1] == b[2] == player) or
                (b[3] == b[4] == b[5] == player) or
                (b[6] == b[7] == b[8] == player) or
                (b[0] == b[3] == b[6] == player) or
                (b[1] == b[4] == b[7] == player) or
                (b[2] == b[5] == b[8] == player) or
                (b[0] == b[4] == b[8] == player) or
                (b[2] == b[4] == b[6] == player))
    


    #commenting convention I will be using for functions
    """
        Description

        Args:
            variable_name (variable_type) : description

        Returns:
            return_type: description

    """