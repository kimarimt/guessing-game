import random
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print('Guess the number')
    print('I\'m thinking of a number between 1 and 100')
    secret_number = random.randint(1, 100)
    difficulty = input('Choose a difficulty (\'easy\' or \'hard\'): ')
    lives = 5 if difficulty == 'hard' else 10
    clear()

    while True:
        print(f'Number of attempts: {lives}')
        if lives == 0:
            print('You ran out of lives. GAME OVER!')
            break

        try:
            guess = int(input('Make a guess: '))
        except ValueError:
            print('guess must be a number')
            continue

        if guess == secret_number:
            print('You guessed the number!')
            break
        elif guess < secret_number:
            print('Too Low!')
        else:
            print('Too High!')

        lives -= 1
        clear()

    print(f'The number was {secret_number}')


if __name__ == '__main__':
    main()
