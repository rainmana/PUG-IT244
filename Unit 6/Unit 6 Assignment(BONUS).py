'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
March 15, 2022
Unit 6 BONUS Code
https://www.github.com/rainmana/PUG-IT244
'''

#Import libraries
import sys
from colorama import Fore, Back, Style, init

#Use the def keyword to define a conversion function that accepts two parameters (F or C)
def tempConversion(temp, unit):
    if unit == "C":
        #convert to fahrenheit
        temp[1] = (temp[0] * 9/5) + 32
    elif unit == "F":
        #convert to celcius
        temp[0] = (temp[1] - 32) * 5/9

    #return temp List
    return(temp)

#Define additional user functions for adding bonus features
def welcomeBanner():
    init(autoreset=True)
    print(Fore.BLUE + r"""
  _______                                  _                  
 |__   __|                                | |                 
    | | ___ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ ___ 
    | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _ \
    | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | |  __/
   _|_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \___|
  / ____|            | |                  | |                 
 | |     _____   ____|_| ____   _____ _ __| |_ ___ _ __       
 | |    / _ \ \ / / _ \ '__\ \ / / _ \ '__| __/ _ \ '__|      
 | |___| (_) \ V /  __/ |   \ V /  __/ |  | ||  __/ |         
  \_____\___/ \_/ \___|_|    \_/ \___|_|   \__\___|_|         
                                                              
                                                              
By W. Alec Akin for PUG IT244 - Python Programming with Dr. Ed Lavieri
        
        
        """)

#Get input from user input() function and define any variables to be used later on
#Print new lines to separate from the top
print("\n\n\n")
welcomeBanner()
#User try funtion to take float input and exit program if user doesn't follow directions. This allows graceful/accessible errror code and close

try:
    userTemp = float(input("Please enter the temperature (numbers only): "))
except ValueError:
    print("You did not enter a number. Please try again.")
    sys.exit() 

# Take input for F/C choice
unit = input("Enter either a C for Celcius or F for Fahrenheit: ")
unit = unit.upper()

#Validate if user entered F/C and exit with error if they did not
if (unit != "C" and unit != "F"):
    print("\nYou did not enter a valid unit. Please try again.")
    sys.exit()

#Empty variable initialized for use later at print output
fullTemp = ""

#Initalize temperature(temp) list to hold temperature values used to pass to the function defined earlier
temp = [0,0]

#Use if/elif state to evaluate the temperature scale entered and populate the apporpriate list position (index) with the temp value entered
if unit == "C":
    temp[0] = userTemp
    fullUnit = "Celsius"
if unit == "F":
    temp[1] = userTemp
    fullUnit = "Fahrenheit"

#Call function defined at begging of program to convert the temperature
tempConversion(temp, unit)

#Print results to standard output as defined in assignment instructions
print("\n\nYou entered a temperature value of ", userTemp, fullUnit, ">>>")
print("The temperature in Celcius is ", temp[0])
print("The temperature in Fahrenheit is", temp[1])