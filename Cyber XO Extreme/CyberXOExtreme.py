# Cyber XO Extreme
# Version 2.7
# By << Neorevn >>
import random
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

board = [' ' for _ in range(9)]

def define_colored_symbol(symbol):
    if symbol == 'X':
        return f"{Fore.LIGHTBLUE_EX}{symbol}{Style.RESET_ALL}"
    if symbol == 'O':
        return f"{Fore.GREEN}{symbol}{Style.RESET_ALL}"
    return ' '

def print_board(prediction_index=None):
    print("\nGame Board:       Input Guide:")
    for i in range(3):
        row_symbols = []
        for j in range(i * 3, (i + 1) * 3):
            if j == prediction_index:
                row_symbols.append(f"{Fore.YELLOW}*{Style.RESET_ALL}")
            else:
                row_symbols.append(define_colored_symbol(board[j]))
        row_board = f"| {' | '.join(row_symbols)} |"
        row_guide = f"| {' | '.join(str(j) for j in range(i*3 + 1, i*3 + 4))} |"
        print(f"{row_board}     {row_guide}")
        if i < 2:
            print("-" * 13 + "     " + "-" * 13)

def player_selection(player_name):
    while True:
        mode_input = input(f"{player_name}, do you want to play against {Fore.LIGHTYELLOW_EX}Skynet{Style.RESET_ALL}? (yes/no): ").strip().lower()
        if mode_input in ['yes', 'no']:
            game_mode = 'computer' if mode_input == 'yes' else 'human'
            break
        else:
            print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please enter 'yes' or 'no'.")

    while True:
        player_symbol = input(f"Hell Yeah {player_name}, choose your symbol ({Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}): ").upper()
        if player_symbol in ['X', 'O']:
            return player_symbol, game_mode
        print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please choose {Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}.")

def computer_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie():
    return ' ' not in board

def predict_winning_move(board, player):
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            is_winner = check_winner(player)
            board[i] = ' '
            if is_winner:
                return i
    return None


def main():
    print(f"Welcome to {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Cyber XO Extreme{Style.RESET_ALL} by {Fore.LIGHTGREEN_EX}Neorevn{Style.RESET_ALL}")
    player_name = input("Enter your name: ").strip().title()
    
    while True:
        global board
        board = [' ' for _ in range(9)]

        player_symbol, game_mode = player_selection(player_name)
        computer_symbol = 'O' if player_symbol == 'X' else 'X'
        current_player = 'X'

        print(f"\n{define_colored_symbol(current_player)} will go first.")
        time.sleep(1.5)
        print_board()

        while True:
            if game_mode == 'computer' and current_player == computer_symbol:
                print(f"{Fore.LIGHTYELLOW_EX}Skynet is thinking... {Style.RESET_ALL}({define_colored_symbol(current_player)})...")
                time.sleep(1)
                position = computer_move(board)
            else:
                while True:
                    try:
                        move_input = input(f"{player_name} ({define_colored_symbol(current_player)}), it's your turn. Make your move (1-9): ")
                        position = int(move_input) - 1

                        if 0 <= position < 9 and board[position] == ' ':
                            break
                        else:
                            print(f"{Fore.RED}<<ERROR:>> Glitch detected. That spot is taken or out of bounds. Please try again.")
                    except ValueError:
                        print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please enter a number.")

            board[position] = current_player
            print_board()

            if check_winner(current_player):
                if game_mode == 'computer' and current_player == computer_symbol:
                    print(f"{Fore.LIGHTYELLOW_EX}Skynet{Style.RESET_ALL} wins! Better be back, {player_name}.")
                else:
                    print(f"GG {player_name} ({define_colored_symbol(current_player)}), you win!")
                break

            if check_tie():
                print(f"It's a tie, {player_name}!")
                break
            
            current_player = computer_symbol if current_player == player_symbol else player_symbol
            
            winning_move_index = predict_winning_move(board, current_player)
            if winning_move_index is not None:
                print(f"\n{Fore.LIGHTYELLOW_EX}Skynet{Style.RESET_ALL} predicts a winning move for {define_colored_symbol(current_player)} on the next turn!")
                print_board(prediction_index=winning_move_index)

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"Thanks for playing {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Cyber XO Extreme{Style.RESET_ALL}, {player_name}! Sayonara!")
            break

main()
