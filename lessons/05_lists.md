# The lists

Working with a single value is useful, but very limiting.  
Often, you need to store **multiple pieces of data** at the same time: several numbers, several words... And a single variable isn't enough for that.

That's where **lists** come in.

A list lets you store **many values inside one variable**, keep them organized, and access or modify them easily.

## 1. How to define a list

A list is created using square brackets `[]`.  
It can contain one value, several values, or even be completely empty.  
Lists are extremely flexible: they can store numbers, strings, booleans, or even a mix of different types.  


#### Empty list

You can start with an empty list and fill it later:

```python
my_list = []
```

This is useful when you don't know the values yet, or when you want to build the list step by step.

#### List with values

You can also define a list directly with elements inside the brackets:

```python
numbers = [3, 7, 10]
words = ["apple","banana", "cherry"]
```

Each value is **separated by a comma**.  
Python keeps them in the order you write them.

#### Mixed types

A list can contain different types at the same time:

```python
mixed = [10, "hello", True]
```

This is allowed because Python lists are not restricted to a single type.  
However, mixing types should be done only when it makes sense in your program.

You can even store other lists inside a list!

```python
matrix = [[1,2], [3,4]]
# This would be :   [ [1, 2],  
#                     [3, 4] ]
```

This is called a *nested list*.  
You won't need it right now, but it shows how flexible lists are!

## 2. How to read a list

Once you have a list, you can access any value inside it using its **index**.  
An index is the position of an element in the list.

#### Indexes start at 0

In Python, the first element is at index `0`, the second at index `1`, and so on.

You can access any value by providing the index to the variable like this:
```python
numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[1])   # 20
print(numbers[2])   # 30
print(numbers[3])   # 40
```

If you try to access an index that doesn't exist, Python will show an **"Index out of range"** error.  
Don't worry — just make sure that you're staying within the bounds of the list!

#### Negative indexes

You can also read values starting from the end of the list:

- `-1` → last element
- `-2` → second to last
- etc.

```python
print(numbers[-1])  # 40
print(numbers[-2])  # 30
```

This is very useful when you want the last value without knowing the list's size.

#### Slicing: reading multiple values at once

You can read a part of the list using the slicing syntax:
- `myList[start:end]` → from `start` to `end - 1`
- `myList[:]` → the whole list (a copy)

```python
print(numbers[1:3]) # [20, 30]
print(numbers[:])   # [10, 20, 30, 40]
```

Slicing never causes an error, even if the indexes go beyond the list.

#### The `len()` function

`len()` returns the number of elements in the list:

```python
print(len(numbers)) # 4
```

This helps you avoid going out of range, and it's often used in loops.

## 3. How to modify a list

Lists are **mutable**, which means you can change their content at any moment.  
You can replace values, add new ones, or remove existing ones.  
This flexibility is one of the main reasons lists are so useful.

#### Changing a value

You can replace an element by assigning a new value to its index:

```python
numbers = [10, 20, 30, 40]

numbers[1] = 99
print(numbers)  # [10, 99, 30, 40]
```

Python updates the list immediately.

#### Adding a value: `append()`

`append()` adds a new element **at the end** of the list.

```python
items = ["coffee", "tea"]
items.append("water")

print(items)    # ["coffee", "tea", "water"]
```

This is the most common way to grow a list.

#### Removing a value: `remove()`

`remove()` deletes **the first occurrence** of a value.

```python
drinks = ["coffee", "tea", "water", "juice"]
drinks.remove("tea")

print(drinks)   # ["coffee", "water", "juice"]
```

If the value appears multiple times, only the first one is removed.  
If the value doesn't exist, Python will show an error.

#### Removing by index: `pop()`

`pop()` removes the element at a specific index and returns it.

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop(2)

print(removed)  # 30
print(numbers)  # [10, 20, 40]
```

The `pop()` function can be called without an index, it removes the **last** element:

```python
numbers = [10, 20, 30, 40]
numbers.pop()   # removes the last value

print(numbers)  # [10, 20, 30]
```

## 4. Strings behave like lists

A string is also a *sequence* of characters.  
This means you can access each character using an index, exactly like a list:

```python
word = "coffee"

print(word[0])      # c
print(word[1])      # o
print(word[3])      # f
print(word[1:4])    # off
```

Everything you learned to access a value in the list works with a string!

#### But strings are immutable

This is the main difference between strings and lists.  
You **cannot** modify a string directly:

```python
word = "coffee"
word[0] = "H"       # error
```

If you want to "modify" a string, you must create a **new** one:

```python
word = "coffee"
word = "C" + word[1:]

print(word)         # Coffee
```

## 5. Transforming strings into lists

Sometimes you want to work with a string as *if it were a list*.  
Python gives you two useful tools for that. 

#### `list()` — split into characters

`list()` converts a string into a list of individual characters:

```python
word = "coffee"
chars = list(word)

print(chars)        # ["c", "o", "f", "f", "e", "e"]
```

This is useful when you need to inspect or manipulate each character separately.

#### `split()` — split into words

`split()` cuts a string into pieces based on a separator.  
By default, it splits on spaces:

```python
sentence = "I drink coffee"
words = sentence.split()

print(words)        # ["I", "drink", "coffee"]
```

You can also choose your own separator:
```python
data = "coffee,tea,juice"
drinks = data.split(",")

print(drinks)       #  ["coffee", "tea", "juice"]
```

This is extremely useful when reading user input, processing text, or handling data from files.

## 6. Exercises!

*I'll give you output files for every exercise, check if you have the right answers in your terminal!*

#### Exercise 1

Given the list `[4, 9, 2, 7, 5]`, display the output of each line:
- the first value.
- the second to last value *(use a negative index)*.
- every value except the first and last one *(use a positive index then a negative index)*.

#### Exercise 2

Start with the following `drinks` list : `["coffee", "tea", "water"]`  
Do the following steps in order, and display at each end of step:
1. Change the 2nd value to `"juice"`.
2. Add `milk` at the end of the list using `append()`.
3. Remove `coffee` using `remove()`.
4. Remove the value at index `1` using `pop()`, store it in a variable named `removed`, and print the variable.

*Observe how the list changes with every modification you do!*

#### Exercise 3

Given the variable `sentence = "I like coffee"`:
1. Turn it into a list of words using `split()` and display it.
2. Grab the last word, put it in a variable named `word` and display it.
3. Create a list `characters` from the variable `word` using `list()` and display it.
4. Display the length of that list in two different ways:
    - using the list `characters`
    - using the string `word`