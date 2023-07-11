list = []

for i in range(10):
    number = float(input("Please write your number:"))
    list.append(number)

list2 = [] 
c = 0
while c < 10:
    list2.append(list[c] + 2)
    c += 1
print(list)
print(list2)