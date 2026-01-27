
# Conditions

## 1. Introduction

You might want to allow your code to **make decisions**.  
Instead of always doing the same thing, your program can choose **what to do** depending on a value, a comparison..  

It's as if the code would ask itself:  
**If *this* is true, then do *that***

Conditions are **essential** to create interactive programs, react to user input, check values, and control the flow of your script.  
You'll use them everywhere — from simple checks to full program logic.

## 2. Comparisons

Before making decisions, Python needs a way to **compare values**.  
A condition is always based on something that is either `True` or `False`, so we use comparison operators to check if two values match, differ, or how they relate.  

These comparisons are the foundation of every `if` statement, so let's look at the most common ones:
- `==` → equal
- `!=` → not equal
- `<` → strictly less
- `>` → strictly greater
- `<=` → less or equal
- `>=` → greater or equal

Each of these expressions produces a **boolean** (`True` or `False`), which is exactly what an `if` statement needs.

## 3. if / elif / else

Once you can compare values, you can use them inside a condition.  
Python will execute the following block of code **only if the condition is true**, otherwise it'll ignore that block and try the `elif` (means "else if"), or if this fails again, do the `else` block, or simply continues the script.  
Here's how you can write it:

```python
if cond_1:
    # code executed if cond_1 is True

elif cond_2:
    # executed only if cond_1 is False and cond_2 is True

elif cond_3:
    # executed only if cond_1 and cond_2 is False and cond_3 is True

else:
    # executed only if everything before is False
```

You can combine `if`, or use `if` then `elif` depending on the situation:
- You use multiple `if` if you want your script to execute several blocks
- You use `if` then `elif` if you want your script to do only one block  
  *Be aware that it'll only do the **first** block that is true and skip the next ones until the full `if/elif/else block` is skipped*

For example, if we want to count a score based on a value entered:
```python
# With multiple if, score will be cumulative

answer = 25
score = 0

if answer >= 10:            # This will be True
    score = score + 1
if answer >= 20:            # This will be True
    score = score + 3
if answer >= 30:            # This will be False
    score = score + 5

print(score)
# Final score will thus be 0 + 1 + 3 = 4
```

```python
# With if then elif, score will be selective

# To count from highest score to lowest, we need to pay attention
#   to the order we write the if and elif
#   Here, because we check if it's greater than, we go from biggest to smallest

answer = 25
score = 0

if answer >= 30:            # This will be False
    score = score + 5
elif answer >= 20:          # This will be True
    score = score + 3
elif answer >= 10:          # This one is skipped       
    score = score + 1

print(score)
# Final score will thus be 0 + 3 = 3
```


**Important rules**
- Indentation matters: everything inside the block must be indented
- `elif` is optional
- `else` is optional
- Only the **first** true condition is executed

Here's an example:
```python
x = 10
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Exactly 10")
else:
    print("Less than 10")

# Output is "Exactly 10"
```

**This is the core of decision-making.**

## 4. Combining conditions

Sometimes one condition isn't enough.  
You may want to check **several things at the same time**, or invert a condition.  

Python gives you **three keywords** to combine or modify conditions:
- `and` → both conditions must be True
- `or` → at least one condition must be true
- `not` → reverses a condition

```python
age = 22
country = "US"

if age >= 21 and country == "US":
    print("Adult in US")

if age < 21 or country != "US":
    print("special case")

if not (age == 21):
    print("Age is not exactly 21")
```

These combinations let you create more precise and flexible decisions in your programs.


## 5. Using input()

To make your conditions interactive, you can ask the user for a value using `input()`, and type what will be display in your terminal in the `()`.  

As an example, if you want to ask for a number:
```python
input("Choose a number: ")
# Will display "Choose a number: " and wait for an input
```  

**Important**: `input()` **always return a string**, even if the user types a number.  
If you want to compare numbers, you **must** convert the value:

```python
answer = input("Your age: ")
age = int(answer)
if age >= 20:
    print("You're older than 20!")
else:
    print("You're younger than 20!")
```

## 6. Common mistakes

Here are the most frequent errors when working with conditions:
- Using `=` instead of `==` inside an `if`
- Comparing different types of values
- Forgetting to convert input values (`"20"` vs `20`)
- Missing indentation after `if`, `elif`, `else`
- Forgetting parentheses in complex combined conditions


These small mistakes are normal at the beginning, but easy to avoid once you know them.

## 7. Let's try!

That was a lot of information, but each part is important to really understand how conditions work.

Now it's time to practice with some small exercises using everything you've just learned: comparisons, if/elif/else, combined conditions, and input().

#### Exercise 1

Ask the user a number, and display if it's positive, negative or equal to 0!

*The file `data01.md` can be used for your tests, copy the values and check if the answer displayed is correct!*
___
#### Exercise 2

Ask the user a price, and apply a reduction depending on the value:
- If price is above or equal to `100`USD, apply a reduction of `10%`  
- Otherwise, if price is above or equal to `50`USD, apply a reduction of `5`USD
- Otherwise, if price is above or equal to `20`USD, apply a reduction of `1`USD
  
*You don't have to manage the "USD", simply ask a number and that's it.*  
*Also, we assume that the price is positive or equal to 0.*

*The file`data02.md` can be used for your tests too!*

**Bonus:** Display the value with a f-string!
___
#### Exercise 3

Ask a number, and check if it is **even**, **greater than 10** or both!

*The file `data03.md` can be used for your tests too!*
___
#### Exercise 04

**Challenge time!**

Let's make a small game!  
The program secretly chooses a number (you can pick any number you want).  
Then, ask the user to guess it.

Depending on the guess, display:
- "Too low!" if the guess is smaller
- "Too high!" if the guess is greater
- "Correct!" if it's exactly the same

*For now, you only have one try — we'll fix that later!*
*The file `data04.md` contains one example and different outputs possible!*