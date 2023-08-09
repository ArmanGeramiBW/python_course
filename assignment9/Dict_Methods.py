Dictionary = {
"Brand": "Skynet",
"Model": "killer of humans T800",         
"Year of construction": "2074"}     

repetition = int(input("How many times do you want to use?:"))

print("""
1 = copy
2 = clear
3 = pop
4 = update
5 = keys
6 = values
7 = items
8 = get
""")

for i in range(0 , repetition):

    methode = input("Which method do you want to use?!:")
   

    if methode == "1":
        copy = Dictionary.copy()
        print("Copied:" , copy)

    elif methode == "2":
        Dictionary.clear()
        print("dictionary:" , Dictionary)
 
    elif methode == "3":
        p = input("What kay do you want to remove?: ")
        Dictionary.pop(p)
        print("dictionary:" , Dictionary) 

    elif methode == "4":
        # This code asks the user to enter the key they want to insert and its value
        a = input("Please type your key that you want to insert:") 
        a2 = input("Please type your value that you want to insert:")
        
        # This code uses the update() method to add or update the specified key-value pair in the dictionary
        Dictionary.update({a : a2})
        # This code prints the updated dictionary
        print("dictionary:" , Dictionary)


    elif methode == "5":
        k = Dictionary.keys()
        print("keys:" , k)

    elif methode == "6":
        v = Dictionary.values()
        print("values:", v)

    elif methode == "7":
        i = Dictionary.items()
        print("items:", i)

    elif methode == "8":
        u = input()
        Dictionary.update(u)
        print("dictionary:",Dictionary)

    else:
        print(f"method number should be 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 not {methode}.")

print("Thank you for using us. See you soon😁😄😉")
