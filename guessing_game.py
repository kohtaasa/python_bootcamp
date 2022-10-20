import random

random_number = random.randint(1,10)
again = 'y'
guess = 0

while again == 'y':
    guess = int(input('Guess a number between 1 and 10: '))
    if guess == random_number:
        print('You guessed it! You won!')
    else:
        while guess != random_number:
            if guess > random_number:
                print('Too high, try again!')
                guess = int(input('Guess a number between 1 and 10: '))
            elif guess < random_number:
                print('Too low, try again!')
                guess = int(input('Guess a number between 1 and 10: '))
    print('You guessed it! You won!')
    again = input('Do you want to keep playing? (y/n) ')