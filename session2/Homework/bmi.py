
a = float(input("Enter your Heigh: "))
b = float(input("Enter your weight: "))
a = a/100
BMI = b/(a*a)
print("Your BMI:",BMI)
if BMI < 16:
   print("Severely underweight")
elif BMI < 18.5:
   print("Underweight")   
elif BMI < 25:
    print("Normal")   
elif BMI < 30:
    print("Overweight")
else :
    print("Obese")    
