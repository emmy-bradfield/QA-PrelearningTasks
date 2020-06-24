# QA Pre-Learning: Python Exercises

Below are three Python exercises designed to test your Python knowledge and problem-solving skills. You should be aware of all of the syntax required to complete these through the Cloud Academy course you have been assigned, but some extra research into additional functions may help you.

The purpose of these exercises is to help you get familiar with solving Python problems and using Git.

## Instructions

There are 3 tasks in this repository designed for you to complete before you begin your training with QA to get you familiar with Python. All of these foundation tasks should be completed **before** you begin your training. They can be found in the `tasks` folder.

Each task has a corresponding stretch goal that gets you to design a more advanced implementation of the foundation task. We encourage you to attempt these as they will put you in good stead for your time in the academy, but should only be attempted once you've completed the foundation tasks. They can be viewed by clicking on the 'Stretch Goal' drop-down buttons for each task. Enter these solutions in the .py files in the `stretch-goals` folder.

To complete these exercises:

1. Fork this repository to your GitLab account
2. Clone your forked repository to your local machine
3. Each of the tasks has a corresponding .py file, specifying where you should enter your code – enter the code solution within the section marked with:
   ```
   # ==============
   # Your code here

   # ==============
   ```

4. When you want to check your code works, perform the following git commands:
   - `git add .` (add any new changes)
   - `git commit -m "pushing for validation"` (commit new changes to your local branch)
   - `git push` (push the changes to the GitLab repository)
5. You must have attempted these three exercises and pushed solutions to your personal GitLab account before you start the Academy.

### If you do not have access to Python 3 Environment

You can still complete this task by making use of the Browser integration with GitLab, and by using a Python 3 REPL such as:

https://repl.it/@enaard/Python-3

## Exercises

### Vowel Swapper

Create a function that accepts a string as an argument and swaps vowels with a corresponding symbol, such that:
- `a` becomes `4`
- `e` becomes `3`
- `i` becomes `!`
- `o` becomes `ooo`
- `u` becomes `|_|`

The vowel swapper should recognise and change lowercase and capital letters the same way, with the exception of `o`: capital `O` should be changed to `000` (zeroes).

The function should return the result as a string.

Examples:
```
print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
```

<details>
<summary>Hint</summary>
Look up the replace() method.
</details>

<details>
<summary>Stretch Goal</summary>

Adapt the function so that **only** the *second* instance of a given vowel in a string is swapped with a symbol.

Examples:
```
print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a4a e3e i!i o000o u|_|u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av4!lable" to the console
```
</details>

### Factors

Create a function that takes a positive integer `number` and returns a list of all of its factors – all the numbers that divide into the input without any remainders.

The output should be a list of integer values and should not include 1 or the input `number`.

If you need a refresher on what factors are and how to find them, here's a good video: https://www.youtube.com/watch?v=vcn2ruTOwFo

**Examples:**
```
print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print [] (an empty list) to the console
```

<details>
<summary>Hint</summary>
You'll need a use a for loop to iterate through every number between 1 and input number. Look up the modulo (%) operator to find remainders.
</details>

<details>
<summary>Stretch Goal</summary>
If the input number doesn’t have any factors, adapt the function so the the output is a string value stating that the input is prime in the format “{number} is a prime number”.

**Examples**
```
print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “13 is a prime number”
```
</details>

### Calculator

Create a function that will take two integer numbers and calculate their value after being added, subtracted, multiplied or divided.

The function should take the following arguments:
- `a` as your first value
- `b` as your second value 
- the operation you want to perform (+, -, *, /) as a string value
Such that the calculation is `a + b`, `a - b`, `a * b`, `a / b`

The output must be an integer value.

**Examples:**
```
print(calculator(2, 4, "+")) # Should print 6 to the console
print(calculator(10, 3, "-")) # Should print 7 to the console
print(calculator(4, 7, "*")) # Should print 28 to the console
print(calculator(100, 2, "/")) # Should print 50 to the console
```

<details>
<summary>Hint</summary>
The operators that are passed through to the function are string values and can't be used as the operator values themselves. You'll need some `if` statements to decide what sum is going to take place based on what the string value is.
</details>

<details>
<summary>Stretch Goal</summary>

Rather than return the answer to the sum as a standard decimal (base 10) number, return the value as a binary (base 2) number. 

The output must be an integer-type binary number that is the answer to this sum. Decimal places should be ignored by the calculator by rounding down, such that 15 / 2 will output 111 (i.e. 7 in binary).

**Examples:**
```
print(calculator(2, 4, "+")) # Should print 110 to the console
print(calculator(10, 3, "-")) # Should print 111 to the console
print(calculator(4, 7, "*")) # Should print 11100 to the console
print(calculator(100, 2, "/")) # Should print 110010 to the console
```
If you're unfamiliar with binary:

- Here’s a handy explanation of what binary numbers are (and why computers use binary, if you’re feeling adventurous):
https://www.howtogeek.com/367621/what-is-binary-and-why-do-computers-use-it/

- Here’s a quick tutorial on how to convert decimal numbers to binary numbers mathematically:
https://www.youtube.com/watch?v=kVvP5MNIND4

</details>

