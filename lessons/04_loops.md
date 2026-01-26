# Loops in Python

## Introduction

Until now, every instruction in your code was executed once, in order.  
But what if you want to repeat something? What if you want to run the same action 5 times, 10 times… or until a condition is met?

You *could* copy‑paste the same line again and again…  
…but that would be terrible. And impossible for anything dynamic.

That's where **loops** come in.

Loops allow your program to repeat actions:
- a specific number of times  
- or until something happens  

We'll start with the `for` loop, perfect when you *know* how many times to repeat.  
Then we'll see the `while` loop, perfect when you *don't know* yet.

Finally, we'll look at `break` and `continue` to control your loops more precisely.

## The `for` loop

Sometimes, you know exactly how many times you want to repeat something.  
For example, you could print something 5 times, count from 1 to 10 or go through a list of items.

That's what the `for` loop is for.

A `for` loop repeats once for every element in a sequence.  
For now, the most common sequence you'll use is `range()`:

```python
for i in range(5):
    print("Hello!")
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
```

This will print "Hello!" five times. The variable `i` takes each value from the sequence, one by one.  

## `range()`

The `range()` function creates a sequence of numbers. It's most often used with `for` loops.

You can use it in different ways:
- range(n)
  → loop that goes from `0` to `n-1`

```python
for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
```

- range(start, end)
  → Create numbers from `start` to `end-1`

```python
for i in range(3,7):
    print(i)
# 3
# 4
# 5
# 6
```

- range(start,end,step)
  → Create numbers from `start` to `end-1`, with a given `step`

  
```python
for i in range(0, 10, 2):
    print(i)
# 0
# 2
# 4
# 6
# 8
```

You can even use negative steps!
```python
for i in range(5,0,-1):
    print(i)
# 5
# 4
# 3
# 2
# 1
```

## Let's train the `for` loops!

Now that you know how `for` and `range()` work, let's practice!  
*I don't think you'll need any example file for math like this*

#### Exercise 1

Ask a number `x` and display its multiplication table from 0 to 10 (included)!

#### Exercise 2

Ask a number `n` and display the sum of every number from 1 to `n` (included)!

#### Exercise 3

Improve!  
Ask two numbers `a` and `b` and compute the sum of every number between both (included)!
Then, do it again, but this time count from `b` to `a` (included)!

## The `while` loop

The `for` loop is perfect when you *know* how many times you want to repeat something.  
But sometimes, you don't know yet.  
Maybe you want to repeat something:
- until a number reaches a certain value
- until the user types something calid
- until a condition becomes fales

That's what the `while` loop is for.

A `while` loop repeats **as long as a condition is true**.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
# 1
# 2
# 3
# 4
# 5
```

Unlike a `for` loop, you **must update the variable yourself**, or the loop never ends.

If the condition never becomes false, the loop never stops:

```python
while True:
    print("Still running!")
```

This is called an **infinite loop**.
Useful sometimes, but dangerous if accidental.

*Just in case you find yourself in an infinite loop, you can press `Ctrl` + `C` at the same time to stop the program (works in most terminals)*

## Let's try the `while` loops

Now that you saw how `while` loops work, let's use them!

#### Exercise 4

Let's try to redo the exercise 2, but with a while loop!
Ask a number `n` and display the sum of every number from 1 to `n` (included)!

#### Exercise 5

Now, same as exercise 3, but with a while loop!  
Ask two numbers `a` and `b` and compute the sum of every number between both (included)!
Then, do it again, but this time count from `b` to `a` (included)!

#### Exercise 6

Ask for a number, and count until the number becomes odd!
- If the number is even, divide it by 2 and display the result and continue
- If the number is odd, display the result and stop the loop