numbers = []
    
number1 = float(input("write your score:"))
number2 = float(input("write your score:"))
number3 = float(input("write your score:"))
number4 = float(input("write your score:"))
number5 = float(input("write your score:"))
number6 = float(input("write your score:"))
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)
numbers.append(number6)
A = sorted(numbers)
print(A)

B = sorted(numbers, reverse=True)
print(B)