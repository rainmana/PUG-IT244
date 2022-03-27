# Unit 6 Assignment: Working With User-Defined Functions 

Outcomes addressed in this assignment: 

### Unit Outcome: 

- Illustrate the creation of user-defined functions. 

### Course Outcome: 

**IT244-2**: Analyze user-defined functions and classes in Python.  

### Purpose 

In this assignment, you will create a user-defined function passing variables both by value and by reference and using arguments of different data types. 

## Assignment Requirements 

For this project, you will write a program that requests a temperature value and the temperature scale used from the user. Write a single function that evaluates a given temperature and returns associated conversions. For example, the user could input a temperature value in Fahrenheit and receive the temperature in its Celsius equivalent.

The program will pass three variables: one for Celsius, one for Fahrenheit, and one flag that indicates the current temperature scale from which to convert (i.e., “C” or “F”) to the function. The function will then calculate the correct temperature for the other temperature scale and place the value in the corresponding variables that were passed to the function. The program will then display the values to the user. 

**Conversion formulas for your reference**:

`F = (C \* 9/5) + 32`

`C = (F - 32) \* 5/9`

## Assignment Instructions 

1. Use the def keyword to define a temperature conversion function (i.e., convertTemp) that accepts two parameters (a temperatures list and a temperature scale letter value [i.e., temps, tempScale]).

	- *Reference*: Refer to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 4: Definition of a Function / Returning More Than One Value; and Programming in Python, Chapter 6: Python Functions / Pass by Value vs. Pass by Reference.

2. Within the function, incorporate an IF/ELIF statement to evaluate the temperature scale entered (“C” or “F”).

	- When the temperature scale entered is F, incorporate a formula to calculate the Celsius equivalent and place the result in the appropriate index position in the temps list. See conversion formula above in requirements.

	- When the temperature scale entered is C, incorporate a formula to calculate the Fahrenheit equivalent and place the result in the appropriate index position in the temps list. See conversion formula above in requirements.

	- Return temps list.

	- *Reference*: Refer to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Simple Math / Order of Operations; Chapter 4: Definition of a Function / Returning More Than One Value; and Chapter 5: The if Statement / Comparison Operators; and Programming in Python, Chapter 6: Python Functions / Pass by Value vs. Pass by Reference.

3. Prompt the user to enter a temperature value and scale. Store the input in variables (i.e., tempEntered, tempScale).

	- Example prompts:

			Enter a temperature value:
			Enter a single letter to indicate the temperature scale (C or F):

	- *Hint*: Placing float ahead of the input statement will store the user input as a decimal number data type. Since the temperature value will be used in the conversion calculation, you will want this to be a numeric value. You may incorporate additional optional data validation as you wish.

	- *Reference*: Refer back to your Unit 1 and 3 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 3: Built-In Functions / Getting Input From the User.

4. Define and initialize your temps list to hold two number values.

	- *Hint*: Initialize both positions to zero for now. The user will only be entering one temperature value, so you will have to fill in one position in the list with that value and leave the other as zero to be converted when the function is called.

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists.

5. Use an IF/ELIF statement to evaluate the temperature scale entered and populate the appropriate list position (index) with the temperature value entered. (i.e., Use position zero for Celsius and position one for Fahrenheit.)

	- Example:

			if tempScale == "C":           

    		temps[0] = tempEntered

6. Call your temperature conversion function passing it the temperature values in a list and a letter code for temperature scale.

	- *Reference*: Refer to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 4: Calling a User-Defined Function.

7. Print the results from the temperature conversion function. Display the temperature value entered (i.e., 32 F) and then display the temperature in both Celsius and Fahrenheit.

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Print Statements.

### EXPECTED OUTPUT:

	Enter a temperature value: 32
	
	Enter a single letter to indicate the temperature scale (C or F): F
	
	You entered  32.0  degrees  F >>>
	
	The temperature in Celsius is  0.0
	
	The temperature in Fahrenheit is  32.0

### Directions for Submitting Your Assignment 

Submit a single program file named `IT244_YourLastName_Unit6_Assignment.py`. 