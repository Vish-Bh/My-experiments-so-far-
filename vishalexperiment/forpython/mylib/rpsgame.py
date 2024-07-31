import random
def game():
    try:
        choices=['rock', 'paper', 'scissors']
        computer=random.choice(choices)
        player=input("Enter your choice: Rock, Paper, Scissors: ").lower()
        print(f"COMPUTER's choice {computer} VS PLAYERS's choice {player} ")
        if player==computer:
            print("It's a tie")
        elif player=='rock' and computer=='paper' or player=='paper' and computer=='scissors':
            print("You lose")
        elif player=='paper' and computer=='rock' or player=='rock' and  computer=='scissors':
            print("You win")
        else :
            print('Invalid input')
    except:
        print('IDK HOW U DID THIS')