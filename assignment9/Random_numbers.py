import random
numbers = []
while True:
 n = int(input('enter number:'))
 while len(numbers) < n:
    number = random.randint(1,100)
    if number in numbers:
        continue
    else:
        numbers.append(number)

 print(numbers)
 break