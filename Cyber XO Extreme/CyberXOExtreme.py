# Cyber XO Extreme
# Version 2.9
# By << Neorevn >>
import random
import time
import subprocess
import sys

def install_dependencies(): # I did use AI here, had no idea where to start - needed it for Colorama
    try:
        import colorama
        from colorama import Fore, Style, init
        init(autoreset=True)
        return Fore, Style  # Return Fore and Style if already installed
    except ImportError:
        print("Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
            import colorama
            from colorama import Fore, Style, init
            init(autoreset=True)
            return Fore, Style  # Return Fore and Style after installation
        except subprocess.CalledProcessError as e:
            print(f"Error installing colorama: {e}")
            return None, None  # Return None values if installation fails
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

Fore, Style = install_dependencies()

if Fore is None or Style is None:
    print("Colorama could not be installed or imported. Exiting.")
    sys.exit()

def define_colored_symbol(symbol): # I like style so had to include this :)
    if symbol == 'X':
        return f"{Fore.LIGHTBLUE_EX}{symbol}{Style.RESET_ALL}"
    if symbol == 'O':
        return f"{Fore.GREEN}{symbol}{Style.RESET_ALL}"
    return ' '

def print_board(board, prediction_index=None): # Started with your board design Hodi, but I wanted to make it look better, as ive said... I like style + a game needs a tutorial
    print("\n Game Board:       Input Guide:")
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

def player_selection(player_name): # The game modes gave me some trouble in the thinking process but made it work
    while True:
        mode_input = input(f"{player_name}, do you want to play against {Fore.LIGHTYELLOW_EX}Skynet{Style.RESET_ALL}? (yes/no): ").strip().lower()
        if mode_input in ['yes', 'no']:
            if mode_input == 'yes':
                game_mode = 'computer'
            else:
                game_mode = 'human'
                return None, game_mode
            break
        else:
            print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please enter 'yes' or 'no'.")
    while True:
        player_symbol = input(f"Hell yeah {player_name}, choose your symbol ({Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}): ").upper()
        if player_symbol in ['X', 'O']:
            return player_symbol, game_mode
        print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please choose {Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}.")

def computer_move(board): # AI Was used for the enumerate class
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None

def check_winner(board,player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie(board):
    return ' ' not in board

def predict_winning_move(board, player): # This was tough... spent a lot of time on it
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            is_winner = check_winner(board,player)
            board[i] = ' '
            if is_winner:
                return i
    return None
def print_scoreboard(player_name, scores, opponent_name): # Thought it was nice to have.. like old games
    print(f"\n--- {Fore.LIGHTMAGENTA_EX}Scoreboard{Style.RESET_ALL} ---")
    print(f"{player_name}: {scores['player']}")
    print(f"{opponent_name}: {scores['opponent']}")

def main():
    print(f"Welcome to {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Cyber XO Extreme{Style.RESET_ALL} by {Fore.LIGHTGREEN_EX}Neorevn{Style.RESET_ALL}")
    player_name = input("Enter your name: ").strip().title()
    while not player_name.isalpha():
        print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please enter a valid name.")
        player_name = input("Enter your name: ").strip().title()
        
    scores = {'player': 0, 'opponent': 0}
    
    while True: # Calls the player_selection function and gets player info and choices and prints the game board
        board = [' ' for _ in range(9)]
        player_symbol, game_mode = player_selection(player_name) 
        if player_symbol is None:
            player2_name = game_mode and input("Enter the name of the second player: ").strip().title()
            while not player2_name.isalpha():
                print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please enter a valid name.")
                player2_name = input("Enter the name of the second player: ").strip().title()
            game_mode = 'human'
            player_symbol = input(f"Hell yeah {player_name}, choose your symbol ({Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}): ").upper()
            while player_symbol not in ['X', 'O']:
                print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please choose {Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}.")
                player_symbol = input(f"Hell yeah {player_name}, choose your symbol ({Fore.LIGHTBLUE_EX}X{Style.RESET_ALL} or {Fore.GREEN}O{Style.RESET_ALL}): ").upper()
            computer_symbol = 'O' if player_symbol == 'X' else 'X'
        else: 
            computer_symbol = 'O' if player_symbol == 'X' else 'X'
            
        if game_mode == 'human':
            opponent_name_display = f"{player2_name}"
        else:
            opponent_name_display = f"{Fore.LIGHTYELLOW_EX}Skynet{Style.RESET_ALL}"
        current_player = 'X'
        print(f"\n{define_colored_symbol(current_player)} will go first.")
        time.sleep(1.5)
        print_board(board)

        while True: # Main game - calls the functions: player_move \ computer_move \ check_winner \ check_tie \ difine_colored_symbol \ print_board \ predict_winning_move
            if game_mode == 'computer' and current_player == computer_symbol:
                print(f"{opponent_name_display} is thinking... ({define_colored_symbol(current_player)})...")
                time.sleep(1)
                position = computer_move(board)
            else:
                while True:
                    try:
                        current_player_name = player_name if current_player == player_symbol else opponent_name_display
                        move_input = input(f"{current_player_name} ({define_colored_symbol(current_player)}), it's your turn. Make your move (1-9): ")
                        position = int(move_input) - 1
                        if 0 <= position < 9 and board[position] == ' ':
                            break
                        else:
                            print(f"{Fore.RED}<<ERROR:>> Glitch detected. That spot is taken or out of bounds. Please try again.")
                    except ValueError:
                        print(f"{Fore.RED}<<ERROR:>> Glitch detected. Please enter a number.")
            board[position] = current_player
            print_board(board)
            time.sleep(1)

            if check_winner(board, current_player):
                if current_player == player_symbol:
                    print(f"GG {player_name} ({define_colored_symbol(current_player)}), you {Fore.WHITE}{Style.BRIGHT}win!")
                    scores['player'] += 1
                else:
                    print(f"{opponent_name_display} {Fore.WHITE}{Style.BRIGHT}wins!{Style.RESET_ALL} Better luck next time, {player_name}.")
                    scores['opponent'] += 1
                break
            if check_tie(board):
                print(f"It's a tie, {player_name}!")
                break

            current_player = computer_symbol if current_player == player_symbol else player_symbol
            
            winning_move_index = predict_winning_move(board, current_player)
            if winning_move_index is not None:
                print(f"\n{Fore.LIGHTYELLOW_EX}Skynet{Style.RESET_ALL} predicts a winning move for {define_colored_symbol(current_player)} on the next turn!")
                print_board(board, prediction_index=winning_move_index)

        print_scoreboard(player_name, scores, opponent_name_display)

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"Thanks for playing {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Cyber XO Extreme{Style.RESET_ALL}, {player_name}! Sayonara!")
            break

main()
