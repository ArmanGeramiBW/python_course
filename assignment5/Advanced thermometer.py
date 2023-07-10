# C = Celsius F=Fahrenheit K=Kelvin
operation = int(input("""1_ C to K '-' 2_ C to F '-' 3_ K to C '-' 4_ K to F '-' 5_ F to C '-' 6_ F to K:"""))
Number = float(input("please write your amount:"))
if operation == 1:
    outcome = Number + 273.15
    print(outcome)
elif operation == 2:
    outcome = (Number * 9 / 5) + 32
    print(outcome)
elif operation == 3:
    outcome = Number - 273.15  
    print(outcome)
elif operation == 4:
    outcome = (Number - 273.15) * 9 / 5 + 32  
    print(outcome) 
elif operation == 5:
    outcome = (Number - 32) * 5 / 9  
    print(outcome)  
elif operation == 6:
    outcome = (Number - 32) * 5 / 9 + 273.15  
    print(outcome) 
else:
    print("I did not find your outcome.Please try again")     