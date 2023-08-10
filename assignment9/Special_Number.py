# Initialize a variable c to store the sum of divisors
c = 0
# Get an integer input from the user and store it in number
number = int(input("Enter Your Number:"))

# Loop through all the numbers from 1 to number-1
for i in range(1,number):
    # Check if number is divisible by i
    if number % i == 0:
        # Add i to c
        c += i
    
# ]f c is equal to number
if c == number:
    # Print a message that the number is perfect
	print("Yes this is a perfect number.")
    
else:
    # Print a message that the number is not perfect
	print("No this isn't a perfect number.")
