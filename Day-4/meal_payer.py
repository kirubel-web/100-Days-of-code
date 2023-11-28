import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

payer_list = []
for name in names:
    payer_list.append(name)

length_of_list = len(payer_list)

payer = random.randint(0, length_of_list - 1)

print(f'{payer_list[payer]} is going to buy the meal today!')
