# IT244 Unit 10 Assignment: User-Define Modules

Outcomes addressed in this assignment: 

### Unit Outcome: 

- Experiment with user-defined modules. 

### Course Outcome: 

**IT244-3**: Examine Python versions, available system interfaces, built-in tools, and user-defined modules. 

### Purpose:

This assignment will allow you to understand and demonstrate the role of user-defined modules in Python. A Python module is a file that contains one or more function definitions or classes. Modules play a vital role in making more reusable code that can be shared between projects or with other programmers. A module you create is just like any other module in the Python standard library.

## Assignment Requirements

In this assignment, you will write a program that demonstrates the use of user-defined modules by invoking functions from imported modules. Your program will accept a distance value and unit of length (miles or kilometers) and will call functions within your user-defined modules to convert the distance to the other unit of length. You will create two modules that contain the functions: one to convert miles to kilometers and one to convert kilometers to miles. Your program should continue converting entered distances until the user chooses to discontinue the program.

## Assignment Directions 

1. You will begin by creating the modules that hold the conversion functions. Start a new Python file and build each function to do the appropriate conversions.

	- a) Create a module named miles.

	- b) Create a function within this module named convertToMiles that accepts one value and returns the converted value when called.

	- c) Create a second module named kilometers.

	- d) Create a function within this module named convertToKilometers that accepts one value and returns the converted value when called.

	- *Conversion formulas for your reference:*

		- [Metric Conversions](https://www.metric-conversions.org/length/kilometers-to-miles.htm) (Kilometers-to-miles)

		- [Metric Conversions](https://www.metric-conversions.org/length/miles-to-kilometers.htm) (Miles-to-kilometers)

	- *Hint*: Modules are created as Python files with the same .py file extension as your main program file. Your modules must be within the same folder/directory as your program file in order to invoke functions from them. 

	- *Reference*: Refer back to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 4: Definition of a Function; and Programming in Python Chapter 7: Python Modules / 7.2 Module Definition / 7.3 Creating a Module.

1. Next you will create your Python program to accept user input of a distance value and unit of length (miles or kilometers). You will start by including the import statements at the top of this program. You will import both the miles and kilometers modules you just created.

	- *Reminder*: These three Python files must exist within the same directory.

	- *Reference*: Refer to Programming in Python Chapter 7: Python Modules / 7.2 7.5 7.6 Importing Modules.

3. Initialize variables. You should create two flag variables and initialize them to a value of true: one for when an invalid value is entered and one for when the user chooses to stop the processing (i.e., validValue, processing).

4. Create a conditional loop that will continue the processing until the user chooses to exit.

	- *Hint*: Use the processing flag you just created in step 3 as your test condition.

	- *Reference*: Refer back to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 6: Loops / The While Statement.  

5. Accept a distance value and unit of length from the user and store these two values in variables. Use prompts such as:

		`Please enter a distance value:
		
		What is the unit of length (M = miles, KM = kilometers):`

	- *Hint*: Preface your input statement with float to ensure the value they enter is stored as a decimal number for use in the conversion formulas.

	- *Reference*: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 3: Built-In Functions / Getting Input From the User.

6. Incorporate a decision structure to check the unit of length entered by the user and call the appropriate conversion function from your user-defined modules.

	- a) If the user entered “M”, call the convertToKilometers function passing in the user entered distance. Store the result of the function call in a new variable (convertedDistance).

   - b) If the user entered “KM”, call the convertToMiles function passing in the user entered distance. Store the result of the function call in a new variable (convertedDistance).

  - c) Use an else statement for any other values and set the validValue flag to false to indicate an invalid value was entered.

	- *Hint*: Use the string function, upper, to convert the user input to uppercase and check for a value of M or KM only.

	- *Reference*: Refer back to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 5: The if Statement / Comparison Operators / The elif Statement.

7. If the user entered a valid unit of length, display the distance they entered, the unit of measurement and the converted distance/unit. Otherwise, display an error message. (i.e.. Your distance of 26.2 miles is equivalent to 42.1 kilometers or You entered an invalid unit of length.)

	- *Hint*: Use an IF/ELSE decision structure here. Concatenate the results into one string.

	- *Reference*: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Print Statements; Chapter 3: Built-In Functions / Concatenation; Chapter 5: The if Statement.

8. Add another prompt to ask the user if they would like to continue. (i.e., `"Press X to quit or enter to continue processing."`)

9. If the user entered a value to discontinue processing, set the processing flag to false to conclude the conditional looping and end the program.

*Note: These small programming examples include very minimal data validation. Feel free to expand upon this and add additional layers of validation.*

### Example Output 

	`Please enter a distance value: 26.2
	
	What is the unit of length (M = miles, KM = kilometers) : m
	
	Your distance of  26.2   miles is equivalent to 42.16 kilometers
	
	Press X to quit or enter to continue processing.
	
	Please enter a distance value: 5
	
	What is the unit of length (M = miles, KM = kilometers) : km
	
	Your distance of  5.0   kilometers is equivalent to 3.10 miles
	
	Press X to quit or enter to continue processing. X
	
	End processing of distances.

## Directions for Submitting Your Assignment 

Submit a single ZIP file that contains the three .py files (the program file and the two module files) named `IT244_YourLastName_Unit10.zip`. 