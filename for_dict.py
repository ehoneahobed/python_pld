#!/usr/bin/python3
"""Using a for loop to access values in a dictionary"""

mdict = {"maths":78, "science":96}

#1
# for i in mdict:
#     print(mdict[i])

#2
# for subject in mdict.keys():
#     print(subject)

# #3
# for subject in mdict.values():
#     print(subject)

#4
# for subject in mdict.items():
#     print(subject)

#5
for subject, score in mdict.items():
    print(f"Subject = {subject} and Score = {score}")