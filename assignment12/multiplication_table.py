def multiplication_table(x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            print(f"{i} x {j} = {i*j}", end=" ") # format = sentence 2 and 1
        print()
x = int(input("enter x: "))
y = int(input("enter y: "))
multiplication_table(x,y)