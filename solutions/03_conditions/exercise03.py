# You're on your own now!
# Ask a number, and display:
# - if it's even
# - if it's greater than 10
# - or if it's both at the same time!
# - if none of the above condition match, say it's a special case.
#
# If it's both, display it in only one print().
# This means you will need to use the `and` keyword!
#
# Hint: An even number is when you divide a number by 2, the remainder is 0.
# The modulo operator (%) exactly gives you that!
# For example: 8 % 2 gives 0, 9 % 2 gives 1
#
# Write your code below:

# Ask for the number and convert it
number = int(input("Choose a number: "))

# Now check!
if number % 2 == 0 and number > 10:
    print("Your number is even and greater than 10!")
elif number % 2 == 0:
    print("Your number is even!")
elif number > 10:
    print("Your number is greater than 10!")
else:
    print("Special case")