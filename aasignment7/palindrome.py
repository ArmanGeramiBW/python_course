S = str(input("Write your thing:"))
S = str(S)
c = -1
for i in range(len(S)//2):
    if S[i] != S[c]:
        print("is not palindrome")
        exit(0)
    else:
        c += -1
print("is palindrome")