'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
March 5, 2022
https://www.github.com/rainmana/PUG-IT244
'''

#Import libraries
import sys


#Print welcome message on the screen
print('\n\n\nWelcome to the Ice Creamery Order System!\n\n\n')

#Create a new list variable for storing seven ice cream falvors - flavorsList
flavorsList = ['Vanilla','Chocolate','Strawberry','Pistachio','Butter Pecan','Cookie Dough','Neopolitan']

#Change the name of one flavor in the list and assign it a new value using index functions (butter pecan to bubblegum)
flavorsList[4] = 'Bubblegum'

#Use a built-in List operator to append a new flavor to the end of the list. List should now have eight items.
flavorsList.append('Cherry Garcia')

#Sort the list alphabetically using built-in method
flavorsList.sort()

#Define a new variable that stores the number of items in the list, then print that number to stdout
flavorsNumbers = len(flavorsList)
print('The number of flavors available is: ', flavorsNumbers)

#Loop through each flavor in the list using a FOR loop to diplay the number and name for each item in the List
for flavor in flavorsList:
    #increment so users aren't confused by a "0" index value
    print('Flavor #: ', (flavorsList.index(flavor)+1), " ", flavor)

# Define dictionary to hold size:price and a dictionary to hold size:descriptions
conePrices = {'S':'$1.50','M':'$2.50','L':'$3.50'}
coneSizes = {'S':'smallish','M':'more','L':'lotta lickin'}

#Prompt user to enter a cone zie (S, M, L) and define as variable customerSize
customerSize = input('\n\n\nWhat size of ice cream do you want today?\n[S]mall\n[M]edium\n[L]arge\nPlease Enter S, M, or L: ')
customerSize = customerSize.upper()

#Validate that the customer chose a proper size. If not, quit. If a valid size is chosen the provide feedback of choice.
if (customerSize != 'S') and (customerSize != 'M') and (customerSize != 'L'):
     print('You did not choose a valid size (S, M, L). Please try again.')
     exit()
    
else:
    if customerSize == 'S':
        print('\nYou hvae chosen a Small ice cream cone.')
    elif customerSize == 'M':
        print('\nYou have chosen a Medium ice cream cone.')
    elif customerSize == 'L':
        print('\nYou have chosen a Large ice cream cone.')

#Prompt user to enter a flavor number from the above list of flavors. If an integer is not entered, quit program.
try:
    customerFlavor = (int(input("Enter a number corresponding to a flavor on the list above (1 to 8): ")))
except:
    sys.exit('You did not enter a number. Please try again.')
    
#Make sure customer entered an integer value between 1 and 8. If value between 1 and 8 is not entered, quit program.
while (customerFlavor > 8) or (customerFlavor < 1):
    sys.exit('You did not enter a valid number (1 - 8). Please try again.')

#Display price, size, and flavor of ice cream chosen by checking index number and dictionary key:value pairs for user selected values
for key,value in conePrices.items():
    if key == customerSize:
        priceValue = value

for key,value in coneSizes.items():
    if key == customerSize:
        sizeValue = value

#Assign variabe to value of flavorsList at index and subtract 1 to compensate of '0' index value
flavorValue = flavorsList[customerFlavor - 1]

#Print feedback on price, size, and flavor to stdout
print("\n\nYou're total today is: ", priceValue)
print("\nYour",(f'"{sizeValue}"'),"sized cone of The Ice Creamery's",flavorValue,"will arrive shortly.")







   