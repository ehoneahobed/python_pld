#!/usr/bin/python3

fname = input("Firstname: ")
surname = input("Surname: ")
age = int(input("Age: "))

# using old style formatting
# print("Your name is %s %s and you are %d years old" %(fname, surname, age))

# print()
# # using new style formatting (str.format())
# print("Your name is {} {} and you are {} years old".format(fname, surname, age))

# print()
# print("Your name is {:s} {:s} and you are {:d} years old".format(fname, surname, age))

print()
print("Your name is {1} {0} and you are {2} years old".format(fname, surname, age))

print()
print("Your name is {lname} {firstname} and you are {years_old} years old".format(lname = surname, firstname = fname, years_old = age))

# f-string formatting style
print(f"Your name is {fname:s} {surname:s} and you are {age:d} years old")
