# program that works out whether if a given year is a leap year

year = int(input("Which year do you want to check? "))
# solution 1
""" if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
    print('Leap')
else:
    print('Not') """

# solution 2
if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print('leap')
        else:
            print('Not Leap')
    else:
        print('Not Leap')
else:
    print('Not Leap')
