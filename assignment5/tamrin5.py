number = int(input("Please write your number:"))

A = number % 7

if number == 0:
    print("please try again")

elif A == 0:
    print("This number is a multiple of seven")

number = number // 7
number *= 7 
number += 7
print(number , "the next multiple of seven" ) 