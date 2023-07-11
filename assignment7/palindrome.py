string = input("Please write your thing:")
string = string.split()
string = '' .join(string)


for i in range(len(string)):
    z = 0
    if string[i] == string[z]:
        print("is")
        exit(0)
    else:
     z += -1
    print("is not palindrome")
