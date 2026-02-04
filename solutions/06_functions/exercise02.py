# Write a function `repeat`:
#  - Has a parameter `text`: the text to print
#  - Has a parameter `times`: number of times to print, 3 by default


# Your function here!

def repeat(text, times=3):
    for i in range(times):
        print(text)




repeat("Hello", 5)      # prints 5 lines of "Hello"
repeat("Hi")            # prints 3 lines of "Hi"