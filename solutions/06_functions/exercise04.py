# Given this code:

x = 10

def modify():
    x = 5
    print("Inside:", x)

print(x)

# 1. What will be printed ?

"""
Answer here:
    The code will print `5`
"""

# 2. Call the function

modify()


# 3. Print `x` again here

print(x)        # Printed 10

# 4. Why are the two values different ?

"""
Answer here:
    Because the x in the `modify()` is only kept inside the function
    Inside, x is modified
    Outside, it is never touched
"""