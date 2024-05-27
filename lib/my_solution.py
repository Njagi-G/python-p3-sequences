def print_fibonacci(length):
    pass
    # Initialize the Fibonacci sequence with the first two values
    fib_list = [0, 1]

    # Generate the Fibonacci sequence up to the specified length
    for i in range (2, length):

        # Calculate the next number in the sequence as the sum of the last two numbers
        i = fib_list[-1] + fib_list[-2]

        # Add the new number to the sequence
        fib_list.append(i)

    # Print the complete Fibonacci sequence
    print(fib_list)


# Call the function to generate and print the Fibonacci sequence up to the length provided in the function's parameters
print_fibonacci(9)
print_fibonacci(12)
print_fibonacci(20)