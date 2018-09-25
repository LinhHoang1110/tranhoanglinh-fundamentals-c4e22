input("Note: you must do the conversion from cm to m before calculation")
a = float(input("Enter your Heigh: "))
b = float(input("Enter your weight: "))

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
