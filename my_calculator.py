
#####################################

# OBJECTIVES

# How to make a calulator
# How to use while loops, if, elif, and else statments
# How to use Python input and output

#####################################

# STEPS

# Print welcome message
# Ask the user for num1
# Ask the user for num2
# Ask the user for an operation
# Execute operations and print results
# loop the program

#####################################

# Print welcome message
print("\nHello, welcome to my calculator program\n")

# define variables
entry = 1

# begin loop
while True:
    print("Entry", entry)

    # Ask the user for num1
    num1 = int(input("Enter your first number: "))

    # Ask the user for num2
    num2 = int(input("Enter your second number: "))


    # Ask the user for an operation
    print("\n"
          "a) Addition\n"
          "b) Subtraction\n"
          "c) Multiplication\n"
          "d) Division\n")
    operation = input("Pick an operation: ")
    operation = operation.lower()

    # Execute operations and print results
    if operation == 'a':
        print("Result:", num1 + num2)
    elif operation == 'b':
        print("Result:", num1 - num2)
    elif operation == 'c':
        print("Result:", num1 * num2)
    elif operation == 'd':
        print("Result:", num1 / num2)
    else:
        print("Error: Invalid operation")
    
    # Print closing message
    response = input("\nEnter 'p' to exit or any other character to continue: ")
    response = response.lower()

    # end loop
    if response == 'p':
        print("Shutting down calculator...")
        break

    # continue loop
    else:
        entry += 1
        print("\n----------------------\n")
