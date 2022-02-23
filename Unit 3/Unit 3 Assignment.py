'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
Februrary 22, 2022
https://www.github.com/rainmana/PUG-IT244
'''

#Setting interative counter early for the loop that will come later
counter = 0

#Setting total to 0 to allow for use later as an integer after built-in debugging complained it needed to be an integer. Likely this is because I'm doing math with it later on in the loop.
total = int(0)

#Prompt user to enter the student's name by printing to standard out
print("\n\nEnter the student's name: ")

#Initialize studentName variable and taking input from stdin
studentName = input()

#Promt user to enter the number of assignments we'll be working with
print("\n\nPlease enter the number of assignment grades: ")
numOfAssignments = input()
numOfAssignments = int(numOfAssignments)

# Loop/interate through the number of assignments and take input from user

while (counter < numOfAssignments):
    #Prompt user to enter assignment grades
    print("\n\nPlease enter an assignment grade: ")

    #Initialize grade variable, assign it the int type, and allow input from stdin
    grade = int(input())

    #Initialize total variable and add to the grade variable
    total = total + grade

    #Utilize counter defined in the beginning to interate through the number of grades
    counter = counter + 1

#Debugging statment commented out but left for professor in case that's of interestest
#print("\n\ncounter is: ", counter, "total is: ", total, "grade is: ", grade)

#Perform mathmatical calculation to determine average grade across all assignments
average = total / numOfAssignments

#Print the final result of student's name and file grade average across all numOfAssignments. Additionally, I added double quotes around the studentName variable to increase readability
print("\n\nThe student named", (f'"{studentName}"'), "recevied a final average grade of", average, "percent, calulated over", numOfAssignments, "assignments.")



