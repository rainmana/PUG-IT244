'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
March 7, 20222
Unit 5 Assignment
https://www.github.com/rainmana/PUG-IT244
'''


#Import libraries
from ast import Index
import sys



#Initialize variable for use later
recordCounter = 0
recordCounter = int(recordCounter)
recordsList = list

#Instead of reading a static file name/location, read in file as command line argument
with open(sys.argv[1], 'r') as file:
   contents = file.readlines()
   fileName = sys.argv[1]

#Add the contents of the file to the recordsList list and strip lines with for loop
recordsList = [line.strip() for line in contents]

#Add a fifth record to recordsList
recordsList.append("5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA")

#Count number of records in recordsList and assign it to recordCount and recordCounter for the next Loop
recordCounter = len(recordsList)
recordCount = len(recordsList)

#Write out the now updated recordsList list to a new file with a counter that increases and compares to a static record value to close the while loop
outputFile = open("IT244_U5_PromoCredit.csv", "w")
outputFile.write("Customer ID, Last Name, First Name, Address, City, State, Promo Credit\n")
while recordCounter <= recordCount:
        for index in recordsList:
            outputFile.write(index)
            outputFile.write(",$500\n")
            recordCounter = recordCounter + 1

#Out put data to stdout that includes the recordCount, the input filename, and records processed
print('There were',recordCount,'files written to the prmo credits csv file.\n')
print('\nINPUT: ')
print(fileName,'\n')

for index in recordsList:
    print(index)




