#!/usr/bin/python3
"""Check if someone is on pension or not"""

age = int(input("What's your age: "))

if (age < 60):
    print("You must be working now")
else:
    print("You must be on pension now")
