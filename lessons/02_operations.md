# Basic operations

## 1. Introduction

Now that you know how to define variables and display them, it's time to **use them**!  
In this lesson, you'll learn how to make Python do math, combine text, and create your own expressions.


## 2. Arithmetic operations

In Python, you can use several basic operations:
- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Integer division `//`
- Modulo `%`

To use them, simply write a number, then the operator, then another number — and that's it!  
You can do that when you define a variable, redefine it, or when you display it for example:
```python
a = 10
b = 3
c = a + b
c = c + 4 # This will do a + b + 4, thus 13 + 4 = 17

print(15 + 17)# 32
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333
print(c)      # 17
print(c // 5) # 3
print(c % 5)  # 2
```

#### **Exercise 1**

Let's try to do some basic maths! Try to display results of:
- 12 * 8
- 50 + 17
- 63 / 7
- 22 - 4
- 14 // 4
- 8 % 3
  
#### **Exercise 2**

Now, let's use some variables to make it a bit more complex!  
Let x be 5, y be 14, z be 2.  
Compute: 
- x + z
- x + y
- y - z
- y - (x * z)
- y % x
- (x + z) * (y / 2) - (y % x)

## 3. String operations

Operations also work with strings!

You can join text together by concatenating them using `+` with strings:
```python
a = "Hello "
b = "world!"
print(a + b)        # Hello world!
```

You can also repeat a string using `*`:
```python
print("ha" * 3)     # hahaha
```

#### **Exercise 3**

Try to join "cof" and "fee", then display it 4 times in the same string using operations!  
*You can either use variables, or directly print it (directly displaying it is harder).* 

## 4. Mixing types

You **cannot** mix numbers and strings directly:
```python
print(42 + "3")     # Error
```

Although, you can convert them!
- int("3") → converts to **a number**
- str(42) → converts to **a string**

Of course, to convert a string into a number, the string must contain a number only!

Here's an example:
```python
age = "20"
print(int(age) + 1)     # 21

number = 42
print("My number is " + str(number))    # My number is 42
```

## 5. Operations inside f-string

Remember the f-strings? Well, instead of using a variable, you can directly use an operation!
```python
a = 5
b = 7
print(f"The result is {a+b}")   # The result is 12
```

#### Exercise 4
To recap everything, here's a challenge:   
Try to display `5 + 3 = 8` using the given variables, an f-string and an operation inside the f-string!