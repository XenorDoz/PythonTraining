# Ask for the number `a`

a = int(input("Number a: "))

# Ask for the number `b`

b = int(input("Number b:"))


# Display every number from `a` to `b` included using a while loop
# Hint: you might want a variable that keeps track of where you are in the loop

position = a # You can use this variable as your starting point

while position <= b:
    print(position)
    position = position + 1


# Now backwards! (from b to a, included)
position = b
while position >= a:
    print(position)
    position = position - 1