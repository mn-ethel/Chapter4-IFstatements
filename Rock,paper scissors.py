import random
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def rock_paper_scissors_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors! Best of 5 rounds.\n")

    # Play 5 rounds
    for round_num in range(1, 6):
        print(f"Round {round_num}:")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        while user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            user_choice = input("Enter rock, paper, or scissors: ").lower()

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!\n")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!\n")
            computer_score += 1
        else:
            print("This round is a tie!\n")

    print("Final Scores:")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the game! ")
    elif computer_score > user_score:
        print("Oops! The computer won the game.")
    else:
        print("It's a tie! Well played!")





