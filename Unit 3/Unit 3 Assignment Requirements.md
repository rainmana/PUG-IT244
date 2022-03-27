# IT244 Unit 3 Assignment: Iteration

Outcomes addressed in this assignment: 

### Unit Outcomes: 

*  Illustrate the use of repetition structures in Python.
*  Apply the debugging process and testing process to programs containing fundamental concepts such as variables, decision statements, and iteration.
*  Comprehend the role of data validation in Python.

### Course Outcome: 

IT244-1: Apply the basic concepts of programming using the Python language. 

### Purpose 

This assignment lets you demonstrate the use of looping (iteration) as well as data validation in a real-world scenario that takes user input, processes it, and formats and displays the results.

## Assignment Requirements 

Write a Python program that will incorporate conditional looping to average a given number of assignment grades for a student. The program will calculate and display the average.

### Pseudocode:

      Enter number of grades to process.

      Enter a student name

            While loop counter is less than number of grades to process

                        Enter assignment grade

                        Add grade to grade tally

                        Increment loop counter

       Calculate student average

       Display student average

## Assignment Instructions

  1. Initialize variables as needed (i.e., numGrades = 0). 

    - *Reference*: Refer back to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Booleans.

2. Prompt the user to input the number of grades to be processed. Store this value in a variable (i.e., numGrades).

    - *Hint*: This value will determine how many repetitions are performed.

    - Reference: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 3: Built-In Functions / Getting Input From the User.

3. Prompt the user to enter a student name. Store that name in a variable (i.e., studentName).

4. Create a conditional loop and continue processing grade values for this student until the given number of assignments have been processed.

    - **Within this loop**:
        - Prompt to get a numeric grade value from the user.
        - Add that grade to a numeric variable to keep a tally of the grades. Each time through the loop (for a given student), a new grade value will be entered and added to this tally.
        - Increment the loop counter.

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 6: Loops / The While Statement / Increment and Decrement

5. Once grades for the conditional loop have been entered, average the grades using the total tally divided by the number of grades to be entered given at the start of the program. Store the average in a variable (i.e., studentAverage).

    - *Reference*: Refer back to your Unit 2 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Simple Math.

6. Display the name of the student and their average.

### EXAMPLE OUTPUT

	Enter number of grades to process: 2
	
	Enter student name: Bob
	
	Enter assignment grade: 90
	
	Enter assignment grade: 80
	
	Bob has an average of:  85.0

### Directions for Submitting Your Assignment

Submit the program source code file (.py) as your deliverable. The file should be named `IT244_YourLastName_Unit3_Assignment`.