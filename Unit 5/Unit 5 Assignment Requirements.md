# Unit 5 Assignment: Security and File Processing

Outcomes addressed in this assignment: 

### Unit Outcomes: 

- Investigate the role of security in programming.
- Examine file input and output. 

### Course Outcomes: 

**GEL-1.02**: Demonstrate college-level communication through the composition of original materials in Standard English. 

**IT244-2**: Analyze user-defined functions and classes in Python. 

### Purpose 

The written assignment for this unit gives you an opportunity to reflect on the role of security and data encryption in the Python programming language and the world in general. The programming assignment lets you demonstrate the ability to utilize file access techniques using Python. 

## Assignment Instructions 

The Unit 5 Assignment will consist of two parts. Part 1 is a paper on security and data encryption using Python. Part 2 is a program written in Python demonstrating file processing. 

### Part 1 Requirements: 

Research the following and write a 2-page double-spaced paper (not including title and reference pages) addressing the following: 

- Highlight any aspects of security that are unique to the Python programming language.
- Identify several methods for securing data in Python software.
- Address the role of data encryption across the Internet.
- Identify any packages built for Python that facilitate data encryption. 

Viewpoint and purpose should be clearly established and sustained, and the paper should be well-ordered, logical, and unified, as well as original and insightful.

Assignment should follow the conventions of Standard English (correct spelling, grammar, and punctuation) and be in APA format with separate title and reference pages formatted per APA guidelines. For more information on APA style formatting, go to Academic Writer, formerly APA Style Central, under the Academic Tools area of this course to assist you in meeting APA expectations. 

### Part 2 Requirements: 

For this programming assignment, you will write a program to process promotional credits for customers.

Due to a recent weather event, Sunnyside Scenic Sailings has had to cancel numerous reservations for its customers. To persuade customers to reschedule their travel plans for a future date, Sunnyside would like to give customers a promotional credit.

You will be working on some of the back-end processing for Sunnyside. Your program should read in the customer information from a text file, add one new customer record, append the new promotional credit, and write out the new records to a CSV file. A CSV file is a comma-separated values file that allows data to be saved in a tabular format. Sunnyside can use this .csv file to import the records into their spreadsheet or database management applications.

### Program Instructions: 

First, you will create the starting data text file.

1. Open Notepad (or any other plain text editor) and add the following data to the file (exactly as shown):

	- `1,Morrison,Marion,1313 Mockingbird Lane,Atlanta,GA`
	- `2,Jane,Mary,1640 Riverside Drive,Hill Valley,CA`
	- `3,Rubble,Barney,84 Beacon Street,Boston,MA`
	- `4,Davis,Betty,10 Stigwood Avenue,New York,NY`

2. Save the file as `IT244_U5_Data.txt`.

3. Define program variables. You will read the records from this text file into a list in your program. Define a list variable to hold the data (i.e., recordsList). Define and initialize a record count variable to be used later (i.e., recordCount).

	- *Reference*: Refer back to your Unit 4 readings from Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 7: Lists.

4. Define a file handle and open your text data file for reading.

	- *Hint*: If you want to reference the file by its name using a relative file path like `“IT244_U5_Data.txt”`, this file must exist in the same folder with your Python source code (.py) file. Otherwise, you will need to include the full file path, such as `C:/MyFolder/MySubFolder/MySubSubFolder/MyFile.txt`

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 9: Defining a Path to a File / Reading From and Writing to a File / File Handle.

5. Use a for loop to access each record in the file and append each record to the list variable each iteration.

	- *Hint*: Use strip to remove any line breaks like recordsList.append(line.strip())

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 9: Writing and Reading a Line at a Time With a File.

6. Close the file.

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 9: Defining a Path to a File / Reading From and Writing to a File/File Handle.

7. Append the following string of data to the list (exactly as shown):

	- `5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA`

	- *Hint*: recordsList.append("5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA")

8. Open a new csv file for writing. Name this file IT244_U5_PromoCredit.csv.

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 9: Defining a Path to a File / Reading From and Writing to a File / File Handle.

9. Write a record to the file that contains the following values that will serve as the header record in your csv file:

	- `Customer ID, Last Name, First Name, Address, City, State, Promo Credit`

	- *Hint*: add `\n` to the end of this string to force a new line.

	- *Reference*: Learn to Program With Python 3: A Step-by-Step Guide to Programming, 2nd edition, Chapter 9: Defining a Path to a File / Reading From and Writing to a File / File Handle.

10. Use another for loop to process the list data.

    - With each iteration through the loop, write out a record.

    - Append the $500 promotional credit.

    - *Hint*: This can be done by simply adding the value in a string like file.write(",$500\n"). Don’t forget the newline character at the end.

    - Increment the record count variable.

11. Close the file.

12. Conclude the program by printing a statement that includes the record count:

	- There were 5 records written to the promo credits csv file.

### Summary of files used in this program: 

**INPUT**: `IT244_U5_Data.txt`

	1,Morrison,Marion,1313 Mockingbird Lane,Atlanta,GA
	
	2,Jane,Mary,1640 Riverside Drive,Hill Valley,CA
	
	3,Rubble,Barney,84 Beacon Street,Boston,MA
	
	4,Davis,Betty,10 Stigwood Avenue,New York,NY

 

**OUTPUT**: `IT244_U5_PromoCredit.csv`

*(This table represents the .csv file opened in a spreadsheet application)*

| Customer ID |  Last Name |  First Name |  Address              |  City       |  State |  Promo Credit |
| ----------- | ---------- | ----------- | --------------------- | ----------- | ------ | ------------- |
| 1           | Morrison   | Marion      | 1313 Mockingbird Lane | Atlanta     | GA     | $500          |
| 2           | Jane       | Mary        | 1640 Riverside Drive  | Hill Valley | CA     | $500          |
| 3           | Rubble     | Barney      | 84 Beacon Street      | Boston      | MA     | $500          |
| 4           | Davis      | Betty       | 10 Stigwood Avenue    | New York    | NY     | $500          |
| 5           | Brady      | Bobby       | 4222 Clinton Way      | Los Angeles | CA     | $500          |

### Directions for Submitting Your Assignment 

For the written assignment, submit a Word file named `IT244_YourLastName_Unit5_Part1`. 

For the programming assignment, submit a ZIP file that includes the text data file you created, the csv file your program produced, and your program source code file. Name your ZIP file `IT244_YourLastName_Unit5_Part2.zip`.