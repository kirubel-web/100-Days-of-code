# program that calculate even numbers

total = 0
for number in range(0, 101, 2):
    total += number

print(f"The sum of even number from 0 - 100 is {total}")