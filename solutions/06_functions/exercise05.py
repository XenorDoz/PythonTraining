# Create the function `ask_number()`
# - ask for a number and returns it
#
# *Don't forget to convert into an int!*

def ask_number():
    number = int(input("Give a number: "))
    return number

# Create the function `compute_total(a, b)`
# - returns the sum of two numbers

def compute_total(a, b):
    return a + b

# Create the function `show_result(value)`
# - prints `The result is: {value}`

def show_result(value):
    print(f"The result is: {value}")

# Use your functions to:
# 1. Ask for two numbers
# 2. Compute their total
# 3. Display the result

a = ask_number()
b = ask_number()

result = compute_total(a, b)

show_result(result)