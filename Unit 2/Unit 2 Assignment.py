'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
Februrary 14, 2022
https://www.github.com/rainmana/PUG-IT244
'''

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

elif userColor == "blue":
    spanishColor = "azul"

elif userColor == "green":
    spanishColor = "verde"

elif userColor == "white":
    spanishColor = "blanco"

elif userColor == "yellow":
    spanishColor = "amarillo"

else:
    validColor = False

# Print out final answer for userColor and corresponding spanishColor or error value if nothing valid is entered
if validColor:
    print("\nThe color", userColor, "in Spanish is " + spanishColor)

# Print error if nothing valid is entered
else:
    print("That is not a valid color for this program. Ese no es un color valido.")
