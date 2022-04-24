'''IT244 Python Programming
Purude Univervisty Global
William "Alec" Akin
April 11, 2022
Unit 10 Assignment
https://www.github.com/rainmana/PUG-IT244
'''

#This file serves and the "main" Python program which incorporates both moddules as imports and performs the primary functions of the Assignment requirements

#First, we import the two custom modules that were written to contain conversion fucntions just as if we did so with a module/lib from PyPi
import kilometers
import miles
import welcomebanner
import goodbye


#I'm also going to import some other libraries that will help with error handling like my other code
import sys
from colorama import Fore, Back, Style, init

#Initialize variables and conditional loop flag
continueProgram = True
invalidValue = True
validValue = True

#Use the welcomebanner module to print a welcome message on first run (not through every loop)
welcomebanner.welcomeBanner()

#Start loop to contain all primary functions for code so that the script keeps running until the user tells it to stop
while continueProgram == True:
    #Print prompting text to stdout to allow user to enter values for distance and the unit of measurement
    print('\n\n\n')
    
    #Using the input method followed by the float method to ensure a decimal point value is permitted
    userDistance = input(Style.BRIGHT + "Please enter a distance value which can include a decimal point:")
    userDistance = float(userDistance)
    print('\n')
    print(Style.BRIGHT + "What is the unit of length? (Enter M = miles, KM = kilomenters:")
    userUnit = input()
    #Ensure that the user's entered unit of measurement is in lowercase to reduce errors
    userUnit = userUnit.lower()
    
    #Debugging print statement
    #print(userUnit)

    #Validate that the user has entered either M or KM as values, otherwise, produce custom error message and exit
    if (userUnit != "m" and userUnit != "km"):
        print("\n" + Fore.RED + Style.BRIGHT + "You did not enter a valid unit (M or KM). Please try again and follow the instructions.")
        sys.exit()

    #Start a decsision structure that will utilize the appropriate module to perform a conversion operation on the user inputed floating point value
    if userUnit == "m":
        convertedDistance = kilometers.convertToKilometers(userDistance)
        print(Fore.GREEN + "Your distance of", userDistance, Fore.GREEN + "miles, is equivalent to", convertedDistance, Fore.GREEN + "kilometers.")
    elif userUnit == "km":
        convertedDistance = miles.convertToMiles(userDistance)
        print(Fore.GREEN + "Your distance of", userDistance, Fore.GREEN + "kilometers, is equivalent to", convertedDistance, Fore.GREEN + "miles.")

    #Prompt the user to quit if they would like to do so
    userContinue = input(Style.BRIGHT + Fore.YELLOW + "Press X to quit or Enter to continue processing:")
    if userContinue == "":
        continueProgram = True
    #By setting the value of "continueProgram" to "False" when the user uses the "X" key, we close the while loop and the program closes
    elif userContinue == "X" or "x":
        #Use the goodbye module and method to display message and mini ascii art image
        goodbye.goodbyeBanner()
        continueProgram = False

