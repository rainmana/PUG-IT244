'''IT244 Python Programming
Purude Univervisty Global
William "Alec" Akin
April 11, 2022
Unit 10 Assignment
https://www.github.com/rainmana/PUG-IT244
'''

#This file serves as the module "kilometers" and is saved as "kilometers.py"

#Creation of a function called convertToKilometers that accepts one value and returns the converted value when called
#Additionally, we will make the kilometersResult variable a floating point number so it can be represented as an accurate decimal value
def convertToKilometers(miles):
    kilometersResult = miles / 0.62137
    return kilometersResult
