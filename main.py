#!/usr/bin/env python3
#./main.py

#MAIN SCRIPT FOR WHOLE PROGRAM

# Libraries
import os
import csv
import sys
from QUESTIONS import question1
from QUESTIONS import question2
from QUESTIONS import question3
from QUESTIONS import question5
from QUESTIONS import question6
from QUESTIONS import question7

#Loop displays menu, gets user input, and makes sure user input is only a number
#that is displayed in the menu
while True:
    #display menu
    print("\n\nMENU")
    print("\n#1. DISPLAY DATA FOR A YEAR")
    print("\n#2. DISPLAY TOP 10 FOR A YEAR")
    print("\n#3. DISPLAY DATA FOR ALL YEARS FOR A SPECIFIC NAME")
    print("\n#4. NUMBER OF MALE AND FEMALE NAMES FOR A SPECIFIC YEAR")
    print("\n#5. DISPLAY DATA FOR A SPAN OF YEARS")
    print("\n#6. DISPLAY DATA FOR A PROVINCE FOR ALL YEARS")
    print("\nENTER 1111 TO EXIT SYSTEM")

    #gets user choice
    choice=input("\nEnter choice of function from the menu: ")

    #only if user input is a number
    if (choice.isdigit()==True):

        #call appropriate function from QUESTIONS scripts
        if int(choice)==1:
            question1.question1()
        elif int(choice)==2:
            question2.question2()
        elif int(choice)==3:
            question3.question3()
        elif int(choice)==4:
            question5.question4()
        elif int(choice)==5:
            question6.question5()
        elif int(choice)==6:
            question7.question6()

       #exits system if 1111 is entered
        elif (int(choice)==1111):
            print("\nEXITING...")
            sys.exit(2)

        #otherwise display message
        else:
            print("\nInvalid entry, please enter a number from the menu.")
    else:
        print("\nInvalid entry, please enter a number from the menu.")


