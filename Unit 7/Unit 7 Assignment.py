'''IT244 Python Programming
Purdue University Global
William "Alec" Akin
March 27, 2022
Unit 7 Assignment
https://www.github.com/rainmana/PUG-IT244
'''

#Import libraries
import sys


# Define Class
class golf:
    'Golf score calculation class' # doc string
    results = " "

    def __init__(self, hole, score, par):
        self.hole = hole
        self.score = score
        self.par = par

    def calculateScore(self, hole, score):
        # Calulate score
        if (score > self.par):
            golf.results = "Over Par"
        elif (score < self.par):
            golf.results = "Under Par"
        else:
            golf.results = "At Par"

        # Report score to user
        print("You scored", golf.results, "on hole", hole, "with a par of", self.par)

# Initialize a variable to zero
score = 0

# Create three objects to represent data for each hole
hole1=golf(1, score, 3)
hole2=golf(2, score, 4)
hole3=golf(3, score, 5)

# Prompt user for Input
try:
    userHole = int(input("Please enter a hole number from 1 to 3: "))
except:
    print("You did not enter a number, please try again.")
    sys.exit()

if (userHole > 3) or (userHole < 1):
    print("You did not enter a value from 1 to 3 for corresponding course holes. Please try again.")
    sys.exit()

try:
    score = int(input("Please enter your score: "))
except:
    print("You did not enter a number, please try again.")
    sys.exit()

# Use IF statements to evaluate input
if userHole == 1:
    hole1.calculateScore(userHole, score)
elif userHole == 2:
    hole2.calculateScore(userHole, score)
elif userHole == 3:
    hole3.calculateScore(userHole, score)


