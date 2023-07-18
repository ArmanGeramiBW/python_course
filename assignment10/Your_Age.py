import datetime
year = int(input("please write that what year were you born:"))
day = int(input("please write that what day were you born:"))
month = int(input("please write thet what month were you born(numbers):"))
now = datetime.datetime.today()

this_year = int(now.year)

age = this_year - year

print(f"You are {age} years old \n")

day = age * 365
week = age * 52        
second = age * 31536000

print(f"You lived for {second} seconds")
print(f"Ypu lived for {day} day")
print(f"You lived for {week} week")
