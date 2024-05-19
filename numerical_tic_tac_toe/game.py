from copy import deepcopy


class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    @staticmethod
    def actions(state):
        """Return a list of the allowable moves at this point.
        :rtype: list of moves (location, value)
        """
        return state.all_odd_moves if state.is_maxes_turn else state.all_even_moves

    @staticmethod
    def result(state, move):
        """Return the state that results from making a move from a state."""
        if move is None:
            print('empty move')
        location, value = move
        board = deepcopy(state)
        board.board[location] = value
        return board

    @staticmethod
    def utility(state, player):
        """Return the value of this final state to player."""
        return state.utility if player == 'MAX' else -state.utility

    @staticmethod
    def is_terminal(state):
        """Return True if this is a final state for the game."""
        num_moves = len(state.all_odd_moves) if state.is_maxes_turn else len(state.all_even_moves)
        return state.has_winning_sum or num_moves == 0

    @staticmethod
    def to_move(state):
        """Return the player whose move it is in this state."""
        return 'MAX' if state.is_maxes_turn else 'MIN'

    @staticmethod
    def display(state):
        """Print or otherwise display the state."""
        print(state)
