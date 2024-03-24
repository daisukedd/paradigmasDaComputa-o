def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter your choice (1-4) or operation symbol (+, -, *, /): ")

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
    }

    # get() method returns the value of the item with the specified key.
    result = operations.get(operation)
    if result is not None:
        print("Result:", result)
    else:
        print("Invalid operation")

calculator()
