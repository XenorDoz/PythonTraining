# Lists, tuples & Dictionaries

Working with a single value is useful, but very limiting.  
Often, you need to store **multiple pieces of data** at the same time: several numbers, several words... And a single variable isn't enough for that.

That's where **lists** come in.

A list lets you store **many values inside one variable**, keep them organized, and access or modify them easily.

# 1. How to define a list

A list is created using square brackets `[]`.  
It can contain one value, several values, or even be completely empty.  
Lists are extremely flexible: they can store numbers, strings, booleans, or even a mix of different types.  


### Empty list

You can start with an empty list and fill it later:

```python
my_list = []
```

This is useful when you don't know the values yet, or when you want to build the list step by step.

### List with values

You can also define a list directly with elements inside the brackets:

```python
numbers = [3, 7, 10]
words = ["apple","banana", "cherry"]
```

Each value is **separated by a comma**.  
Python keeps them in the order you write them.

### Mixed types

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

# 2. How to read a list

Once you have a list, you can access any value inside it using its **index**.  
An index is the position of an element in the list.

### Indexes start at 0

In Python, the first element is at index `0`, the second at index `1`, and so on.

You can access any value by using its index, like this:
```python
numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[1])   # 20
print(numbers[2])   # 30
print(numbers[3])   # 40
```

If you try to access an index that doesn't exist, Python will show an **"Index out of range"** error.  
Don't worry — just make sure that you're staying within the bounds of the list!

### Negative indexes

You can also read values starting from the end of the list:

- `-1` → last element
- `-2` → second to last
- etc.

```python
print(numbers[-1])  # 40
print(numbers[-2])  # 30
```

This is very useful when you want the last value without knowing the list's size.

### Slicing: reading multiple values at once

You can read a part of the list using the slicing syntax:
- `my_list[start:end]` → from `start` to `end - 1`
- `my_list[:]` → the whole list (a copy)

```python
print(numbers[1:3]) # [20, 30]
print(numbers[:])   # [10, 20, 30, 40]
```

Slicing never raises an error, even if the slices goes beyond the list boundaries.

### The `len()` function

`len()` returns the number of elements in the list:

```python
print(len(numbers)) # 4
```

This helps you avoid going out of range, and it's often used in loops.

# 3. How to modify a list

Lists are **mutable**, which means you can change their content at any moment.  
You can replace values, add new ones, or remove existing ones.  
This flexibility is one of the main reasons lists are so useful.

### Changing a value

You can replace an element by assigning a new value to its index:

```python
numbers = [10, 20, 30, 40]

numbers[1] = 99
print(numbers)  # [10, 99, 30, 40]
```

Python updates the list immediately.

### Adding a value: `append()`

`append()` adds a new element **at the end** of the list.

```python
items = ["coffee", "tea"]
items.append("water")

print(items)    # ["coffee", "tea", "water"]
```

This is the most common way to add new elements a list.

### Removing a value: `remove()`

`remove()` deletes **the first occurrence** of a value.

```python
drinks = ["coffee", "tea", "water", "juice"]
drinks.remove("tea")

print(drinks)   # ["coffee", "water", "juice"]
```

If the value appears multiple times, only the first one is removed.  
If the value doesn't exist, Python will show an error.

### Removing by index: `pop()`

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

# 4. Strings behave like lists

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

### But strings are immutable

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

# 5. Transforming strings into lists

Sometimes you want to work with a string as *if it were a list*.  
Python gives you two useful tools for that. 

### `list()` — split into characters

`list()` converts a string into a list of individual characters:

```python
word = "coffee"
chars = list(word)

print(chars)        # ["c", "o", "f", "f", "e", "e"]
```

This is useful when you need to inspect or manipulate each character separately.

### `split()` — split into words

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

# 6. Exercises!

*I'll give you output files for every exercise, check if you have the right answers in your terminal!*

### Exercise 1

Given the list `[4, 9, 2, 7, 5]`, display the output of each line:
- the first value.
- the second to last value *(use a negative index)*.
- every value except the first and last one *(use a positive index then a negative index)*.
___
### Exercise 2

Start with the following `drinks` list : `["coffee", "tea", "water"]`  
Do the following steps in order, and display at each end of step:
1. Change the 2nd value to `"juice"`.
2. Add `milk` at the end of the list using `append()`.
3. Remove `coffee` using `remove()`.
4. Remove the value at index `1` using `pop()`, store it in a variable named `removed`, and print the variable.

*Observe how the list changes with every modification you do!*
___
### Exercise 3

Given the variable `sentence = "I like coffee"`:
1. Turn it into a list of words using `split()` and display it.
2. Grab the last word, put it in a variable named `word` and display it.
3. Create a list `characters` from the variable `word` using `list()` and display it.
4. Display the length of that list in two different ways:
    - using the list `characters`
    - using the string `word`
  
# 7. Tuples

Sometimes you want a sequence of values, just like a list, but you want to make sure **nobody can modify it**.

That's what **tuples** are for.

A tuple is almost the same as a list, except for one key difference: **tuples are immutable**.  
You cannot add, remove, or change elements once the tuple is created.

### Defining a tuple

A tuple uses **parentheses** instead of brackets:

```python
numbers = (10, 20, 30)
words = ("coffee", "tea", "water")
```

You can also mix types:

```python
mixed = (10, "hello", True)
```

A tuple with a single value needs a comma:

```python
single = (42,)
```

Without the comma, Python thinks it's just a number.

### Reading a tuple

Tuples behave exactly like lists for reading:
- `tuple[0]` → first element
- `tuple[-1]` → last element
- `tuple[1:3]` → slicing
- `len(tuple)` → number of elements  

Everything you learned about **reading** a list also works with tuples.

### Why use tuples?

Tuples are useful when:
- The data should **never change**
- You need a sequence that is **faster** and **lighter** than a list
- You want to use the sequence as a **dictionary key**
  
Tuples are perfect for fixed data like coordinates, dates, RGB colors...

# 8. Dictionaries

Lists and tuples let you store multiple values, but you always access them using **indexes**.  
Sometimes, this is not what you want. What if you want to access a value using a **name** instead of a number ?  
That's exactly what **dictionaries** are for.

A dictionary stores data as **key → value** pairs.  
You choose the key, and Python gives you the value.

It works just like a real dictionary: you look up a word (the key) to get its definition (the value).

### Defining a dictionary

A dictionary uses **curly braces** `{}` and contains pairs separated by commas.  
Each pair has:
- a **key** (usually a string, but can be anything)
- a **value** (anything you want)

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
    }
```

Keys must be **unique**.  
If you repeat a key, the last value replaces the previous one.

Values can be: 
- numbers
- strings
- lists
- dictionaries
- booleans
- anything

### Reading values from a dictionary 

You access a value using its key:

```python
print(person["name"])   # Alice
print(person["age"])   # 25
```

If the key doesn't exist, Python shows a **KeyError**.  
To avoid errors, you can use `get()`:

```python
print(person.get("job"))    # None
```

`get()` returns `None` instead of crashing.

### Modifying a dictionary

Dictionaries are **mutable**, just like lists.  
You can change a value:

```python
person["age"] = 26
```

You can add a new key:

```python
person["job"] = "developer"
```

Python updates the dictionary immediately.

### Removing values

You can remove a key using `pop()`:

```python
person.pop("city")
```

This removes the key and returns its value.

You can remove everything using `clear()`:

```python
person.clear()
```

### Checking if a key exists

You can test if a key is present:

```python
"name" in person    # True
"salary" in person  # False
```

This is extremely useful when processing user input or external data.

### Why use dictionaries?

Dictionaries are perfect when:
- you want to store **structured data**
- you want to access values by **name**, not by index
- you need fast lookups
- you want to group related information
  
They are used everywhere in Python:
- JSON files
- APIs
- configurations
- databases
- user profiles
- game objects
  
Here's how you would represent a player for example:
```python
player = {
    "name": "Xen",
    "level": 12,
    "hp": 87,
    "coords": (13, 42),
    "inventory": ["sword", "potion", "shield"]
}
```

This is much clearer than using a list like:

```python
["Xenor", 12, 87, (13, 42),["sword", "potion", "shield"]]
```

# 9. Last exercises!

### Exercise 4

Given the tuple:  
`coords = (12, 5, 9, 3, 5, 12)` 

Do the following:
1. Display the first value and the last value.
2. Display the length of the tuple using `len()`.
3. Display all values except the first two (use slicing).
4. Display how many times the value `12` appears in the tuple (hint: use `tuple.count()`).
___
### Exercise 5

Start with the dictionary:
`player = {"name": "Alex", "level": 3, "hp": 20}`  
Do the following steps in order, and display the dictionary after each one:
1. Change the `"level"` value to `4`
2. Add a new key `"weapon"` with the value `"sword"`
3. Remove the key `"hp"` using `pop()`, store the removed value in a variable named `removed_hp`, and display it.
4. Check if the key `"armor"` exists in the dictionary and display the result.
___
### Exercise 6

You are given the following dictionary representing temperatures on a grid:

```python
temps = {
    (0, 0): 12,
    (0, 1): 14,
    (1, 0): 15
}
```

Do the following:
1. Display the temperature at position `(0, 1)`
2. Add a new temperature at position `(1, 1)` with the value `18`
3. Replace the temperature at position `(0,0)` with `10`
4. Display all the keys from the dictionary (hint: use `temps.keys()`)
___
### Exercise 7

Given the following data:

```python
students = [
    ("Alice", 15),
    ("Bob", 12),
    ("Charlie", 17)
]
```

Do the following:
1. Create a dictionary named `grades` where each key is the student's name and each value is their grade.
2. Display the grade of `"Charlie"` from the dictionary.
3. Add a new student `"Diana"` with grade `14` in the dictionary.