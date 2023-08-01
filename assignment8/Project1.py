text = input("type some numbers(for example: 3.11.9):")
sum = 0

for c in text:
    #isdigit()In Python, the isdigit() function is a string function that checks whether all characters are
    ## in the same string. This function returns True if all characters are string and False otherwise
    if c.isdigit():
        sum += int(c)

print("Outpot:" , sum)
