import random

def hangman():
    LIST_OF_WORDS = ['brick', 'glent', 'jumpy', 'vozhd', 'waqfs', 'abuzz', 'bezzy', 'dizzy', 'fizzy', 'jazzy', 'muzzy', 'pozzy', 'whizz', 'zazen', 'docks', 'dodge', 'dodgy', 'doggy', 'dogma', 'doing', 'dolce', 'dolls', 'dolly', 'donna', 'donor', 'donut']
    print(f'The list of words is {LIST_OF_WORDS}')
    word = random.choice(LIST_OF_WORDS)
    letter_to_guess = len(word)
    print(f'The word is {letter_to_guess} letters long')
    guess = 0
    print(' _ ' * letter_to_guess)
    letter_of_guess = ['_'] * letter_to_guess
    while guess < 3:
        letter_guessed = input('Enter your Guess: \n').lower()
        if len(letter_guessed) > 1:
            print('Please enter only one letter')
            continue
        if letter_guessed in word:
            print('You guessed it right')
            for i, letter in enumerate(word):
                if letter == letter_guessed:
                    letter_of_guess[i] = letter_guessed
                    break
            print(' '.join(letter_of_guess))
            if '_' not in letter_of_guess:
                print('Congratulations, You won :()')
                return
        else:
            guess += 1
            print('You guessed it wrong \n You got ', (3-guess), 'guesses left')
        if guess == 3:
            print('You lost hahahhah :)')
            print('The word was', word)

hangman()