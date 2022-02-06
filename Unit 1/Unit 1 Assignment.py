#/usr/bin/python3
# IT244 Python Programming
# Purdue Univeristy Global
# William "Alec" Akin
# February 6, 2022


# Define each string and utilize \ as an escape character so python doesn't interpret them as code
string1 = " Python was created in the 1890's by Guido van Rossum. "
string2 = " Python is maintained as an \'open source\' project by a group that is called the Python Software Foundation. "
string3 = " He is affectionately known as Python's \"Benevolent Dictator for Life.\" "

# Strip leading spaces from each string and define these as the most recent string* variables
string1 = string1.lstrip()
string2 = string2.lstrip()
string3 = string3.lstrip()

# Replace substring of 1890 with 1990 and define this as the new string1 variable
string1 = string1.replace('1890','1990')

# Define single variable to combine (concatenate) all strings together in order of expected output
stringALL = string1 + string3 + string2

# Print output to stdout for grading/testing/debugging
print(stringALL)
