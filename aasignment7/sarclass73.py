# input : 5
# output :01'2''3'''4''''5'''''

n = int(input('n: '))
c = 0
while c <= n:
        print(c,"'"*c , end='' , sep='')
        c += 1