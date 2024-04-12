import random


def roll_dice():
    # Simulates rolling a dice and returns the result.
    return random.randint(1, 6)


def play_game():
    # Plays the dice game.
    print("Welcome to the Dice Game!")
    ready = input("Are you ready to play? (yes/no): ")

    if ready.lower() != "yes":
        print("Maybe next time!")
        return

    user_name = input("Enter your name: ")

    user_score = 0
    computer_score = 0

    while user_score <= 30 and computer_score <= 30:
        input("Press Enter to roll the dice...")

        user_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"{user_name} rolled: {user_roll}")
        print("Computer rolled:", computer_roll)

        if user_roll > computer_roll:
            print(f"{user_name} wins this round!")
            user_score += user_roll
        elif user_roll < computer_roll:
            print("Computer wins this round!")
            computer_score += computer_roll
        else:
            print("It's a tie!")

        print(f"{user_name} score: {user_score}")
        print("Computer score:", computer_score)

    if user_score > computer_score:
        print(f"Congratulations, {user_name}! You win!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")


# Start the game
play_game()
