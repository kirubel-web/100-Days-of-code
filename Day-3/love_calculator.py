# program that tests the compatibility betweeen two people

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

full_name = name1 + name2

t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')

total_1 = t + r + u + e

l = full_name.count('l') # noqa
o = full_name.count('o')
v = full_name.count('v')
e = full_name.count('e')

total_2 = l + o + v + e

total = str(total_1) + str(total_2)

if (int(total) < 10) or (int(total) > 90):
    print(f'Your score is {total}, you go together like coke and mentos.')
elif 40 < int(total) < 50:
    print(f'Your score is {total}, you are alright together.')
else:
    print(f'Your score is {total}')
