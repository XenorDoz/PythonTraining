sentence = "I like coffee"

# Turn the sentence into a list of words using split() and display it

words_list = sentence.split()
print(words_list)

# Grab the last word and put it in a variable named `word`

word = words_list[-1]
print(word)

# Create a list `characters` from the variable `word` using `list()` and display it

characters = list(word)
print(characters)


# Display the length of that list in two different ways:
#   - using the list `characters`
#   - using the string `word`

print(len(characters))
print(len(word))