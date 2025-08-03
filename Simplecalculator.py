print("🧮 Welcome to Kamungu's Simple Calculator!😎")

while True:  # Keeps running until the user chooses to exit
    # Get numbers from the user
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    # Ask for the operation
    print("Choose an operation: +  -  *  /")
    operation = input("Enter the operation you want to perform: ")

    # Perform the chosen operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "❌ Error: Division by zero is not allowed."
    else:
        result = "❌ Invalid operation."

    # Display the result
    print("✅ Result:", result)

    # Ask if user wants to calculate again
    again = input("Do you want to do another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("👋🏾 Thank you for using Kamungu’s calculator. 😊Bye Bye!")
        break  # Exit the loop
