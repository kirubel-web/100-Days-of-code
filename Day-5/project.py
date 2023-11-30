# password generator
import string
import random

print('Welcome to the PyPassword Generator!')
length_of_pass = int(input('How many letters would you like in \
your password?'))
symbols = int(input('How many symbols would you like?'))
numbers = int(input('How many numbers would you like?'))

letters_letters = list(string.ascii_letters)
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '(', ')']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password_string = []

for char in range(1, length_of_pass + 1):
    password_string.append(random.choice(letters_letters))

for char in range(1, symbols + 1):
    password_string.append(random.choice(symbols_list))

for char in range(1, numbers + 1):
    password_string.append(random.choice(numbers_list))


random.shuffle(password_string)

final = ''.join(password_string)
print(final)
