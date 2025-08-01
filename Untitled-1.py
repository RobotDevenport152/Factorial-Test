# Week 1 – Activity 1: Factorial using a while loop

print("Welcome to the Factorial Calculator!")

while True:
    try:
        # Ask user to enter a number
        user_input = input("Enter a non-negative integer to calculate its factorial (or type 'exit' to quit): ")

        # Allow user to exit
        if user_input.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break

        # Convert input to integer
        num = int(user_input)

        # Check for negative input
        if num < 0:
            print("Factorial is not defined for negative numbers. Please try again.")
            continue

        # Special case: factorial of 0 is 1
        if num == 0:
            print("The factorial of 0 is 1.")
            continue

        # Calculate factorial using a while loop
        factorial = 1
        counter = num

        while counter > 1:
            factorial *= counter
            counter -= 1

        print(f"The factorial of {num} is {factorial}.")

    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
