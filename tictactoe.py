import random
import time
import sys

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(b):
    win_coords = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for (x, y, z) in win_coords:
        if b[x] == b[y] == b[z] != " ":
            return b[x].upper()
    return None

def play_game():
    board = [" "] * 9
    current_player = "X"
    game_still_going = True
    
    while game_still_going:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter position (0-8): "))
            if board[move] != " ":
                print("Spot taken! Try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Game Over! Player {winner} wins!")
            game_still_going = False
        elif " " not in board:
            print_board(board)
            print("It's a draw!")
            game_still_going = False
        else:
            current_player = "O" if current_player == "X" else "X"
    
    input("\nPress Enter to return to main menu...")
    main_menu()

def play_game_vs_ai():
    board = [" "] * 9
    current_player = "X" 
    game_still_going = True
    
    while game_still_going:
        print_board(board)
        
        if current_player == "X":
            try:
                move = int(input(f"Your turn (0-8): "))
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move or spot taken!")
                    continue
                board[move] = "X"
            except (ValueError, IndexError):
                print("Enter a number 0-8.")
                continue
        else:
            print("Bot is thinking...")
            time.sleep(1.5)
            
            # --- Smarter Bot Logic ---
            available_moves = [i for i, spot in enumerate(board) if spot == " "]
            
            if 4 in available_moves:
                move = 4  # Always take the center if available
            else:
                move = random.choice(available_moves)
                
            board[move] = "O"
            print(f"Bot chose position {move}")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Game Over! {winner} wins!")
            game_still_going = False
        elif " " not in board:
            print_board(board)
            print("It's a draw!")
            game_still_going = False
        else:
            current_player = "O" if current_player == "X" else "X"

    input("\nPress Enter to return to main menu...")
    main_menu()

def main_menu():
    print("\nWelcome to Kachi's Tic-Tac-Toe!")
    print("1. Play Game vs Player")
    print("2. Play Game vs AI(Bot)")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        play_game()
    elif choice == "2":
        play_game_vs_ai()
    elif choice == "3":
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# This is the standard way to start a Python script
if __name__ == "__main__":
    main_menu()