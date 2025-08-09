import random

def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors and validates the input.
    """
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """
    Generates a random choice for the computer.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the round based on the game's logic.
    Returns 1 for user win, -1 for computer win, and 0 for a tie.
    """
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        return 0 
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 1 
    else:
        return -1 

def play_game():
    """
    Main function to run the Rock, Paper, Scissors game.
    Includes score tracking and a play-again loop.
    """
    user_score = 0
    computer_score = 0

    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)

        if result == 1:
            print("You win this round!")
            user_score += 1
        elif result == -1:
            print("The computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
            break


if __name__ == "__main__":
    play_game()
