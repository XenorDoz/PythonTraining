# Ask the user for a number n

n = int(input("Number n:"))

# While the number is even:
# - divide it by 2
# - display the result
# - continue the loop
# When the number becomes odd:
# - display the result
# - stop the loop

while n % 2 == 0:
    n = n // 2
    print(n)