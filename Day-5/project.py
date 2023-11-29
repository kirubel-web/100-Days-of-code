# password generator
import string
import random

print('Welcome to the PyPassword Generator!')
length_of_pass = int(input('How many letters would you like in your password?'))
symbols = input('How many symbols would you like?')
numbers = input('How many numbers would you like?')

letters_letters = list(string.ascii_letters)
symbols_list = list(string.punctuation)
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

password_string = []

for i in random.choices(letters_letters, symbols_list, numbers_list):
    password_string.append(i)
