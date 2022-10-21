#!/usr/bin/python3

# defining the function
def age_calculator(name, yob, current_year):  # parameters (placeholders)
    age = current_year - yob
    print(f"{name}, you are {age} years old")

# calling the function
age_calculator(current_year=2028, name="Ernest", yob=1985)
