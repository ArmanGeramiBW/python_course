import random
list_numbers = []

num1 = 0

c = 0
while not(num1 == 6):
    list_numbers.append(num1)
    num1 = random.randint(1,6)
    c += 1
    if num1 == 6:
        print(f"round {c}")
        print("You winnnnnn")
    else:
        print(f"round {c} is:")
        print(num1)