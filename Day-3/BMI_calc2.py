# program that interprets the Body Mass Index

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = float(height)
weight = float(weight)
bmi = weight / (height ** 2)

if bmi > 35:
    print('clinically obese')
elif 30 < bmi <= 35:
    print('obese')
elif 25 < bmi <= 30:
    print('overweight')
elif 18.5 <= bmi <= 25:
    print('normal weight')
elif bmi < 18.5:
    print('underweight')

