# The variables

You can use variables to store any kind of data under a name, and retrieve it simply by typing that name back!
There are different kinds of values you can store : 
- A **number** → Integers like `42` or decimals like `3.141592`, doesn't matter !
- A **string** → Text between quotes, like `"Hello"` or `"abc"`.  
Be careful: **numbers inside a string are not real numbers**, so you cannot compute with them!
- A **boolean** → `True` or `False` statements
- And many other types we'll see later

Here are some examples :

```python
my_number = 42
my_string = "This is more than 10 characters long!"
```

There are also a few rules for naming variables:
- There should not be any space in that name  
 → We use naming styles like `camelCase` (each word starts with a capital letter) or `snake_case` (words separated by `_`)
- A variable must not start with a digit or a symbol

# The print function

The **print function** is very important, this is what **displays text** in your terminal.

To use it, type `print`, then add `()` right after it.
Inside the parentheses, you can put whatever you want to display!

You have different options :
- A **variable** → Simply type the name of the variable!
- A **string** → Write it between quotes, like `"This is a string"`.

With the previous examples, here are some examples :
```python
print(my_number)
→ 42

print(my_string)
→ This is more than 10 characters long!

print("Hi everyone!")
→ Hi everyone!
```

You can also mix text and variables using an **f-string** : add an `f` before the quotes, and put variables inside `{}`: 
```python
print(f"My favorite number is {myNumber}!")
→ My favorite number is 42!
```

Something that can be useful to know, using `#` makes what's after a comment, and is not read by the script.  
To do it on multiple lines, write `"""` at the beginning and at the end of your comment.  
*This technically creates a string, named "docstring", but if it's not used then Python will simply ignore it.*  

Use it to explain what you do!

```python
a = 5 
# This is a comment
b = 6
c = "Hi!" # You can also put it directly next to a line!
"""
Everything between the quotes
Will not be used in the script
You can do as many lines as you want!
"""
print(c) # This should print "Hi!" in the terminal
```

# Time to try!

You should now try to use print and variables!

## Exercise 1
You are given two texts, try to rmodify it by replacing text so your terminal displays :
```bash
What's your favorite number?
42
```
Be careful, we want 42 as an **integer**, not a string!

## Exercise 2
Now that you understand how printing work, time to do the ritual that every new developper does: display "Hello world!" in your terminal!

## Exercise 3
Now, try to do the same but with variables!  
1. Define the variable `myText` and put the question in.  
2. Define the variable `favoriteNumber` and put your favorite number in.  
3. Print both variables separately.
4. Print the favoriteNumber with text before using an `f-string`.

Final result should be :
```bash
What's your favorite number?
42
Your favorite number is 42!
```