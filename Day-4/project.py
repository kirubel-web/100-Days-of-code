# Rock paper or scissors
import random

player_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2  \
for Scissors.\n')
computer = random.randint(0, 2)
try:
    if int(player_choice) == computer:
        print('Its a Draw')
    elif int(player_choice) >= 3:
        print('Invalid Input Please Try again.')
    elif int(player_choice) == 0 and computer == 1:
        print('You Lose computer Choose paper')
    elif int(player_choice) == 0 and computer == 2:
        print('You Win computer choose scissors')
    elif int(player_choice) == 1 and computer == 0:
        print('You Win computer choose rock')
    elif int(player_choice) == 1 and computer == 3:
        print('You lose computer choose Scissors')
    elif int(player_choice) == 2 and computer == 0:
        print('You lose computer choose Rock')
    elif int(player_choice) == 2 and computer == 1:
        print('You Win computer choose paper')
except ValueError:
    print('Enter A number')
