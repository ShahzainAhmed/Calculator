# Calculator

# Creating function for Addition.
def Add(x,y):
    return x + y

# Creating function for Subtraction.
def Sub(x,y):
    return x - y

# Creating function for Multiplication.
def Mult(x,y):
    return x * y

# Creating function for Division.
def Div(x,y):
    return x / y

print ("Select operation for Calculation")
print ("1: Addition")
print ("2: Subtraction")
print ("3: Multiplication")
print ("4: Division")

while True:
    # Taking input from the user.
    choice = input("Enter choice (1/2/3/4):")

    # Check if choice is from any of these 4.
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", Add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Mult(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Div(num1, num2))
        break
    else:
        print("Invalid Input")