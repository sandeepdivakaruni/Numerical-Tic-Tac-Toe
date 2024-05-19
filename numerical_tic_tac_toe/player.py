from .search import iterative_deepening_alphabeta
from copy import deepcopy


class Player:
    def __init__(self, is_human, is_max=False):
        self.is_human = is_human
        self.is_max = is_max

    def all_legal_moves(self, board):
        """Return all legal moves for the player based on whether they are max or min."""
        return board.all_odd_moves if self.is_max else board.all_even_moves

    def all_legal_move_locations(self, board):
        """Return all legal move locations for the player based on whether they are max or min."""
        return {move[0] for move in (board.all_odd_moves if self.is_max else board.all_even_moves)}

    def all_legal_move_values(self, board):
        """Return all legal move values for the player based on whether they are max or min."""
        return {move[1] for move in (board.all_odd_moves if self.is_max else board.all_even_moves)}

    @staticmethod
    def perform_move(move_location, move_value, board):
        """Perform a move on the board and return the new board state."""
        new_board = deepcopy(board)
        new_board.board[move_location] = move_value
        return new_board

    def get_move(self, board):
        """Get the next move for the player. If the player is human, prompt for input."""
        return self.get_move_from_user(board) if self.is_human else iterative_deepening_alphabeta(board)

    def get_move_from_user(self, board):
        """Prompt the human player to enter a move location and value."""
        move_location = self._get_valid_input(
            'Enter move location {}: '.format(self.all_legal_move_locations(board)),
            self.all_legal_move_locations(board)
        )
        move_value = self._get_valid_input(
            'Enter move value {}: '.format(self.all_legal_move_values(board)),
            self.all_legal_move_values(board)
        )
        return move_location, move_value

    @staticmethod
    def _get_valid_input(prompt, valid_options):
        """Helper method to prompt for and validate user input."""
        while True:
            try:
                value = int(input(prompt))
                if value in valid_options:
                    return value
                else:
                    print('Not a valid option')
            except ValueError:
                print('Not a valid input')

    def print_all_legal_moves(self, board):
        """Print all legal moves for the player."""
        print('All moves:')
        for i, move in enumerate(self.all_legal_moves(board)):
            if i % 5 == 0 and i != 0:
                print()
            print('{} '.format(move), end='')
        print()
