import random

def multiplication_game():

    print("Welcome to the Multiplication Game!\n")
    total_questions = 10

    for question in range(1, total_questions + 1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2


        print(f"Question {question}: {num1} x {num2} = ?", end=" ")


        try:
            user_answer = int(input())  # Input from the user
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        if user_answer == correct_answer:
            print("Right!\n")
        else:
            print(f"Wrong. The answer is {correct_answer}.\n")

    print("Game Over! Great job playing the multiplication game!")



