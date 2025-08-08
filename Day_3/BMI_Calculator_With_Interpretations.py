weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in m? "))

BMI = weight / (height ** 2)
print(f"BMI ={BMI}")
if BMI<18.5:
    print("underweight")
if BMI>=18.5:
    print("normal weight")
if BMI>=25:
    print("overweight")