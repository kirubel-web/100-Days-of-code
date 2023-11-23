# program that tests the compatibility betweeen two people

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

love = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']
i = 0
if i in love and name1:
    i += 1
print(i)