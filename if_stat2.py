#!/usr/bin/python3
"""Give us directions based on traffic rules"""

light = input("What color is the light? ").lower()

if (light == "red"):
    print("Hey stop")
elif (light == "yellow"):
    print("Get ready")
elif (light == "green"):
    print("Go")
else:
    print("This color doesn't exist")