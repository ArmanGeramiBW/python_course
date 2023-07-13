Number = int(input("write your number")) 
for i in range(Number, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
for i in range(1 , Number + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
