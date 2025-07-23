# Guessing Game - Jessie Sebastian

import random

def generate_random_number(): # to generate the secret number
    return random.randint(1, 100)
def get_user_guess(): # to save the users guess
    while True: # loop until user gives valid guess
        try:
            guess = int(input('Enter your guess (1-100): '))
            if guess >= 1 and guess <= 100: # checks if the number is > 1 and < 100
                return guess
            else:
                print('Enter a valid number: ')
        except ValueError:
            print('Invalid input, enter a whole number: ')

def play_guessing_game(): # to play the game
    secret_number = generate_random_number()
    attempts = 0
    while True: # to track the number attempts and to give clues to the player if the number is higher/lower
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number: # checks if the number is higher/lower to give appropriate response
            print('The secret number is higher')
        elif guess > secret_number:
            print('The secret number is lower')
        else: # checks if the number is correct and then displays the number of attempts it took
            print(f'Correct, it took you {attempts} attempts')
            break

def game_loop(): # to run the game
    while True: # asks if user wants to play again and outputs proper response
        play_guessing_game()
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again == 'no': # checks if user doesn't want to play again and then stops the game
            print('Thanks for playing')
            break

if __name__ == "__main__": # states the function
    game_loop()
