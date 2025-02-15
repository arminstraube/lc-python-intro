---
title: "Variables and Assignment"
teaching: 15
exercises: 15
questions:
- "How can I store data in programs?"
- "(David)"
objectives:
- "Write programs that assign values to variables and perform calculations with those values."
- "Correctly trace value changes in programs that use assignment."
keypoints:
- "Use variables to store values."
- "Use `print` to display values."
- "Variables must be created before they are used."
- "Variables can be used in calculations."
- "Use an index to get a single character from a string."
- "Use a slice to get a substring."
- "Use the built-in function `len` to find the length of a string."
- "Python is case-sensitive."
- "Use meaningful variable names."
---
## Use variables to store values.

*   Variables are names for values.
*   In Python the `=` symbol assigns the value on the right to the name on the left.
*   The variable is created when a value is assigned to it.
*   Here, Python assigns an age to a variable `age`
    and a name in quotation marks to a variable `first_name`.

~~~
age = 42
first_name = 'Ahmed'
~~~
{: .python}

*   Variable names:
    *   cannot start with a digit
    *   cannot contain spaces, quotation marks, or other punctuation
    *   *may* contain an underscore (typically used to separate words in long variable names)
*   Underscores at the start like `__alistairs_real_age` have a special meaning
    so we won't do that until we understand the convention.

## Use `print` to display values.

*   Python has a built-in function called `print` that prints things as text.
*   Call the function (i.e., tell Python to run it) by using its name.
*   Provide values to the function (i.e., the things to print) in parentheses.
*   To add a string to the printout, wrap the string in single quotations.
*   The values passed to the function are called 'arguments'

~~~
print(first_name, 'is', age, 'years old')
~~~
{: .python}
~~~
Ahmed is 42 years old
~~~
{: .output}

*   `print` automatically puts a single space between items to separate them.
*   And wraps around to a new line at the end.

## Variables must be created before they are used.

*   If a variable doesn't exist yet, or if the name has been mis-spelled,
    Python reports an error.
    *   Unlike some languages, which "guess" a default value.

~~~
print(eye_color)
~~~
{: .python}
~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-c1fbb4e96102> in <module>()
----> 1 print(eye_color)

NameError: name 'eye_color' is not defined
~~~
{: .error}

*   The last line of an error message is usually the most informative.
*   We will look at error messages in detail [later]({{ page.root }}/05-error-messages/).

## Variables can be used in calculations.

*   We can use variables in calculations just as if they were values.
    *   Remember, we assigned 42 to `age` a few lines ago.

~~~
age = age + 3
print('Age in three years:', age)
~~~
{: .python}
~~~
Age in three years: 45
~~~
{: .output}

## Use an index to get a single character from a string.

*   The characters (individual letters, numbers, and so on) in a string are
    ordered. For example, the string 'AB' is not the same as 'BA'. Because of
    this ordering, we can treat the string as a list of characters.
*   Each position in the string (first, second, etc.) is given a number. This
    number is called an index or sometimes a subscript.
*   Indices are numbered from 0 rather than 1.
*   Use the position's index in square brackets to get the character at that
    position.

~~~
element = 'helium'
print(element[0])
~~~
{: .python}
~~~
h
~~~
{: .output}

## Use a slice to get a substring.

*   A part of a string is called a substring. A substring can be as short as a
    single character.
*   An item in a list is called an element. Whenever we treat a string as if it
    were a list, the string's elements are its individual characters.
*   A slice is a part of a string (or, more generally, any list-like thing).
*   We take a slice by using `[start:stop]`, where `start` is replaced with the
    index of the first element we want and `stop` is replaced with the index of
    the element just after the last element we want.
*   Mathematically, you might say that a slice selects `[start:stop]`.
*   The difference between stop and start is the slice's length.
*   Taking a slice does not change the contents of the original string. Instead,
    the slice is a copy of part of the original string.

~~~
element = 'sodium'
print(element[0:3])
~~~
{: .python}
~~~
sod
~~~
{: .output}

## Use the built-in function `len` to find the length of a string.

~~~
print(len('helium'))
~~~
{: .python}
~~~
6
~~~
{: .output}

*   Nested functions are evaluated from the inside out,
    just like in mathematics.

## Python is case-sensitive.

*   Python thinks that upper- and lower-case letters are different,
    so `Name` and `name` are different variables.
*   There are conventions for using upper-case letters at the start of variable names
    so we will use lower-case letters for now.

## Use meaningful variable names.

*   Python doesn't care what you call variables as long as they obey the rules
    (alphanumeric characters and the underscore).

~~~
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')
~~~
{: .python}

*   Use meaningful variable names to help other people understand what the program does.
*   The most important "other person" is your future self.

> ## Swapping Values
>
> Draw a table showing the values of the variables in this program
> after each statement is executed.
> In simple terms, what do the last three lines of this program do?
>
> ~~~
> x = 1.0
> y = 3.0
> swap = x
> x = y
> y = swap
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > swap = x  #  x->1.0 y->3.0 swap->1.0
> > x = y     #  x->3.0 y->3.0 swap->1.0
> > y = swap  #  x->3.0 y->1.0 swap->1.0
> > ~~~
> > These three lines exchange the values in `x` and `y` using the `swap`
> > variable for temporary storage. This is a fairly common programming idiom.
>{: .solution}
{: .challenge}

> ## Predicting Values
>
> What is the final value of `position` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
>
> ~~~
> initial = "left"
> position = initial
> initial = "right"
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > initial = "left"  # Initial is assigned the string "left"
> > position = initial  # Position is assigned the variable initial, currently "left"
> > initial = "right"  # Initial is assigned the string "right"
> > print(position)
> > ~~~
> > {: .python}
> > ~~~
> > left
> > ~~~
> > {: .output}
> > The last assignment to position was "left"
>{: .solution}
{: .challenge}

> ## Choosing a Name
>
> Which is a better variable name, `m`, `min`, or `minutes`?
> Why?
> Hint: think about which code you would rather inherit
> from someone who is leaving the library:
>
> 1. `ts = m * 60 + s`
> 2. `tot_sec = min * 60 + sec`
> 3. `total_seconds = minutes * 60 + seconds`
>
> > ## Solution
> >
> > `minutes` is better because `min` might mean something like "minimum"
> > (and actually does in Python, but we haven't seen that yet).
> {: .solution}
{: .challenge}

> ## Slicing
>
> What does the following program print?
>
> ~~~
> library_name = 'social sciences'
> print('library_name[1:3] is:', library_name[1:3])
> ~~~
> {: .python}
>
> 1.  What does `thing[low:high]` do?
> 2.  What does `thing[low:]` (without a value after the colon) do?
> 3.  What does `thing[:high]` (without a value before the colon) do?
> 4.  What does `thing[:]` (just a colon) do?
> 5.  What does `thing[number:negative-number]` do?
>
> > ## Solution
> > ~~~
> > library_name[1:3] is: oc
> > ~~~
> > {: .output}
> > 1.  It will slice the string, starting at the `low` index and ending an element before the `high` index
> > 2.  It will slice the string, starting at the `low` index and stopping at the end of the string
> > 3.  It will slice the string, starting at the beginning on the string, and ending an element before the `high` index
> > 4.  It will print the entire string
> > 5.  It will slice the string, starting the `number` index, and ending a distance of the absolute value of `negative-number` elements from the end of the string
> {: .solution}
{: .challenge}

> ## Can you slice a number?
>
> If you assign `a = 123`,
> what happens if you try to get the second digit of `a`?
>
> > ## Solution
> > Numbers are not stored in the written representation,
> > so they can't be treated like strings.
> >
> > ~~~
> > a = 123
> > print(a[1])
> > ~~~
> > {: .python}
> > ~~~
> > TypeError: 'int' object is not subscriptable
> > ~~~
> > {: .error}
> {: .solution}
{: .challenge}
