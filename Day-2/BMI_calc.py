# program that calculates the body mass index

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = float(height)
weight = float(weight)
bmi = weight / (height ** 2)

print(int(bmi))  # or i can use floor division for output
