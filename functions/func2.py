#!/usr/bin/python3


def greeting(fname, lname, title, mname=None):
    if mname is not None:
        str_to_return = f"Hi {title}, your full name is {fname} {mname} {lname}"
    else:
        str_to_return = f"Hi {title}, your full name is {fname} {lname}"
    return str_to_return

obed = greeting("Obed", "Ehoneah", "Dr")
print(obed)