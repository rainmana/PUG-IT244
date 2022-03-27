# IT244 Unit 2 Assignment: Using Conditional Logic

Outcomes addressed in this assignment: 

### Unit Outcomes: 

* Illustrate the use of decision structures.
* Use logical/relational operators to prepare a conditional statement. 

### Course Outcome:

IT244-1: Apply the basic concepts of programming using the Python language. 

### Purpose

This assignment gives you the opportunity to demonstrate the use of decision structures and logical operators in a simple language conversion routine.

## Assignment Requirements

For this assignment, you will create a Python program that will accept user input of an English color value from a given range of colors and will return the Spanish equivalent. You will use IF, ELIF, and ELSE statements along with comparison operators to evaluate the entered value and display the appropriate results to the user.

### Assignment Instructions

1. Print a string statement with a list of acceptable colors to the screen:

	- "Your color choices are red, blue, green, white or yellow."  

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Print Statements.

2. Prompt the user to enter a color value from the list. Assign the user input to a variable (i.e., userColor).

    - "Enter a color from the list above: "

    - *Reference*: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 3: Built-In Functions / Getting Input From the User.

3. Convert the color value entered to all lowercase for easier evaluation. Use the string function lower and store the lowercase color in a new variable (i.e., color).

    - *Reference*: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 8: Built-In String Operations.

4. Create a variable named validColor and set it to a value of true.

   -  Using a series of IF/ELIF statements, evaluate the color and set a new variable (i.e., spanishColor) to the appropriate Spanish equivalent. Use a final else statement if a valid color was not entered, and assign the validColor flag to a value of false.

    	- red = rojo

    	- blue = azul

    	- green = verde

    	- white = blanco

    	- yellow = amarillo

    - Reference: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 5: The if Statement / Comparison Operators / The elif Statement / Using Many elif Statements.

5. Create a final IF/ELSE statement to evaluate the validColor flag. If a valid color was entered, use string concatenation to display the English color (color) and its Spanish equivalent (spanishColor). If not, display a message indicating a valid color was not entered.

    - Reference: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Print Statements; Chapter 3: Built-In Functions / Concatenation.

###     EXAMPLE OUTPUT

    Your color choices are red, blue, green, white or yellow.

    Enter a color from the list above: rEd

    The color red in Spanish is rojo

    Your color choices are red, blue, green, white or yellow.

    Enter a color from the list above: black

    That is not a valid color for this program. Ese no es un color válido.

### Directions for Submitting Your Assignment

Submit the program source code file (.py) as your deliverable. The file should be named `IT244_YourLastName_Unit2_Assignment`.