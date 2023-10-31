#FROM MENU 1-- MENU 2
#PICK PROVINCE(S)--MENU OF PROVINCES
#PICK YEARS
#PICK SEX
#PICK NAME

import sys

#function gets user input for provinces from a menu
def provChoice():

    #displays menu
    print("\n\nPROVINCE/STATE DISPLAY")
    print("\n#1. BRITISH COLUMBIA")
    print("\n#2. ALBERTA")
    print("\n#3. ONTARIO")
    print("\n#4. QUEBEC")
    print("\n#5. NEWFOUNDLAND")
    print("\n#6. NEWBRUNSWICK")
    print("\n#7. NOVA SCOTIA")
    print("\nENTER 1111 TO EXIT TO MAIN")
    
    #while loop to insure user can only input certain values
    #asks user for their choice from menu and only accepts one of the numbers feautured
    #exits if 1111 is entered
    while True:
        choice1=input("\nEnter choice of province from the menu: ")
        if (choice1.isdigit()==True):
            if (int(choice1)>=1) and (int(choice1)<8):
                return choice1
            elif (int(choice1)==1111):
                print("\nEXITING...")
                return
            else:
                print("\nInvalid entry, please enter a number from the menu.")
        else:
            print("\nInvalid entry, please enter a number from the menu.")

#function simply gets a year input from user
def yearChoice():

    #while loop just checks user input is a number
    while True:
        choice2=input("\nEnter year: ")
        if (choice2.isdigit()==True):
                return choice2
        else:
            print("\nInvalid entry, please enter a number.")

#function gets user input for sex from a menu
def sexChoice():

    #displays menu
    print("\n\nSEX MENU")
    print("\n#1. FEMALE")
    print("\n#2. MALE")
    print("\nENTER 1111 TO EXIT TO MAIN")
    
    #while loop to insure user can only input certain values
    #asks user for their choice from menu and only accepts one of the numbers featured
    #exits if 1111 is entered
    while True:
        choice3=input("\nEnter choice of sex from the menu: ")
        if (choice3.isdigit()==True):
            if (int(choice3)>=1) and (int(choice3)<3):
                return choice3
            elif (int(choice3)==1111):
                print("\nEXITING...")
                return
            else:
                print("\nInvalid entry, please enter a number from the menu.")
        else:
            print("\nInvalid entry, please enter a number from the menu.")

#function gets input for a name from user
def nameChoice():

    #while loop gets input from user and makes sure it's not a number
    while True:
        choice4=input("\nEnter name: ")
        if (choice4.isdigit()==False):
            return choice4
        else:
            print("\nInvalid entry, please enter a name")

#function gets y/n input for weither user wants a graph
def graphChoice():
    #loop asks for user input and only allows them to enter y/Y or n/N
    while True:
        choice5=input("\nWould you like to see a graph for name data (Y/N): ")
        if (choice5.isdigit()==False):
            if (choice5.upper()=='Y'):
                return 1
            elif (choice5.upper()=='N'):
                return 2
            else:
                print("\nInvalid entry, please enter Y or N")
        else:
            print("\nInvalid entry, please enter Y or N")