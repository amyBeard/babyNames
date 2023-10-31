#!/usr/bin/env python3
# Libraries
import os
import sys
import choiceFunctions
import pandas
import csv

def question6():


    #if statements based on prov
    prov=choiceFunctions.provChoice()
    
    if prov==str(1):
        #BC
        #while user input is british columbia
        while True: 
            #calling the sex choice function and asking users for input
            sex=choiceFunctions.sexChoice()
            #if sex choice is female
            if (sex==str(1)):
                #running formattiing scrip for bc once again
                bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_GIRLS.csv -o OUTPUTS/bcGirlsNew"
                os.system(bcScript)
                #openig the result from bc script
                with open("OUTPUTS/bcGirlsNew.csv") as f:
                  #read csv
                  reader = csv.reader(f)
                  #for each row print it
                  for row in reader:
                    print(*row)
            if (sex==str(2)):
                bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_BOYS.csv -o OUTPUTS/bcBoysNew"
                os.system(bcScript)
                with open("OUTPUTS/bcBoysNew.csv") as f:
                  reader = csv.reader(f)
                  for row in reader:
                    print(*row)
            break

    elif prov==str(2):
        #ALBERTA
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #get inputs from user and based on sexChoice function, assign input and output file names
            sex=choiceFunctions.sexChoice()
            if (sex==str(1)):
                inputFile="./PY_SCRIPTS/ALBERTA/albertaFemaleAllYears.py -i ALBERTA.csv -o OUTPUTS/albertaFemale"
                outputFile="OUTPUTS/albertaFemale.csv"
            elif (sex==str(2)):
                inputFile="./PY_SCRIPTS/ALBERTA/albertaMaleAllYears.py -i ALBERTA.csv -o OUTPUTS/albertaMale"
                outputFile="OUTPUTS/albertaMale.csv"
            #exits if 1111 is entered
            elif (sex==str(1111)):
                return
            #run inputfile snd read and display outputFile
            os.system(inputFile)
            outputFile=pandas.read_csv(str(outputFile))
            print(outputFile)
            break
        

    elif prov==str(3):
        #ON
        while True: 
            #calling the sex choice function
            sex=choiceFunctions.sexChoice()
            #if sex choice is female
            if (sex==str(1)):
                #running the ontario script for formatting the ontario csv file into communal format
                onScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_female.csv -o OUTPUTS/onGirlsNew"
                #running the script
                os.system(onScript)
                #open the newly formatted file and reading each row and printing it
                with open("OUTPUTS/onGirlsNew.csv") as f:
                  reader = csv.reader(f)
                  for row in reader:
                    print(*row)
            if (sex==str(2)):
                onScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_male.csv -o OUTPUTS/onBoysNew"
                os.system(onScript)
                with open("OUTPUTS/onBoysNew.csv") as f:
                  reader = csv.reader(f)
                  for row in reader:
                    print(*row)
            break

    elif prov==str(4):
        #QUEBEC
        #while quebec is picked
        while True: 
            #calling the sex choice function, asking for user input for sex
            sex=choiceFunctions.sexChoice()
            if (sex==str(1)):
                #running the quebec script for formatting the quebec csv file into communal format
                quebec="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_FEMALE.csv -o OUTPUTS/quebecGirlsNew"
                #running the script
                os.system(quebec)
                #open the newly formatted file and reading each row and printing it
                with open("OUTPUTS/quebecGirlsNew.csv") as f:
                  reader = csv.reader(f)
                  for row in reader:
                    print(*row)
            #do same as above for male if user picks male instead
            if (sex==str(2)):
                quebec="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_MALE.csv -o OUTPUTS/quebecBoysNew"
                os.system(quebec)
                with open("OUTPUTS/quebecBoysNew.csv") as f:
                  reader = csv.reader(f)
                  for row in reader:
                    print(*row)
            break

    elif prov==str(5):

    #NEWFOUNDLAND
    #while loop makes sure inputs are correct and that system only runs once
     while True:

            #get inputs from user and based on sexChoice function, assign input and output file names
            sex=choiceFunctions.sexChoice()
            if (sex==str(1)):
                inputFile="./PY_SCRIPTS/NEWF/newfFemaleAllYears.py -i NEWFOUNDLAND -o OUTPUTS/newfFemale"
                outputFile="OUTPUTS/newfFemale.csv"
            elif (sex==str(2)):
                inputFile="./PY_SCRIPTS/NEWF/newfMaleAllYears.py -i NEWFOUNDLAND -o OUTPUTS/newfMale"
                outputFile="OUTPUTS/newfMale.csv"
            #exits if 1111 is entered
            elif (sex==str(1111)):
                return
            #run inputfile snd read and display outputFile  
            os.system(inputFile)
            outputFile=pandas.read_csv(str(outputFile))
            print(outputFile)
            break


    elif prov==str(6):
        #NEWBRUNSWICK
        while True:
            
            sex=choiceFunctions.sexChoice()
            if (sex==str(1)):
                inputFile="./PY_SCRIPTS/newbrunswick/nbFemaleAllYears.py -i NB.csv -o OUTPUTS/nbFemale"
                outputFile="OUTPUTS/nbFemale.csv"
            elif (sex==str(2)):
                inputFile="./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py -i NB.csv -o OUTPUTS/nbMale"
                outputFile="OUTPUTS/nbMale.csv"
            elif (sex==str(1111)):
                return

                
            os.system(inputFile)
            outputFile=pandas.read_csv(str(outputFile))
            print(outputFile)
            break

    elif prov==str(7):
        #NOVA SCOTIA
        while True:
            
            sex=choiceFunctions.sexChoice()
            if (sex==str(1)):
                inputFile="./PY_SCRIPTS/NS/nsFemaleAllYears.py -i NS.csv -o OUTPUTS/nsFemale"
                outputFile="OUTPUTS/nsFemale.csv"
            elif (sex==str(2)):
                inputFile="./PY_SCRIPTS/NS/nsMaleAllYears.py -i NS.csv -o OUTPUTS/nsMale"
                outputFile="OUTPUTS/nsMale.csv"
            elif (sex==str(1111)):
                return

            os.system(inputFile)
            outputFile=pandas.read_csv(str(outputFile))
            print(outputFile)
            break
    
    #exits if 1111 is entered
    elif prov==str(1111):
        return
    
    
