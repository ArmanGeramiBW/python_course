# Create a set
my_set = {"Green", "Blue", "Black", "White", "Red"}

# Get the number of times to repeat the loop
number_of_repetition = int(input("How many times do you want to use?:"))

# Loop through the set functions
for i in range(0, number_of_repetition):
    # Get the method to try
    print("""
1 = add
2 = remove
3 = copy
4 = clear
5 = discard
6 = update
""")
    our_method = int(input("Which method do you want to use?!: "))
    
    # Print the set
    print(my_set)

    # Try the selected method
    if our_method == 1:
        input_str = input("Please write what you want to add to your set: ")
        my_set.add(input_str)
        print("Set:", my_set)
    # Remove something from our set.
    elif our_method == 2:
        input_str = input("Please write what you want to remove from your set: ")
        my_set.remove(input_str)
        print("Set:", my_set)
    # Copy something from our set.
    elif our_method == 3:
        new_set = my_set.copy()
        print("New Set:", new_set)
    # Remove all things in a set.
    elif our_method == 4:
        my_set.clear()
        print("Set:", my_set)
    # Remove something that we want to remove it.
    elif our_method == 5:
        input_str = input("Please write what you want to discard from your set: ")
        my_set.discard(input_str)
        print("Set:", my_set)

    elif our_method == 6:
        input_str = input("Please write what you want to insert into your set: ")
        my_set.update(input_str)
        print("Set:", my_set)

    else:
        print(f"Input should be 1, 2, 3, 4, 5, or 6 not {our_method}")

# End of loop
print("Thank you for using us. See you soon😁😄😉")


