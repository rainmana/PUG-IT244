'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
March 7, 20222
Unit 5 Assignment
https://www.github.com/rainmana/PUG-IT244
'''


#Import extra libraries to achieve bonus functionality/features that go beyond Assignment Requirements
import sys
import csv

#Define variables to be used later
recordCount = 0
recordCount = int(recordCount)
recordsList = []

#Instead of using a static filename in inline code, make the progam able to take in any text file from the command line as arg
with open(sys.argv[1], 'r') as file:
    #Use for loop to add records from text file line by line to recordsList
    for line in file:
        recordsList = recordsList.append(line.split())
        #No close statement necessary since it's automatically taken care of. With statement makes sure this is done automatically.

print(recordsList)
sys.exit()
#Appned a new record to the list as a string of data
recordsList.append("5,Brady,Bobby,422 Clinton Way,Los Angeles,CA")




#Write data to a CSV file in the directory this script was run in
with open('Unit5_Assignment_Output.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    writer.writerow(['Customer ID','Last Name','First Name','Address','City','State','Promo Credit','test'])
    for index,record in enumerate(recordsList):
        writer.writerow(recordsList)
        recordCount = recordCount + len(recordsList)
        print('The record count now is: ', recordCount)
print(recordsList)


