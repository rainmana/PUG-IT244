'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
Februrary 14, 2022
https://www.github.com/rainmana/PUG-IT244
BONUS
'''

# Import libraries to add color
import colorama
from colorama import Fore, Style

# Print welcome message to stdout
print("\n\n\n\nYour color choices are red, blue, green, white, or yellow.")

# Print instructions to stdout and allow user input
userColor = input("\n\nEnter a color from the list above: ")

# Take user input and convert to lowercase
userColor = userColor.lower()

# Set a variable for color validity checking to be used in the final else statement
validColor = True

# Begin logic of taking user input and assinging the spanish color. If no valid color was entered, assign False value to validColor
if userColor == "red":
    spanishColor = "rojo"
    termColor = Fore.RED

elif userColor == "blue":
    spanishColor = "azul"
    termColor = Fore.BLUE

elif userColor == "green":
    spanishColor = "verde"
    termColor = Fore.GREEN

elif userColor == "white":
    spanishColor = "blanco"
    termColor = Fore.WHITE

elif userColor == "yellow":
    spanishColor = "amarillo"
    termColor = Fore.YELLOW

else:
    validColor = False

# Print out final answer for userColor and corresponding spanishColor or error value if nothing valid is entered
if validColor:
    print("\n", termColor + "The color", userColor, "in Spanish is " + spanishColor)

# Print error if nothing valid is entered
else:
    print("That is not a valid color for this program. Ese no es un color valido.")
