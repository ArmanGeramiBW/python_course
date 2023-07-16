while True:
 number = float(input("enter number: "))
 if 0 > number :
     print("D") #means our number is negative
 else :
     if number % 2 == 0 and number < 4:
      print("B")
     elif number % 2 == 0 and number > 6:
      print("A")
     else:
      print("C")