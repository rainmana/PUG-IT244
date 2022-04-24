'''IT244 Python Programming
Purude Univervisty Global
William "Alec" Akin
April 11, 2022
Unit 10 Assignment
https://www.github.com/rainmana/PUG-IT244
'''

#This file serves as the module for "goodbye" which contains the welcome text and colors for the main.py program

#Import extra libraries
from colorama import Fore, Back, Style, init

#Define the function which contains the goodbye ascii art and message when user decides to close program/loop
def goodbyeBanner():
    init(autoreset=True)
    print(Fore.LIGHTBLUE_EX + r"""
  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-'   - Thank you for an awesome class Dr. Ed!

""")