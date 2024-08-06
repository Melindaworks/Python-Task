def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Prompt the user to input a positive integer
n = int(input("Enter a positive integer: "))

# Compute and print the nth Fibonacci number
if n > 0:
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
else:
    print("Please enter a positive integer.")
