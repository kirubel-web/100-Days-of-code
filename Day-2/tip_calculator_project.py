print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


if tip == 10:
    totall = ((bill * 0.10) + bill) / people
elif tip == 12:
    totall = ((bill * 0.12) + bill) / people
elif tip == 15:
    totall = ((bill * 0.15) + bill) / people

totall = round(totall, 2)  # or __round__(2)
totall = "{:.2f}".format(totall)
print(f'Each person should pay: ${totall}')
