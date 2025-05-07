import random

def get_user_choice():
    """Prompt user for their choice and validate input."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    return "computer"

def play_game():
    """Main game function to handle game flow and score tracking."""
    user_score = 0
    computer_score = 0
    
    print("\n=== Welcome to Rock, Paper, Scissors! ===")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")
    
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determine and display result
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Display scores
        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")
        
        # Play again?
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    # Final score
    print("\n=== Game Over ===")
    print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations, you won the match!")
    elif computer_score > user_score:
        print("Computer won the match. Better luck next time!")
    else:
        print("The match ended in a tie!")

# Start the game
if __name__ == "__main__":
    play_game()