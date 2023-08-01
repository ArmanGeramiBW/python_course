import random

def guessing_game():
    low = 0
    high = 100
    count = 0

    while True:
        guess = random.randint(low,high)
        count += 1
        answer = input(f"My guess is {guess}. Is it too high (h), too low (l), or correct (c)? ")
        if answer == "h":
            high = guess - 1 #It means to measure less
        elif answer == "l":
            low = guess + 1 #It means to measure more
        elif answer == "c":
            print(f"I guessed your number in {count} times that you playing with me!")
            break

    print("Thanks for playing!See you soon :)")

guessing_game()
