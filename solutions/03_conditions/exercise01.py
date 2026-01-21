# We first ask the user a number, and store the value
answer = input("Choose an number: ")

# We convert the answer into a integer
number = int(answer)

# Now check the value!
# Replace the empty parentheses with the correct conditions:

if (number == 0):
    print("Your number is equal to 0!")
elif (number < 0):
    print("Your number is negative!")
else: 
    print("Your number is positive!")

# Note :
# We don't need a condition for the positive case.
# Ifi t's not a zero and not negatibe, the only option left is: positive!