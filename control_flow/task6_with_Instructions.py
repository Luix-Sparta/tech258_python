import random  # Import the random module

def roll_dice():
    """Simulates rolling a dice and returns the result."""
    return random.randint(1, 6)  # Generate a random number between 1 and 6

def play_game():
    """Plays the dice game."""
    print("Welcome to the Dice Game!")
    ready = input("Are you ready to play? (yes/no): ")

    if ready.lower() != "yes":
        print("Maybe next time!")
        return

    user_name = input("Enter your name: ")

    user_score = 0
    computer_score = 0

    # Keep playing until either user's score or computer's score reaches 30
    while user_score <= 30 and computer_score <= 30:
        input("Press Enter to roll the dice...")

        user_roll = roll_dice()  # Roll the dice for the user
        computer_roll = roll_dice()  # Roll the dice for the computer

        print(f"{user_name} rolled: {user_roll}")
        print("Computer rolled:", computer_roll)

        # Compare the rolls and update scores accordingly
        if user_roll > computer_roll:
            print(f"{user_name} wins this round!")
            user_score += user_roll
        elif user_roll < computer_roll:
            print("Computer wins this round!")
            computer_score += computer_roll
        else:
            print("It's a tie!")

        # Print the current scores
        print(f"{user_name} score: {user_score}")
        print("Computer score:", computer_score)

    # Declare the winner based on scores
    if user_score > computer_score:
        print(f"Congratulations, {user_name}! You win!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()  # Restart the game if the player wants to play again
    else:
        print("Thank you for playing!")

# Start the game
play_game()
