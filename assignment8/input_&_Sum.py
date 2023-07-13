x = []
S = str(input("write your thing:"))
sum_Numbers = 0
Numbers = [ 1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 , 0]
for i in Numbers:
    for j in S:
        if str(i) == j:
            sum_Numbers += i
        else:
           x.append(j)
print(sum_Numbers)
