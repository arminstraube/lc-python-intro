# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:51:43 2022

@author: Account
"""


"""Let´s get started"""

print('Hello world!')



"""Variables and Assignment"""

#Use variables to store values.
age = 42
first_name = 'Ahmed'

#Use "print" to display values.
print(first_name, 'is', age, 'years old')

#Variables must be created before they are used.
print(eye_color)

#Variables can be used in calculations.
age = age + 3
print('Age in three years:', age)

#Use an index to get a single character from a string.
element = 'helium'
print(element[0])

#Use a slice to get a substring.
element = 'sodium'
print(element[0:3])

#Use the built-in function "len" to find the length of a string.
print(len('helium'))

#Use meaningful variable names 
# Python is case sensitive. Always use lower-case for variable names
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')

#---->Go to exercises about Variables and Assignment



"""Data Types and Type Conversion"""

#Every value has a type.

#Use the built-in function "type" to find the type of a value.
print(type(52))

title = 'Biochemistry'
print(type(title))

#Types control what operations (or methods) can be performed on a given value.
print(5 - 3)
print('hello' - 'h')

#You can use the + and * operators on strings.
full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)

separator = '=' * 10
print(separator)

#Strings have a length (but numbers don’t).
print(len(full_name))
print(len(52))

#Must convert numbers to strings or vice versa when operating on them.
print(1 + 'A')

print(1 + int('2'))
print(str(1) + '2')

#Can mix integers and floats freely in operations.
print('half is', 1 / 2.0)
print('three squared is', 3.0 ** 2)

#Variables only change value when something is assigned to them.
first = 1
second = 5 * first
first = 2
print('first is', first, 'and second is', second)

#Strings to Numbers
print("string to float:", float("3.4"))
print("float to int:", int(3.4))

print("string to float:", float("Hello world!"))

#---->Go to exercises about Data Types and Type Conversion



"""Built-in Functions and Help"""

#Use comments to add documentation to programs.
# This sentence isn't executed by Python.
name = 'Library Carpentry'   # Anything after '#' is ignored.

#A function may take zero or more arguments.
print("I am an argument and must go here.")

print('before')
print()
print('after')

#Commonly-used built-in functions
print(max(1, 2, 3))
print(min('a', 'b', 'c'))
print(min('a', 'A'))

#Functions may only work for certain (combinations of) arguments.
print(max(1, 'a'))

#Functions may have default values for some arguments.
round(3.712)
round(3.712, 1)

#Use the built-in function "help" to get help for a function.
help(round)

#Python reports a syntax error when grammar rules have been violated.
# Forgot to close the quotation marks around the string.
name = 'Feng 

# An extra '=' in the assignment.
age = = 52 

print("hello world"

#Runtime error when something goes wrong while a program is executing.
age = 53
# mis-spelled 'age'
remaining = 100 - aege 

#---->Go to exercises about Built-in Functions and Help



"""Libraries"""

#Most of the power of a programming language is in its (software) libraries.
# Python standard library: https://docs.python.org/3/library/
# Additional libraries at the Python Package Index (PyPI): https://pypi.org/

#A program must import a library module before using it.
import string
print('The lower ascii letters are', string.ascii_lowercase)
print(string.capwords('capitalise this sentence please.'))

#Use "help" to learn about the contents of a library module.
help(string)

#Create an alias for a library module when importing it to shorten programs.
import string as s
print(s.capwords('capitalise this sentence again please.'))

#Import specific items from a library module to shorten programs.
from string import ascii_letters
print('The ASCII letters are', ascii_letters)

#---->Go to exercises about Libraries



"""Lists"""

#A list stores many values in a single structure.
temperatures = [17.3, 17.5, 17.7, 17.5, 17.6]
print('temperatures:', temperatures)
print('length:', len(temperatures))

#Use an item’s index to fetch it from a list.
print('first item of temperatures:', temperatures[0])
print('fifth item of temperatures:', temperatures[4])

#Lists’ values can be replaced by assigning to them.
temperatures[0] = 16.5
print('temperatures is now:', temperatures)

#Appending items to a list lengthens it.
# append() below is a method. Methods work much like functions. 
# Methods must be called on an object (like this list here)  
print('temperatures is initially:', temperatures)
temperatures.append(17.9)
temperatures.append(18.2)
print('temperatures has become:', temperatures)

#More methods for lists
help(list)

#Use "del" to remove items from a list entirely.
primes = [2, 3, 5, 7, 11]
print('primes before removing last item:', primes)
del primes[4]
print('primes after removing last item:', primes)

#List can be empty (contain no value).

#Lists may contain values of different types.
goals = [1, 'Create lists.', 2, 'Extract items', 3, 'Modify lists.']

#Character strings can be indexed like lists.
element = 'carbon'
print('first character:', element[0])
print('fourth character:', element[3])

#Character strings are immutable.
element[0] = 'C'

#Indexing beyond the end of the collection is an error.
print('99th element of element is:', element[99])

#---->Go to exercises about Lists



"""For Loops"""

#A for loop executes commands once for each value in a collection.
for number in [2, 3, 5]: 
    print(number)

#The first line must end with a colon, and the body must be indented.

#Indentation is always meaningful in Python.
for number in [2, 3, 5]:
print(number)

firstName="Jon"
  lastName="Smith"

#A for loop is made up of a collection, a loop variable, and a body.
for number in [2, 3, 5]:
    print(number)

#Loop variable names follow the normal variable name conventions.

#The body of a loop can contain many statements.
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)

#Use "range" to iterate over a sequence of numbers.
print('a range is not a list: range(0, 3)')
for number in range(0,3):
    print(number)

#Or use "range" to repeat an action an arbitrary number of times.
for number in range(5):
    print("Again!")
    
#The Accumulator pattern turns many values into one.    
# Sum the first 10 integers.
total = 0
for number in range(10):
   total = total + (number+1)
print(total)    
    
#---->Go to exercises about For Loops


"""Conditionals"""

#Use "if" statements to control whether or not a block of code is executed.
mass = 3.54
if mass > 3.0:
    print(mass, 'is larger')

mass = 2.07
if mass > 3.0:
    print (mass, 'is larger')

#Conditionals are often used inside loops.
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is larger')

#Use "else" to execute a block of code when an if condition is not true.
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for mass in masses:
    if mass > 3.0:
        print(mass, 'is larger')
    else:
        print(mass, 'is smaller')

#Use "elif" to specify additional tests.
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for mass in masses:
    if mass > 9.0:
        print(mass, 'is HUGE')
    elif mass > 3.0:
        print(mass, 'is larger')
    else:
        print(mass, 'is smaller')

#Conditions are tested in order and the process stops if a condition matches
grade = 85
if grade >= 70:
    print('grade is C')
elif grade >= 80:
    print('grade is B')
elif grade >= 90:
    print('grade is A')

#Conditionals are often used in a loop to evolve the values of variables.
velocity = 10.0
for i in range(5): # execute the loop 5 times
    print(i, ':', velocity)
    if velocity > 20.0:
        print('moving too fast')
        velocity = velocity - 5.0
    else:
        print('moving too slow')
        velocity = velocity + 10.0
print('final velocity:', velocity)

# Combine relations using "and" and "or" 
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa! Some other combination!")
        
#Use parentheses to avoid ambiguity when mixing "and and "or"
if mass[i] <= 2 or mass[i] >= 5 and velocity[i] > 20: # ambiguous
if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20: # alternative 1
if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20): # alternative 2

#---->Go to exercises about Conditionals


"""Writting Functions"""

#Break programs down into functions to make them easier to understand.

#Define a function using "def" with a name, parameters, and a block of code.
def print_greeting():
    print('Hello!')

#Defining a function does not run it.
print_greeting()

#Arguments in call are matched to parameters in definition.
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)

#Functions may return a result to their caller using "return"

def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)

a = average([1, 3, 4])
print('average of actual values:', a)

print('average of empty list:', average([]))


#The scope of a variable is the part of a program that can ‘see’ that variable.
# In the following "pressure" is a global variable. 
# "t" and "temperature" are local variables in "adjust"

pressure = 103.9

def adjust(t):
    temperature = t * 1.43 / pressure
    return temperature

print('adjusted:', adjust(0.9))
print('temperature after call:', temperature)

#---->Go to exercises about Writing Functions



"""Ressources"""

# Style Guide for Python Code: https://www.python.org/dev/peps/pep-0008/
# Python standard library: https://docs.python.org/3/library/
# Additional libraries at the Python Package Index (PyPI): https://pypi.org/

# This script belongs to: https://arminstraube.github.io/lc-python-intro
