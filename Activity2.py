height=int(input("enter height"))
weight=int(input("enter weight"))
bmi=weight/(height/100)**2

if bmi<=18.9:
    print("you are underweight",bmi)
elif bmi<=24.9:
    print("you are healthy",bmi)
elif bmi<=29.9:
    print("you are overweight",bmi)
elif bmi<=34.9:
    print("you are severly overweight",bmi)
elif bmi<=39.9:
    print("you are obese",bmi)
else:
    print("you are severly obese",bmi)
