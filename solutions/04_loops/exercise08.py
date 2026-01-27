# Ask for a number n
# (You can ask it before or inside the loop!)
#
# while True:
#   - if n is negative, skip it using continue
#   - if n is 0, stop the loop
#   - otherwise, display n
#   - ask again for a new number

while True:
    n = int(input("Number n: "))
    if n < 0:
        continue
    if n == 0:
        break
    if n > 0:
        print(n)