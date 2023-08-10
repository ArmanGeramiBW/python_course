import random
numbers = []
while True:
 n = int(input('enter number:'))
 while len(numbers) < n:
    number = random.randint(1,100)
    if number in numbers:
        continue
    else:
        numbers.append(number)

 print(numbers)
 break



#or

import random

# Get the length of the list from the user
x = int(input("How many numbers do you want?:"))

# Define the range of random numbers
start = 0
end = 100

# Generate a list of random, non-repeating numbers
numbers_list = random.sample(range(start, end), x)

# Print the list of numbers
print("Here is your list of random, non-repeating numbers:")
print(numbers_list)
