numbers = [1 , 2 , 3 , 4 , 3 , 2 , 1 , 4 , 5 , 6 , 7 , 7 , 7 ]
dict = {}
for number in numbers:
    if number in dict:
        dict[number] += 1
    else:
        dict[number] = 1
print(dict)
