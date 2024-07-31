import random
def hangman():
    list_of_words=['apple', 'banana', 'grapes']
    print(list_of_words)
    word_choice=random.choice(list_of_words)
    print(word_choice)
    letters_to_guess=len(word_choice)
    formated_guessed_word=('_ ' * int(letters_to_guess))
    print(f'A random letter is choicen from the above list can u guess that word?? \n {'_ '*letters_to_guess}')
    lives=3
    while lives!=0:
        guessed_letter=input('Enter : ')
        if len(guessed_letter)!=1:
            print('Enter only a single letter')
        elif guessed_letter in word_choice:
            print('well done u got it right this time')
            for word in word_choice:
                if word==guessed_letter:
                    i=word_choice.index(word)
                    listed_formated_guessed_word=list(formated_guessed_word)
                    listed_formated_guessed_word[i]=guessed_letter
                    final=''.join(listed_formated_guessed_word)
                    print(final)
                    pass
                else:
                    pass
        elif guessed_letter not in word_choice:
            print('You GOt it WRONG HAHA :)')
hangman()
