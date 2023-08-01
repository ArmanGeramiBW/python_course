import random
number = float(input("player1: type your number:"))
while True:
    number2 = float(input("player2:is your number?"))
    if number2 == number:
      print("Oh Jesus Christ, your number is correct.")
      break
    elif number2 > number:
       print("lower")
    else:
        print("there is more")
