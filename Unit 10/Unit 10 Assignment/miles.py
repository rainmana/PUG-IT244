'''IT244 Python Programming
Purude Univervisty Global
William "Alec" Akin
April 11, 2022
Unit 10 Assignment
https://www.github.com/rainmana/PUG-IT244
'''

#This file serves as the module "miles" and is saved as "miles.py"

#Creation of a function called convertToMiles that accepts one value and returns the coverted value when called
#Additionally, we will make the milesResult variable a floating point number so it can be represented as an accurate decimal value
def convertToMiles(kilometers):
    milesResult = kilometers * 0.62137
    return milesResult
    