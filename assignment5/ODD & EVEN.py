number = input("Enter your number:")

n0 = number.count("0")
n1 = number.count("1")
n2 = number.count("2")
n3 = number.count("3")
n4 = number.count("4")
n5 = number.count("5")
n6 = number.count("6")
n7 = number.count("7")
n8=  number.count("8")
n9 = number.count("9")

n0 = n0
n1 = n1
n2 = n2
n3 = n3
n4 = n4
n5 = n5
n6 = n6
n7 = n7
n8 = n8
n9 = n9

evens = int(n0+n2+n4+n6+n8)
odds = int(n1+n3+n5+n7+n9)

if evens>odds:
    print("Even is more than odd.")
elif odds>evens:
    print("odd is more than even.")
else:
    print("odd and even are equal.")
