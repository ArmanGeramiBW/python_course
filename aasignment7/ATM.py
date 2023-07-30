password = "5007"

pass_list = [password[3],password[2],password[1],password[0]]
#Placement of numbers for password
c = 0

while 3 > c:
      Password = input("enter your password:\n")
    
      if len(Password) == 4:
         if password == Password:
            print("ٌWelcomeback!")
           
         elif str([Password[3],Password[2],Password[1],Password[0]]) == str(pass_list[::-1]):
            print("In a few minutes you will be arrested by the police dear friend")
            
         else:
            print("Please try again")
            c += 1
    
      else:
        print("Please try again")

print("We are sorry because you can't log in your acc")
