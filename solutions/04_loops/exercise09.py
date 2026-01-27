# Ask for a number n

n = int(input("Number n:"))

# while True:
#   - if n is even, divide it by 2, display the result and repeat the loop immediatly
#   - if n is odd, stop the loop

while True:
    if n % 2 == 0:
        n //= 2 # Means n = n // 2
        print(n)
        continue
    if n % 2 == 1:
        break
