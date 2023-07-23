def C_S(str): # C_S means capital & small words
    lowerrr = 0
    upperrr = 0
    for s in str:
        if 65 <= ord(s) <= 90: #this numbers is like mors code ...---...
            upperrr += 1
        elif 97 <= ord(s) <= 122:
            lowerrr += 1
        
    return upperrr , lowerrr
string = input("enter your string: ")
u, l, = C_S(string)
# u means upper
## l means lower
print("number of capital words:", u)
print("number of small words: ", l)