# Ask for the number `n`

n = int(input("Number: "))

# Display the sum of every number from 1 to `n` (included)
# Hint: think about how to accumulate a result inside the loop

sum = 0
for i in range(1, n + 1):
    sum = sum + i

print(sum)