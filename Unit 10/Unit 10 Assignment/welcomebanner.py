'''IT244 Python Programming
Purude Univervisty Global
William "Alec" Akin
April 11, 2022
Unit 10 Assignment
https://www.github.com/rainmana/PUG-IT244
'''

#This file serves as the module for "welcomebanner" which contains the welcome text and colors for the main.py program

#Import extra libraries
from colorama import Fore, Back, Style, init


#Define function which contains the welcome banner ascii and color formatting
def welcomeBanner():
    init(autoreset=True)
    print(Fore.BLUE + r"""
    
 ___    ____ _____ ______   ____  ____     __    ___                  
|   \  |    / ___/|      | /    ||    \   /  ]  /  _]                 
|    \  |  (   \_ |      ||  o  ||  _  | /  /  /  [_                  
|  D  | |  |\__  ||_|  |_||     ||  |  |/  /  |    _]                 
|     | |  |/  \ |  |  |  |  _  ||  |  /   \_ |   [_                  
|     | |  |\    |  |  |  |  |  ||  |  \     ||     |                 
|_____||____|\___|  |__|  |__|__||__|__|\____||_____|                 
                                                                      
    __   ____  _        __  __ __  _       ____  ______   ___   ____  
   /  ] /    || |      /  ]|  |  || |     /    ||      | /   \ |    \ 
  /  / |  o  || |     /  / |  |  || |    |  o  ||      ||     ||  D  )
 /  /  |     || |___ /  /  |  |  || |___ |     ||_|  |_||  O  ||    / 
/   \_ |  _  ||     /   \_ |  :  ||     ||  _  |  |  |  |     ||    \ 
\     ||  |  ||     \     ||     ||     ||  |  |  |  |  |     ||  .  \
 \____||__|__||_____|\____| \__,_||_____||__|__|  |__|   \___/ |__|\_|

     By W. Alec Akin for PUT IT244 - Python Programming with the legenedary Dr. Ed Lavieri                                                                 

    """)