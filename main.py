from numerical_tic_tac_toe.board import Board
from numerical_tic_tac_toe.player import Player


def main():
    human_vs_ai = prompt_user_for_game_type()

    if human_vs_ai:
        human_player_first = prompt_user_for_play_order()
        players = create_players(human_player_first)
    else:
        players = [Player(is_human=0, is_max=1), Player(is_human=0, is_max=0)]

    max_, min_ = get_max_and_min(players)
    board = Board(4)

    print(board)

    while True:
        max_move = max_.get_move(board)
        board = max_.perform_move(*max_move, board)
        print(board)
        if board.has_winning_sum:
            print('Max wins!')
            break
        if len(list(board.all_possible_moves)) == 0:
            print('Draw!')
            break
        if not human_vs_ai:
            input('Press enter to continue...')

        min_move = min_.get_move(board)
        board = min_.perform_move(*min_move, board)
        print(board)
        if board.has_winning_sum:
            print('Min wins!')
            break
        if len(list(board.all_possible_moves)) == 0:
            print('Draw!')
            break
        if not human_vs_ai:
            input('Press enter to continue...')


def prompt_user_for_game_type():
    while True:
        human_vs_ai = input('Would you like to play against an AI [Y/n]?: ').strip().lower()
        if human_vs_ai in {'', 'y', 'n'}:
            return human_vs_ai != 'n'


def prompt_user_for_play_order():
    while True:
        human_player_first = input('Would you like to go first [Y/n]?: ').strip().lower()
        if human_player_first in {'', 'y', 'n'}:
            return human_player_first != 'n'


def create_players(human_player_first):
    if human_player_first:
        human_player = Player(is_human=1, is_max=1)
        ai_player = Player(is_human=0, is_max=0)
    else:
        human_player = Player(is_human=1, is_max=0)
        ai_player = Player(is_human=0, is_max=1)
    return [human_player, ai_player]


def get_max_and_min(players):
    max_player = next(player for player in players if player.is_max)
    min_player = next(player for player in players if not player.is_max)
    return max_player, min_player


if __name__ == '__main__':
    main()
