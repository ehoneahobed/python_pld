#!/usr/bin/python3
"""Prints from 1 to 10"""

counter = 1 # initialization

while (counter <= 10): # condition
    """Will only execute if the condition is true"""
    
    if (counter == 4):
        counter = counter + 1 
        break
    elif (counter == 5):
        print("Five")
    else:
        print(counter)
    counter = counter + 1 # increment / decrement
else:
    print("Your loop finally finished executing")