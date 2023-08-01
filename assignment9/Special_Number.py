num = int(input("please enter your number:"))
answer = 0
for i in range(1,num):
    if num % i == 0:
        answer += i
if answer == num:
    print("Yes,this is ok")
else:
    print("No,this isn't ok")
