passcode = 5007
police_pass = 7005
list_pass = []
S = 0
while S < 3 :
   password = int(input("please enter your passcode:"))
   if password == passcode :
      print("welcome to your account")
      break
   elif (password) == police_pass:
      print("In another minute you will be arrested by the police.")
      break
   else:
      print("The password is wrong")
      S += 1
      
