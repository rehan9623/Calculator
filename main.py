def Calculator(num1,num2,operator):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1+num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        if num2 == 0:
            return "Error, Division by 0 is not possible"
        return num1/num2
    elif operator == '^':
        return num1**num2
    elif operator == '%':
        return (num1/num2)*100
    else:
        return "Invalid Response"

'''print("***Advanced Calculator***")   
print("Available operations: +, -, *, /, ^ (power), % (percentage)") 
num1 = float(input("Enter a First Number: "))
num2 = float(input("Enter a Second Number: "))
operator = input("Enter operator (+, -, *, /, ^, %): ")

Result = Calculator(num1,num2,operator)

print(f"\nResult : {num1} {operator} {num2} = {Result}")'''

while True:  # Infinite loop
    # Taking user inputs
    try:
        num1 = float(input("\nEnter first number: "))
        operator = input("Enter operator (+, -, *, /, ^, %): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue  # Restart loop if invalid input is given

    # Perform calculation
    result = Calculator(num1, num2, operator)
    print(f"Result: {num1} {operator} {num2} = {result}")

    # Ask user if they want to perform another calculation
    choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if choice not in ('yes', 'y'):
        print("👋 Thanks for using the calculator. Goodbye!")
        break  # Exit the loop