print("Weight(kg): ")
while True:
    try:
        weight = float(input())
        break
    except ValueError:
        print("Please enter a number")

print("Height(m): ")
while True:
    try:
        height = float(input())
        break
    except ValueError:
        print("Please enter a number")

bmi = round(weight/(height**2), 2)
print("Your BMI is " + str(bmi))