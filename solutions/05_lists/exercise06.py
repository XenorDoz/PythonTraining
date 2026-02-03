# You are given the following dictionary

temps = {
    (0, 0): 12,
    (0, 1): 14,
    (1, 0): 15
}

# Display the temperature at position `(0, 1)`

print(temps[(0, 1)])

# Add a new temperature at position `(1, 1)` with the value `18`

temps[(1,1)] = 18

# Replace the temperature at position `(0,0)` with `10`

temps[(0,0)] = 10

# Display all the keys from the dictionary (hint: use `temps.keys()`)

print(temps.keys())




"If you want to display only the keys, you can do this:"

string = ""
for key in temps.keys():
    string += str(key) + ", "
print(string[:-2])
# The `:-2` removes the ", " at the end that I added
#  to separate every key

"""
Although, this is for display only
You want to keep it raw to use it in your code
"""