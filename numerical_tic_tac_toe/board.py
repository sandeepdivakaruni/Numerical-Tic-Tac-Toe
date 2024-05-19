from itertools import product


class Board:
    def __init__(self, length=4):
        """Initializes the board with a specified length.
           The length must be a perfect square. Zeroes represent empty spaces."""
        self.length = length
        self.board = [0 for _ in range(pow(self.length, 2))]
        self.num_columns = self.num_rows = int(self.length)
        self.all_numbers = range(1, len(self.board) + 1)
        self.winning_sum = int(sum(self.all_numbers) / self.length)

    def __str__(self):
        out = ''
        for i, val in enumerate(self.board):
            out += '{:2} '.format(val)
            if ((i + 1) % self.num_columns) == 0:
                out += '\n'
        return out

    @property
    def has_winning_sum(self):
        """Returns True if the values of a row, column, or diagonal sum to the winning sum value"""
        return self.row_has_winning_sum or self.column_has_winning_sum or self.diagonal_has_winning_sum

    @property
    def rows(self):
        return [self.board[i * self.num_columns:(i + 1) * self.num_columns] for i in range(self.num_columns)]

    @property
    def columns(self):
        return [self.board[i::self.num_rows] for i in range(self.num_rows)]

    @property
    def row_has_winning_sum(self):
        for row in self.rows:
            if sum([val for val in row if val != 0]) == self.winning_sum and len([val for val in row if val != 0]) == self.length:
                return True
        return False

    @property
    def column_has_winning_sum(self):
        for column in self.columns:
            if sum([val for val in column if val != 0]) == self.winning_sum and len([val for val in column if val != 0]) == self.length:
                return True
        return False

    @property
    def major_diagonal(self):
        return self.board[::self.num_columns + 1]

    @property
    def minor_diagonal(self):
        return self.board[self.num_columns - 1:len(self.board) - self.num_columns + 1:self.num_columns - 1]

    @property
    def diagonals(self):
        return [self.major_diagonal, self.minor_diagonal]

    @property
    def diagonal_has_winning_sum(self):
        for diagonal in self.diagonals:
            if sum([val for val in diagonal if val != 0]) == self.winning_sum and len([val for val in diagonal if val != 0]) == self.length:
                return True
        return False

    @property
    def is_maxes_turn(self):
        even, odd = self.count_even_odd(self.board)
        return even == odd

    @staticmethod
    def count_even_odd(vector):
        """Counts the number of even and odd numbers in a vector. Zeroes are not counted."""
        even_cnt = odd_cnt = 0
        for val in vector:
            if val == 0:
                continue
            if val % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return even_cnt, odd_cnt

    @property
    def all_possible_move_locations(self):
        """Returns all indexes that contain the value zero"""
        return [i for i, val in enumerate(self.board) if val == 0]

    @property
    def all_possible_move_values(self):
        """Returns all possible values that can be placed on the board"""
        used_values = [val for val in self.board if val != 0]
        return [val for val in self.all_numbers if val not in used_values]

    @property
    def all_possible_moves(self):
        """Returns all possible moves. A move is a tuple. The move[0] is the location
           (index) of the move and move[1] is the value."""
        return product(self.all_possible_move_locations, self.all_possible_move_values)

    @property
    def all_odd_moves(self):
        """Returns all possible odd moves. A move is a tuple. The move[0] is the location
           (index) of the move and move[1] is the value."""
        return [move for move in self.all_possible_moves if move[1] % 2 == 1]

    @property
    def all_even_moves(self):
        """Returns all possible even moves. A move is a tuple. The move[0] is the location
           (index) of the move and move[1] is the value."""
        return [move for move in self.all_possible_moves if move[1] % 2 == 0]

    @property
    def utility(self):
        """Returns 100 if there is a winning sum else returns 0"""
        return 100 if self.has_winning_sum else 0

    def equal_even_odd(self, vector):
        even, odd = self.count_even_odd(vector)
        return even == odd
