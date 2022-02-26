# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:23:18 2022

@author: Account
"""


"""Exercises about Variables and Assignment"""

#Swapping Values - Explain what is happening
x = 1.0
y = 3.0
swap = x
x = y
y = swap

#Predicting Values - 
# What is the final value of position in the program below? 
# Try to predict the value before running the program.
initial = "left"
position = initial
initial = "right"
print(position)

#Choosing a name
# Which is a better variable name and why?
# ts = m * 60 + s
# tot_sec = min * 60 + sec
# total_seconds = minutes * 60 + seconds

#Slicing
# What does the following program print and why?
library_name = 'social sciences'
print('library_name[1:3] is:', library_name[1:3])

# What does thing[low:high] do?
# What does thing[low:] (without a value after the colon) do?
# What does thing[:high] (without a value before the colon) do?
# What does thing[:] (just a colon) do?
# What does thing[number:negative-number] do?

#Can you slice a number?
# Try to get the second digit of "a"
a = 123



"""Exercises about Data Types and Type Conversion"""

#Conversions (or typecasts)
# What do you expect the following program to do and why?
print("fractional string to int:", int("3.4"))

#Fractions
# What type of value is 3.4? How can you find out?

#Automatic Type Conversion
# What type of value is 3.25 + 4?

#Choose a Type
# What type (integer, floating point, string) would you use and why?
# 1.Number of days since the start of the year.
# 2.Time elapsed since the start of the year.
# 3.Title of a book.
# 4.Standard book loan period.
# 5.Number of reference queries in a year.
# 6.Average classes taught per semester.

#Arithmetic with Different Types
first = 1.0
second = "1"
third = "1.1"
# Which of the following will prints 2.0 and why?
# There may be more than one right answer.
# 1. first + float(second)
# 2. float(second) + float(third)
# 3. first + int(third)
# 4. first + int(float(third))
# 5. int(first) + int(float(third))
# 6. 2.0 * second

#Division
# Normal division(operator:"/"): 5 / 2 = 2.5
# Floor division (operator:"//") cuts out the part after the period): 5 / 2 = 2
# Modulo division (operator:"%") only keeps the remainder: 5 / 2 = 1
# Try:
print('5 / 3:', 5/3)
print('5 // 3:', 5//3)
print('5 % 3:', 5%3)

# Write an expression that calculates the number of classes needed.
# How many full classes, how many students are in the last (not full) class?
num_students = 600 #total number of students
num_per_class = 42 # maximum number of students in one class



"""Exercises about Built-in Functions and Help"""

#What Happens When
# Explain what happens when and why. What is the final value of word? 
word = 'blah '
word = max(min(word * 2 + 'blur ', 'aaah '), 'ping')
print(word)

#Spot the Difference
# Predict what the two print statements in the program below will print.
# Explain why. 
richer = "gold"
poorer = "tin"
print(max(richer, poorer))
print(max(len(richer), len(poorer)))



"""Exercises about Libraries"""

#When Is Help Available?
# Try to get help about the os Library (gives operating system functions):
help(os)
# Why do you get an error?

#Exploring the os Library 
# What function from the os library can determine the working directory?

#Many Ways To Import Libraries
# Match the following library calls and print statements
    # Library calls:
        # A) from string import digits
        # B) import string
        # C) import string as s
    # Print commands:
        # 1. print(list(s.digits))
        # 2. print(list(digits))
        # 3. print(string.ascii_uppercase)

#Reading Error Messages 
# What type of error do you get with this code and why?
import datetime
datetime.date(2022,18,2)

"""Exercises about Lists"""

#Fill in the blanks so that the program below produces the output shown:
values = ____
values.____(1)
values.____(3)
values.____(5)
print('first time:', values)
values = values[____]
print('second time:', values)
#Output:
# first time: [1, 3, 5]
# second time: [3, 5]

#From Strings to Lists and Back
# Explain what list('some string') does.
# What does '-'.join(['x', 'y']) generate?
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))

#Working with the End
# What does the following program print?
element = 'helium'
print(element[-1])
# 1. How does Python interpret a negative index?
# 2. If a list or string has N elements: 
#    What is the most negative index that can safely be used with it? 
#    What location does that index represent?
# 3. If values is a list, what does del values[-1] do?
# 4. How can you display all elements but the last one without changing values? 
# (Hint: you will need to combine slicing and negative indexing.)

#Stepping Through a List
# The following adheres to the structure "low:high:stride". 
# What does "stride" do if you run:
element = 'fluorine'
print(element[::2])
print(element[::-1])


"""Exercises about For Loops"""

#Is an indentation error a syntax error or a runtime error?

#Reversing a String
# Fill in the blanks in the program below so that it prints “nit” 
# (Hint: Think about the order in which to put the result back together)
original = "tin"
result = ____
for char in original:
    result = ___ + ___
    print(result)


"""Exercises about Conditionals"""

#Tracing Execution
# What does this program print?
pressure = 71.9
if pressure > 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)

#Trimming Values
# Fill in the blanks so that this program creates a new list with
# - zeroes where the original list’s values were negative and 
# - ones where the original list’s values were positive.
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)


"""Exercises about Writing Functions"""

#Definition and Use
# What does the following program print?
def report(pressure):
    print('pressure is', pressure)

report(22.5)

#Calling by Name
# What does this short program print?
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(day=18, month=2, year=2022)



"""Solutions"""

# This script belongs to: https://arminstraube.github.io/lc-python-intro
# Solutions and further exercises can be found there 