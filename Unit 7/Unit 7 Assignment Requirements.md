# Unit 7 Assignment: Classes and Objects

Outcomes addressed in this assignment: 

### Unit Outcome: 

- Integrate the use of the classes in Python programs.

### Course Outcome: 

**IT244-2**: Analyze user-defined functions and classes in Python. 

### Purpose

Create a program written in Python demonstrating the use of classes.

## Assignment Requirements:

For this assignment you will be demonstrating the use of classes and objects in Python.

You will write a simple golf scoring program that defines a golf class from which you will create three objects (one for each hole on a three-hole golf course). You will pass the hole number, score, and par value for each object. The class will contain a method that evaluates a score and displays whether the score is at, under, or over par for the given hole.

## Assignment Instructions

1. Define your golf class.

	- a) Use the keyword "class" to define a class named golf

	- b) Initialize a class variable named results to hold the string that states whether the score is at, under, or over par.

	- *Hint*: Initialize with a space.

	- c) Define the constructor method to accept variables for hole, score, and par. Initialize hole and par.

	- *Hint*: Use self as an argument like self.hole = hole

	- d) Define a method to evaluate and display the score. Use an IF statement to check the score against par. Set the results accordingly. Display the results for the given score and par value. Include the par value in the display.

		- `score > par is "Over Par"`

		- `score < par is “Under Par”`

		- `Otherwise (equal) is  "At Par"`

	- *Reference*: Refer to Programming in Python, Chapter 10: Classes and Objects / 10.1 Designing Classes.

2. Initialize a score variable to zero.

3. Create your objects for each hole. There should be three arguments: the hole #, the score, and the par value.

	- Example:

			`hole1=Golf(1, score, 3)`

		- Where 1 represents the hole number, score will be the user’s score entered, and 3 is the par value for the given hole.

	- *Reference*: Refer to Programming in Python, Chapter 10: Classes and Objects / 10.2 Creating Objects.

4. Prompt the user to enter a hole number and score. Store the hole number in a variable and the score in the score variable initialized previously.

	- *Hint*: Placing int ahead of the input statement will store the user input as a number.

	- *Reference*: Refer back to your Unit 1 and 3 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 3: Built-In Functions / Getting Input From the User.

5. Use IF statements to evaluate the hole number entered and call the appropriate class method for the appropriate hole object. This will invoke the method in the class to display the results to the user.

	- Example:

			if enterHole == 1:
			
			   hole1.evaluateAndDisplayScore(enterHole, score)

	- *Reference*: Refer to Programming in Python, Chapter 10: Classes and Objects / 10.3 Accessing Attributes.

### EXAMPLE RESULTS

	Enter the hole number: 1
	
	Enter your score: 5
	
	You scored Over Par on hole # 1 with a par of 3
	
	 
	
	Enter the hole number: 2
	
	Enter your score: 1
	
	You scored Under Par on hole # 2 with a par of 4
	
	 
	
	Enter the hole number: 3
	
	Enter your score: 5
	
	You scored At Par on hole # 3 with a par of 5

### Directions for Submitting Your Assignment

Submit one program named `IT244_YourLastName_Unit7.py`.