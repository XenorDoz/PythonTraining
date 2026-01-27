# Ask for a number n
# (You can ask it before or inside the loop!)
#
# while True:
#   - if n is 0, stop the loop using break
#   - otherwise, display n and ask again

while True:
    n = int(input("Number n: "))
    if n == 0:
        break
    print(n)