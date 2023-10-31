#!/usr/bin/env python3

#FUNCTIONALITY: This script presents users with province choices and and while loops through os.system to run each provincial file

# Libraries
import os
import sys
import choiceFunctions
import pandas

def question1():

    #if statements based on prov
    prov=choiceFunctions.provChoice()
    
    if prov==str(1):
        #BC
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            bcScript=""
            #prompting for year choice
            year=choiceFunctions.yearChoice()
            #ranging year
            if (int(year)>=1922) and (int(year)<2022):
                #calling sexchoice function
                sex=choiceFunctions.sexChoice()
                #depending on sex
                if (sex==str(1)):
                    #os.system for command line, running file into format and then running question file
                    bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_GIRLS.csv -o OUTPUTS/bcGirlsNew"
                    os.system(bcScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ1.py -i OUTPUTS/bcGirlsNew.csv -y" +str(year)
                    os.system(inputFile)
                elif (sex==str(2)):
                    bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_BOYS.csv -o OUTPUTS/bcBoysNew"
                    os.system(bcScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ1.py -i OUTPUTS/bcBoysNew.csv -y" +str(year)
                    os.system(inputFile)
                elif (sex==str(1111)):
                    return
                break
            else:
                print("\nPlease enter a year between 1922 and 2021")

    elif prov==str(2):
        #ALBERTA
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #get inputs from user and make sure years are within limit
            year=choiceFunctions.yearChoice()
            if (int(year)>=1980) and (int(year)<2021):
                sex=choiceFunctions.sexChoice()
                #based on sexChoice function, assign input and output file names
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/ALBERTA/albertaFemale.py -i ALBERTA.csv -y " +str(year) + " -o OUTPUTS/AB_FEMALE" 
                    outputFile="OUTPUTS/AB_FEMALE" + str(year)+".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/ALBERTA/albertaMale.py -i ALBERTA.csv -y " +str(year) + " -o OUTPUTS/AB_MALE" 
                    outputFile="OUTPUTS/AB_MALE" + str(year)+".csv"
                #exits if 1111 is entered
                elif (sex==str(1111)):
                    return
                
                #run inputfile snd read and display outputFile
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a year between 1980 and 2020")
        
        

    elif prov==str(3):
        #ON
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            onScript=""
            #calling the year choice function
            year=choiceFunctions.yearChoice()
            #ranging the years
            if (int(year)>=1917) and (int(year)<2021):
                #os.system for command line, running file into format and then running question file to re-sort and print
                sex=choiceFunctions.sexChoice()
                if (sex==str(1)):
                    ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_female.csv -o OUTPUTS/ontarioGirlsNew"
                    os.system(ontarioScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ1.py -i OUTPUTS/ontarioGirlsNew.csv -y" +str(year)
                    os.system(inputFile)
                elif (sex==str(2)):
                    ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_male.csv -o OUTPUTS/ontarioBoysNew"
                    os.system(ontarioScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ1.py -i OUTPUTS/ontarioBoysNew.csv -y" +str(year)
                    os.system(inputFile)
                elif (sex==str(1111)):
                    return
                break
            else:
                print("\nPlease enter a year between 1917 and 2021")

    elif prov==str(4):
        #QUEBEC
        #while loop makes sure inputs are correct and that system only runs once
        while True: 
            #calling the year choice function
            year=choiceFunctions.yearChoice()
            #ranging the years
            if (int(year)>=1980) and (int(year)<2022):
                #running sex choice
                sex=choiceFunctions.sexChoice()
                #os.system for command line, running file into format and then running question file to re-sort and print
                if (sex==str(1)):
                    quebecScript="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_FEMALE.csv -o OUTPUTS/quebecGirlsNew"
                    os.system(quebecScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ1.py -i OUTPUTS/quebecGirlsNew.csv -y" +str(year)
                    os.system(inputFile)
                elif (sex==str(2)):
                    quebecScript="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_MALE.csv -o OUTPUTS/quebecBoysNew"
                    os.system(quebecScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ1.py -i OUTPUTS/quebecBoysNew.csv -y" +str(year)
                    os.system(inputFile)
                elif (sex==str(1111)):
                    return
                break
            else:
                print("\nPlease enter a year between 1917 and 2021")

    elif prov==str(5):
        #NEWFOUNDLAND
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #get inputs from user and make sure years are within limit
            year=choiceFunctions.yearChoice()
            if (int(year)>=2003) and (int(year)<2021):
                sex=choiceFunctions.sexChoice()
                #based on sexChoice function, assign input and output file names
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/NEWF/newfoundlandFemale.py -i NEWFOUNDLAND -y " +str(year) + " -o OUTPUTS/newfFemale" 
                    outputFile="OUTPUTS/newfFemale" + str(year)+".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/NEWF/newfoundlandMale.py -i NEWFOUNDLAND -y " +str(year) + " -o OUTPUTS/newfMale" 
                    outputFile="OUTPUTS/newfMale" + str(year)+".csv"
                #exits if 1111 is entered
                elif (sex==str(1111)):
                    return
                
                #run inputfile snd read and display outputFile
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a year between 2003 and 2020")

    elif prov==str(6):
        #NEWBRUNSWICK
        while True:
            year=choiceFunctions.yearChoice()
            if (int(year)>=1980) and (int(year)<2018):
                sex=choiceFunctions.sexChoice()
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/newbrunswick/nbFemale.py -i NB.csv -y " +str(year) + " -o OUTPUTS/NB_FEMALE" 
                    outputFile="OUTPUTS/NB_FEMALE" + str(year)+".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/newbrunswick/nbMale.py -i NB.csv -y " +str(year) + " -o OUTPUTS/NB_MALE" 
                    outputFile="OUTPUTS/NB_MALE" + str(year)+".csv"
                elif (sex==str(1111)):
                    return
                
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a year between 1980 and 2018")

    elif prov==str(7):
        #NOVA SCOTIA
        while True:
            year=choiceFunctions.yearChoice()
            if (int(year)>=1920) and (int(year)<2022):
                sex=choiceFunctions.sexChoice()
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/NS/novaScotiaFemale.py -i NS.csv -y " +str(year) + " -o OUTPUTS/NS_FEMALE" 
                    outputFile="OUTPUTS/NS_FEMALE" + str(year)+".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/NS/novaScotiaMale.py -i NS.csv -y " +str(year) + " -o OUTPUTS/NS_MALE" 
                    outputFile="OUTPUTS/NS_MALE" + str(year)+".csv"
                elif (sex==str(1111)):
                    return

                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a year between 1920 and 2022")
    
    #exits if 1111 is entered
    elif prov==str(1111):
        return
    
    

    
