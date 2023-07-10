height = float(input("please type your height:"))
weight = float(input("please type your weight:"))
your_BMI = (height * height) / weight
print(your_BMI)
if your_BMI < 18.5:
    print("you are thin")
elif 18.5 <  your_BMI < 24.9:
    print("you are normal")
elif 25.0 < your_BMI < 29.9:
    print("you are In obesity")
elif 30 < your_BMI < 34.9:
    print("you are fat")
else:
    print("You are very fat")