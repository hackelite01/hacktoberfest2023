import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def get_valid_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= 200:
                return guess
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
        except ValueError:
            print("I don't think that's a number. Please enter a valid number.")

def play_game():
    number = random.randint(1, 200)
    guesses_taken = 0
    while guesses_taken < 6:
        guess = get_valid_guess()
        guesses_taken += 1
        if guess < number:
            print("The guess of the number that you have entered is too low.")
        elif guess > number:
            print("The guess of the number that you have entered is too high.")
        else:
            print(f"Good job, {name}! You guessed my number ({number}) in {guesses_taken} guesses!")
            break
    else:
        print(f"Nope. The number I was thinking of was {number}.")

def play_again():
    while True:
        play_again_option = input("Do you want to play again? (yes/no): ").lower()
        if play_again_option in ("yes", "no"):
            return play_again_option
        else:
            print("Please enter 'yes' or 'no'.")

name = ""
playagain = "yes"
while playagain in ("yes", "y"):
    intro()
    play_game()
    playagain = play_again()
