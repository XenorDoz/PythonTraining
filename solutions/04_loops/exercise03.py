# Ask for the number `a`

a = int(input("Number a: "))

# Ask for the number `b`

b = int(input("Number b: "))

# Display every number from `a` to `b` included

for i in range(a, b + 1, 1):
    print(i)

# Now backwards!

for i in range(b, a - 1, -1):
    print(i)