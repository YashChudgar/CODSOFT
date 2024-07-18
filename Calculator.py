def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Denominator cant be zero")


print("Welcome to the World of Calculations")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

while True:
    try:
        number=int(input("Enter the operation number you want to perform: "))
        if number in [1,2,3,4]:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4")
    except ValueError:
        print("Invalid Input.Please Enter a number.")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

if number==1:
    result=add(num1,num2)
    operation="+"
elif number==2:
    result=subtract(num1,num2)
    operation="-"
elif number==3:
    result=multiply(num1,num2)
    operation="*"
elif number==4:
    result=divide(num1,num2)
    operation="/"
print(f"{num1} {operation} {num2} = {result}")