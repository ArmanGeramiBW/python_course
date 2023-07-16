import random
x =int(input("Write your number:"))

Big_num= 100
Small_num = 0
bot = random.randint(Small_num,Big_num)
while True:
    if bot == x:
        print(f"bot is {bot}"," WE'VE GOT A WINNER!")
        break
    elif x < bot:
        print(f"bot is {bot}","Go DOWN!")
        Big_num = x
        bot = random.randint(Small_num,Big_num)
    else:
        print(f"bot is {bot}","Go UP!")
        Small_num = x
        bot = random.randint(Small_num,Big_num)
        #Helped from KIA
