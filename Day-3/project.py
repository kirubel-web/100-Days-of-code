# treasure island

print("Welcome to Treasure Island Your mission is to find the treasure.")
print("Your mission is to find the treasure.")

decision_1 = input('You are at a cross road. left or right.\n').lower()

if decision_1 == 'left':
    print('You come to a lake. There is an island in the middle of the lake. \
Type "wait" to wait for a boat. Type "swim" to swim across.')
    decision_2 = input('\n').lower()
    if decision_2 == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 \
doors. One red, one yellow and one blue. which color do you choose')
        decision_3 = input('\n').lower()
        if decision_3 == 'yellow':
            print('You win')
        elif decision_3 == 'red' or decision_3 == 'blue':
            print('You enter a room of beasts. Game Over.')
    elif decision_2 == 'swim':
        print('Game Over.')
elif decision_1 == 'right':
    print('Game Over.')
else:
    print('Game Over.')
