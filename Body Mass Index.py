height=float(input("enter the height of your body in inches "))
weight=float(input('enter the weight of your body in pounds '))

BMI=(weight*703)/(height**2)

if BMI < 18.5:
    print(f"your Body Mass Index is {BMI:.2f}")
    print("your are uderweight please eat havy food (:")
elif 18.5<= BMI <=25:
    print(f"your BMI is {BMI:.2f}")
    print("your are please optimize weight (:")
else:
    print(f"your Body Mass Index is {BMI:.2f}")
    print("your are overweight (Obolo) (:")

#print(BMI 