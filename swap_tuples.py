#!/usr/bin/python3
"""Swapping 2 numbers"""
a = 10
b = 20

# swap the values of a and b
# b = 10, a = 20

temp = a   # temp = 10
a = b      # a = 20
b = temp   # b = 10

print(f" a = {a} and b = {b}")

# use tuples to swap the numbers
a, b = b, a

print(f" a = {a} and b = {b}")
