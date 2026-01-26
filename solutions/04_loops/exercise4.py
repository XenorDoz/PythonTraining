# Ask for the number `n`

n = int(input("Number n: "))

# Display the sum of every number from 1 to `n` (included) using a while loop
# Hint: you might want a variable that keeps track of where you are in the loop
#       you will probably need it to increase at each step

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print(sum)