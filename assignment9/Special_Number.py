c = 0
number = int(input("Enter Your Number:"))

for i in range(1,number):
    if number % i == 0:
        c += i
    
if c == number:
	print("Yes this is that result that we want.")
    
else:
	print("No this isn't our result.")