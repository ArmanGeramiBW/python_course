while True:
 import math
 def sum(a,b):

    return a+b

 def subtraction(a,b):
    return a-b

 def multiplication(a,b):
    return a*b

 def division(a,b):
    return a/b

 print ("the operations:")
 print ("1.sum 2.subtraction 3.multiplication 4.division 5.log 6.pow 7.sqrt 8.tan 9.cot ")
 selection = int(input("your operation:"))
 First_number = int(input("enter your first number: "))
 Second_number = int(input("enter your second number: "))
 if selection == 1:
    print(First_number , "+" , Second_number , "=" , sum(First_number , Second_number))
 elif selection == 2:
    print(First_number , "-" , Second_number , "=" , subtraction(First_number , Second_number))
 elif selection == 3:
    print(First_number , "*" , Second_number , "=" , multiplication(First_number , Second_number))
 elif selection == 4:
    if Second_number == 0:
        print("error")
    else:
        print(First_number , "/" , Second_number , "=" , division(First_number , Second_number))

 elif selection == 5:
     print(math.log(First_number))
 elif selection == 6:
    print(math.pow(First_number , Second_number))     
 elif selection == 7:
    print(math.sqrt(First_number))   
 elif selection == 8:
    print(math.tan.radians(First_number)) 
 elif selection == 9:
    print = math.cos(math.radians(First_number) / math.sin(math.radians(First_number)))
 else:
    print ("we could not find your number.Please try again")
 Q = input("Do you wanna more?!:(y/n)")
 if Q == "n":
    exit(0)
 else:
    Q == "y" 
