#!/usr/bin/python3

def greet_user(**kwargs):
    # *args =>  a tuple
    # **kwargs => dictionary
    print(kwargs)

# greet_user("Obed")
{"fname" : "obed", "lname":"ehoneah" }
greet_user("Obed", "Ehoneah", 99)