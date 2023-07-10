number = float(input("[Please type  your number:"))
if number % 2 == 0 and number > 4 :
     print("A")
elif number % 2 == 0 and number < 4 :
     print("B")
elif number < 0 :
    print("D")
else:
     print("C")