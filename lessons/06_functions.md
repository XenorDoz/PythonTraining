# Functions (basics)

Working with variables and lists is useful, but as your program grows, you will quickly notice something:  
You start repeating the same code again and again.

That's where **functions** come in.

A function lets you **group code into a reusable block**, give it a name, and call it whenever you need it.  
It makes your code **cleaner, shorter, and easier to understand**

# 1. What is a function?

A function is a named block of code that performs a specific task.  
You define it once, and then you can call it as many times as you want.  

Think of it like a machine:  
You give it some input, it does something, and it may give you an output.

# 2. Defining a function

A function is defined using the `def` keyword:

```python
def compute():
    print("Computing..")
```

- `def` tells Python you are defining a function
- `compute` is the function's name
- `()` means it takes no parameters
- the code inside is indented as long as it must be used by the function block
  
Nothing happens yet — you only *defined* the function.

# 3. Calling a function

To execute the code inside the function, you must **call it**:

```python
compute()
```

Every time you call it, the code inside runs again.

# 4. Using parameters

Parameters let you pass information into a function.

```python
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")
```

Here:
- `name` is a parameter
- `"Alice"` and `"Bob"` are arguments
  
Parameters make functions flexible and reusable.

# 5. Default parameters

You can give parameters a default value:

```python
def greet(name="friend"):
    print("Hello", name)

greet("Xen")    # Hello Xen

greet()         # Hello friend
```

If you don't provide a value, Python uses the default one.

**Default parameters must be placed after non-default parameters**

In Python, parameters with default values must always come **after** the ones without defaults.

**Valid:**

```python
def greet(name, message="Hello"):
    print(message, name)
```

**Invalid:**

```python
def greet(message="Hello", name):
    print(message, name)
```

This causes a syntax error because Python wouldn't know how to match the arguments when calling the function.

You can still override default values using keyword arguments:

```python
greet(name="Xen", message="Hi")
```

# 6. `return` vs `print`

A function can **return** a value using `return`

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)       # 8
```

**Printing is not returning**

```python
def bad_add(a, b):
    print(a + b)

x = bad_add(3, 5)
print(x)       # None
```

- `print()` displays something
- `return` gives a value back to the caller  

Most useful functions use `return`.

# 7. Multiple returns

A function can return multiple values at once (as a tuple):

```python
def compute_stats(a, b):
    return a + b, a * b

s, p = compute_stats(3, 5)
print(s, p)         # 8 15
```

# 8. Scope of a variable

Variables created **inside** a function are **local**:

```python
def test():
    x = 10      # local

    print(x)

test()          # 10
print(x)        # error: x does not exist here
```

They only exist inside the function and in every block indented past the declaration in that function.

Variables created **outside** a function are **global**:

```python
x = 10

def show():
    print(x)    # can read global variable

show()          # 10
print(x)        # 10
```

**Modifying a global variable inside a function**

You must use `global` to be able to modify a global variable inside a function:

```python
x = 10

def modify():
    global x
    x = 20

print(x)        # 10
modify()
print(x)        # 20
```

But it is **not recommended**.  
It makes code harder to understand.

Prefer returning values instead.

# 9. Conclusion

Functions help you structure your program like chapters in a book.

Instead of writing everything in one giant block, you split your logic into small, clear pieces:
- one function to load data
- one function to compute something
- one function to display results
- ...
  
This makes your code:
- easier to read
- easier to maintain
- easier to debug
- easier to reuse

Good code is not code that "works".  
Good code is code that is **clear**.

# 10. Exercises!    

### Exercise 1

Write a function `square(n)` that returns the square of a number.  
Then:
1. Ask the user for a number using `input()`.
2. Convert it to an integer.
3. Call the function and print the result, without printing inside the function.
___

### Exercise 2

Write a function `repeat()` that prints `text` a certain number of times.  
You'll give it:
- a parameter `text`: the text to print
- a parameter `times`: the number of times it is printed, it should be 3 by default

The function should print the result directly
___

### Exercise 3

Write a function `analyze(a, b)` that returns:
- their sum
- their difference
- their product

Then ask for two numbers, call the function and display the three results on separate lines.  
*The function should not display the results, only returning them.*
___

### Exercise 4

Given the following code:

```python
x = 10

def modify():
    x = 5
    print("Inside:", x)
```

1. Predict what will be printed.
2. Call the function.
3. Print `x` again outside the function.
4. Explain why the two values are different.
___

### Exercise 5

Create three functions:
- `ask_number()` → asks the user for a number and returns it
- `compute_total(a, b)` → returns the sum of two numbers
- `show_result(value)` → prints `The result is: <value>`

Then, write a small program that uses these three functions to:
1. ask for two numbers
2. compute their total
3. display the result

*You can do the small program in multiple lines, or in one line!*  
*Although it is strongly recommended to do it on multiple lines for readability*