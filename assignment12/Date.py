def date(year,month,day, hour,minutes):
    print("You were born on date")
    print(year, '/', month, '/', day,'at',hour , ':' , minutes ,  end="")
day = int(input("Write the number of your birth day: "))
month = int(input("Write the number of your birth month: "))
year = int(input("Write the number of your birth year: "))
hour = int(input("Write the number of your birth hour:"))
minutes = int(input("Write the number of your birth minutes:"))
date(year, month, day , hour , minutes)
