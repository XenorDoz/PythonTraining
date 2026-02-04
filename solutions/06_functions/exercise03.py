def anaylze(a, b):
    # Compute their sum
    add = a + b


    # Compute ther difference
    sub = a - b


    # Compute their product
    mult = a * b


    # Return the correct values
    return add, sub, mult

# Ask for the two numbers
a = int(input("Give a number a: "))
b = int(input("Give a number b: "))


# Call the function, grab the values in different variables
sum, diff, prod = anaylze(a, b)



# Display the results in separate lines
print(f"The sum is {sum}")
print(f"The difference is {diff}")
print(f"The profuct is {prod}")