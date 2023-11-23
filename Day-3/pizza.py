#

print("Welcome to python pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price = price + 2
    else:
        pass
    if extra_cheese == "Y":
        price = price + 1
if size == "M":
    price = 20
    if add_pepperoni == "Y":
        price = price + 3
    else:
        pass
    if extra_cheese == "Y":
        price = price + 1
if size == "L":
    price = 25
    if add_pepperoni == "Y":
        price = price + 3
    else:
        pass
    if extra_cheese == "Y":
        price = price + 1
print(f'Your final bill is: ${price}.')
