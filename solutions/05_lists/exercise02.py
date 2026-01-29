drinks = ["coffee", "tea", "water"]

print(f"Default state of drinks:\n\t{drinks}")

# Change the 2nd value to juice"

drinks[1] = "juice" 

print(f"Changed \"tea\" to \"juice\":\n\t{drinks}")

# Add "milk" at the end of the list using append()

drinks.append("milk")

print(f"Added \"milk\" at the end of the list:\n\t{drinks}")

# Remove coffee using remove()

drinks.remove("coffee")

print(f"Removed coffee:\n\t{drinks}")

# Remove the value at index 1 using pop()
# Store it in a variable named `removed`
# Print the variable `removed`

removed = drinks.pop(1)
print(removed)

print(f"Removed the value at index 1:\n\t{drinks}")

