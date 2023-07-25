def replace(word):
    vowels = "AEIOUauoie"
    for i in word:
        if i in vowels:
            word = word.replace(i, "!")
    return word
word = input("enter your string: ")
print(replace(word)) 