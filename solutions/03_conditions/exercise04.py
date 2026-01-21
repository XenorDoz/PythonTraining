# Let's make a small game!
# The program secretly chooses a number (you can pick any number you want).
# Then, ask the user to guess it.
#
# Depending on the guess, display:
# - "Too low!" if the guess is smaller
# - "Too high!" if the guess is greater
# - "Correct!" if it's exactly the same
#
# For now, you only have one try — we'll fix that later!

secret = 6                                            # Choose your secret number here
guess = int(input("Choose a number between 1 and 10: "))   # Ask the user for their guess

# Write your conditions here:
if guess == 6:
    print("Correct!")
elif guess <= 6:
    print("Too low!")
else:
    print("Too high!")


# Note: 
# This works too if you used 3 if, but it does not always work for every code
# It's better to use if/elif/else, just in case!

