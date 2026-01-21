# First, ask for the price
# You can almost copy the exercise01.py file!
# Also, don't bother with "USD", simply ask the price without the unit

answer = input("Give your price in USD: ")

# Then, convert it into a number

price = int(answer)

# Now, apply the correct reduction using the correct block!
# You must decide how to structure your conditions so that:
"""
If price is equal or above to 100, apply a reduction of 10 %
Otherwise, if price is equal or above to 50, apply a reduction of 5
Otherwise, if price is equal or above to 20, apply a reduction of 1

*Hint: Apply a reduction of 10% is the same as multiplying by 0.90!*
"""
# Think carefully: depending on how you write your conditions,
# the result may change!

if price >= 100:
    price = price * 0.9
elif price >= 50:
    price = price - 5
elif price >= 20:
    price = price - 1

# Finally, display it!
print(f"The final price is {price}!")