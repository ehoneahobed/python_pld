#!/usr/bin/python3
'''Calculate BMI (m = height, kg = weight)'''

def bmi_calculator(weight, height):
    bmi = weight // (height * height)
    weight_cm = weight * 100

    # print(f"Your BMI is {bmi}")

    # tuples, list, dictionaries, sets (collections)
    return bmi

bb_bmi = bmi_calculator(70, 1.76)

print(bb_bmi)

# if bb_bmi > aa_bmi:
#     print("BB is heavier than AA")
# else:
#     print("AA is heavier than BB")