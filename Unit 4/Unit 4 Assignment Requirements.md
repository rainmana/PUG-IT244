# Unit 4 Assignment: Using Python Data Structures

Outcomes addressed in this assignment: 

### Unit Outcomes: 

* Use lists to manipulate groups of related data.
* Illustrate the role of an index in lists.
* Discover the use of additional data structures in Python such as tuples, lists of lists, and dictionaries. 

### Course Outcomes: 

IT244-1: Apply the basic concepts of programming using the Python language. 

PC-2.1: Achieve goals through planning and prioritization.

### Purpose 

This assignment allows you to demonstrate the use of data manipulation using lists and dictionaries. You will plan out your program and then achieve your goal of creating it for customer usage.

Assignment Requirements: 

For this assignment you will plan and create a program for a small ice cream shop that will allow a customer to see the flavors available, select a cone size, and see the price for their order. Planning and prioritizing before creating a usable program is extremely important. To achieve your identified goals, you should first develop detailed models for a program that you will then create that fulfills requirements. Your models and program should be well organized and tested for correct output before customer usage.

- Create a list to hold seven ice cream flavors.
- Modify the name of one flavor.
- Add one new flavor to the end of the list.
- Sort the list.
- Display the number of flavors and number and name of each flavor in the list.
- Create two dictionaries: one to hold the cone sizes and prices and another to hold the size descriptions.
- Prompt the user to enter a size and flavor.
- Validate that a correct size and flavor value were entered.
- Display the price, size description, and flavor.

## Assignment Instructions: 

### PART 1 - PLANNING

Using an IPO chart and pseudocode, plan the input and output data and model your processing prior to creating the code in Python for this programming scenario.

*Reference supplemental videos for three previous programs for examples of IPO charts and pseudocode.*

### PART 2 - PROGRAMMING FROM THE MODELS

1. Display a welcome message on the screen:

    - “Welcome to The Ice Creamery”

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Print Statements.

2. Create a new list variable for storing seven ice cream flavors (i.e., flavorsList).

    - flavorsList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]

    - *Reference:* Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists.

3. Change the name of one flavor in the list of flavors just created.

    - *Hint*: Use the index value for the position of the flavor in the list and assign it a new value.

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd Edition, Chapter 7: Lists / Changing a Value in a List.

4. Use a built-in list operation to append a new flavor to the end of the list. You should now have eight flavors in the list.

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists / Table 7-1: The Built-In List Operations.

5. Use a built-in list operation to sort the flavors list in alphabetical order.

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists / Table 7-1: The Built-In List Operations.

6. Store the number of flavors in the list in a variable and display the number of flavors.

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists / Determining the Number of Elements in a List: The len Function.

7. Loop through each flavor in the list using a FOR loop to display the number and name for each item in the list.

	- a) Create FOR loop to process each flavor in flavorsList list.

    - b) With each iteration, display the flavor # using the index value in the flavors list and the name of the flavor.

    - *Hint*: Remember index positions in lists start with zero. To make this more customer friendly, add one to the index value before displaying it.

        *Reference*: Refer back to your Unit 1 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 2: Simple Math; Chapter 7: Lists / Position of an Element in a List: Index / Accessing an Element in a List / for Statements and for Loops.

8. Define dictionaries to hold the prices and descriptions for each cone size.

    - `conePrices={"S":"$1.50","M":"$2.50","L":"$3.50"}
`
    - `coneSizes={"S":"smallish","M":"more for me","L":"lotta lickin"}`

    - *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 11: Data Structures, Dictionary.

9. Prompt the user to enter a cone size (S, M, or L). Store their choice in a variable (i.e., customerSize).

    - *OPTIONAL VALIDATION*: Use an IF statement to ensure a valid value was entered. Display an error message if an invalid value was entered.

    - *Reference*: Refer back to your Unit 1 and 3 readings in Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 3: Built-In Functions / Getting Input from the User; Chapter 5: The if Statement / Comparison Operators.

10. Prompt the user to enter a flavor number. Store their choice in a number variable (i.e., customerFlavor).

    - *Hint*: Placing int ahead of the input statement will store the user input as a number. You will be using this number as the index to find the flavor value from the list.

    - *OPTIONAL VALIDATION*: Use an IF statement to ensure a valid value was entered. Display an error message if an invalid value was entered.

11. Display the price, size description, and flavor for their choice. Use your conePrices dictionary to match the size value entered to the price. Use your coneSizes dictionary to match the size to the description of the size.

    - *Hint*: Remember that index positions in lists start with zero. To make this more customer friendly, we added one to the index value before displaying it. You will need to do the same here to display the appropriate value from the list. 

    - Use `print()` to print blank lines as necessary for readability.

    - *Reference*: Refer to Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists / Position of an Element in a List: Index / Accessing an Element in a List; Chapter 11: Data Structures, Dictionary.

### EXAMPLE PROGRAM OUTPUT 

	Welcome to The Ice Creamery
	
	These are the 8 flavors we are serving today at The Ice Creamery:
	
	Flavor #:  1   Blueberry Crunch
	Flavor #:  2   Butter Pecan
	Flavor #:  3   Chocolate
	Flavor #:  4   Cookie Dough
	Flavor #:  5   Neapolitan
	Flavor #:  6   Strawberry
	Flavor #:  7   Vanilla
	Flavor #:  8   Very Berry Strawberry
	
	Please enter the cone size of your choosing: S, M, or L: S
	Please enter your flavor number: 5
	
	Your total is:  $1.50
	Your smallish sized cone of The Ice Creamery's Neapolitan will arrive shortly.
	
	Thank you for visiting the Ice Cream Creamery

### Directions for Submitting Your Assignment

Submit a zipped folder with two files: your Word® document that contains the IPO chart and pseudocode and the program source code file (.py) as your deliverable.

The file should be named `IT244_YourLastName_Unit4_Assignment`. 