#!/usr/bin/env python3
# Libraries
import os
import sys
import choiceFunctions
import pandas

def question4():

    #if statements based on prov
    prov=choiceFunctions.provChoice()
    
    if prov==str(1):
        #BC
        #running the following command lines while true
        while True:
            #calling the year choice functions
            year=choiceFunctions.yearChoice()
            #ranging the years
            if (int(year)>=1922) and (int(year)<2021):
                #running the script to reformat the csv file and then running another script below to manipulate the new csv
                bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_GIRLS.csv -o OUTPUTS/bcGirlsNew"
                os.system(bcScript)
                #running question 5 file for girls
                inputFile1="./PY_SCRIPTS/BC/bcScriptQ5.py -i OUTPUTS/bcGirlsNew.csv -y" +str(year) + " -o OUTPUTS/bcFemale" 
                outputFile1="OUTPUTS/bcFemale.csv"
                #doing the same process for boys
                bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_BOYS.csv -o OUTPUTS/bcBoysNew"
                os.system(bcScript)
                inputFile2="./PY_SCRIPTS/BC/bcScriptQ5.py -i OUTPUTS/bcBoysNew.csv -y" +str(year) + " -o OUTPUTS/bcMale " 
                outputFile2="OUTPUTS/bcMale.csv"
                #running the input file which holds question 5 manipulations, putting it into output files
                os.system(inputFile1)
                #reading the output file using pandas
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                #after reading printing the lines
                print("\nThere were",len(outputFile1),"female names registered in BC in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in BC in", str(year))
                break
            else:
                print("\nPlease enter a year between 1922 and 2020")

    elif prov==str(2):
        #ALBERTA
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #get inputs from user and make sure years are within limit
            year=choiceFunctions.yearChoice()
            if (int(year)>=1980) and (int(year)<2021):
                #creates 2 input and output files
                inputFile1="./PY_SCRIPTS/ALBERTA/albertaFemale.py -i ALBERTA.csv -y " +str(year) + " -o OUTPUTS/AB_FEMALE" 
                outputFile1="OUTPUTS/AB_FEMALE" + str(year)+".csv"
                inputFile2="./PY_SCRIPTS/ALBERTA/albertaMale.py -i ALBERTA.csv -y " +str(year) + " -o OUTPUTS/AB_MALE" 
                outputFile2="OUTPUTS/AB_MALE" + str(year)+".csv"
                
                #runs and reads input and output files
                os.system(inputFile1)
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                #dispplays length of output files
                print("\nThere were",len(outputFile1),"female names registered in Alberta in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in Alberta in", str(year))
                break
            else:
                print("\nPlease enter a year between 1980 and 2020")
        
        

    elif prov==str(3):
        #ON
        #running while ontario is selected by user
        while True:
            #calling the year choice function to ask people input a year
            year=choiceFunctions.yearChoice()
            #if statement as long as the inputted year is correctly within the range
            if (int(year)>=1917) and (int(year)<2021):
                #running question 5 file for girls
                ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_female.csv -o OUTPUTS/ontarioGirlsNew"
                os.system(ontarioScript)
                inputFile1="./PY_SCRIPTS/BC/bcScriptQ5.py -i OUTPUTS/ontarioGirlsNew.csv -y" +str(year) + " -o OUTPUTS/onFemale" 
                outputFile1="OUTPUTS/onFemale.csv"
                #running the input file which holds question 5 manipulations, putting it into output files
                ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_male.csv -o OUTPUTS/ontarioMaleNew"
                os.system(ontarioScript)
                inputFile2="./PY_SCRIPTS/BC/bcScriptQ5.py -i OUTPUTS/ontarioMaleNew.csv -y" +str(year) + " -o OUTPUTS/onMale " 
                outputFile2="OUTPUTS/onMale.csv"
                #running the two input files for formatting purposes
                os.system(inputFile1)
                #reading the newly outputted file, and printing the amount of lines counted below
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                #after reading printing the amount of lines
                print("\nThere were",len(outputFile1),"female names registered in Ontario in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in Ontario in", str(year))
                break
            else:
                print("\nPlease enter a year between 1922 and 2020")

    elif prov==str(4):
        #QUEBEC
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #calling the year choice functions for user input
            year=choiceFunctions.yearChoice()
            #get inputs from user and make sure years are within limit
            if (int(year)>=1980) and (int(year)<2022):
                #calling quebec script to reformat the files
                quebecScript="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_FEMALE.csv -o OUTPUTS/quebecGirlsNew"
                os.system(quebecScript)
                #manipulating the already ordered formatting files into a output files
                inputFile1="./PY_SCRIPTS/BC/bcScriptQ5.py -i OUTPUTS/quebecGirlsNew.csv -y" +str(year) + " -o OUTPUTS/quebecFemale" 
                outputFile1="OUTPUTS/quebecFemale.csv"

                quebecScript="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_MALE.csv -o OUTPUTS/quebecGirlsNew"
                os.system(quebecScript)
                inputFile2="./PY_SCRIPTS/BC/bcScriptQ5.py -i OUTPUTS/ontarioMaleNew.csv -y" +str(year) + " -o OUTPUTS/quebecMale " 
                outputFile2="OUTPUTS/quebecMale.csv"
                #running the input file which holds question 5 manipulations, putting it into output files
                os.system(inputFile1)
                #reading the newly outputted file, and printing the amount of lines counted below
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                #after reading printing the amount of lines
                print("\nThere were",len(outputFile1),"female names registered in Quebec in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in Quebec in", str(year))
                break
            else:
                print("\nPlease enter a year between 1922 and 2020")

    elif prov==str(5):
        #NEWFOUNDLAND
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #get inputs from user and make sure years are within limit
            year=choiceFunctions.yearChoice()
            if (int(year)>=2003) and (int(year)<2021):
                #creates 2 input and output files
                inputFile1="./PY_SCRIPTS/NEWF/newfoundlandFemale.py -i NEWFOUNDLAND -y " +str(year) + " -o OUTPUTS/newfFemale" 
                outputFile1="OUTPUTS/newfFemale" + str(year)+".csv"
                inputFile2="./PY_SCRIPTS/NEWF/newfoundlandMale.py -i NEWFOUNDLAND -y " +str(year) + " -o OUTPUTS/newfMale" 
                outputFile2="OUTPUTS/newfMale" + str(year)+".csv"
                
                #runs and read both input and output files
                os.system(inputFile1)
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                #prints length of output files
                print("\nThere were",len(outputFile1),"female names registered in Newfoundland in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in Newfoundland in", str(year))
                break
            else:
                print("\nPlease enter a year between 2003 and 2020")

    elif prov==str(6):
        #NEWBRUNSWICK
        while True:
            year=choiceFunctions.yearChoice()
            #get inputs from user and make sure years are within limit
            if (int(year)>=1980) and (int(year)<2018):
                #running question 5 file for girls
                inputFile1="./PY_SCRIPTS/newbrunswick/nbFemale.py -i NB.csv -y " +str(year) + " -o OUTPUTS/NB_FEMALE" 
                outputFile1="OUTPUTS/NB_FEMALE" + str(year)+".csv"
                inputFile2="./PY_SCRIPTS/newbrunswick/nbMale.py -i NB.csv -y " +str(year) + " -o OUTPUTS/NB_MALE" 
                outputFile2="OUTPUTS/NB_MALE" + str(year)+".csv"
                
                os.system(inputFile1)
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                print("\nThere were",len(outputFile1),"female names registered in Newbrunswick in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in Newbrunswick in", str(year))
                break
            else:
                print("\nPlease enter a year between 1980 and 2018")

    elif prov==str(7):
        #NOVA SCOTIA
        while True:
            year=choiceFunctions.yearChoice()
            if (int(year)>=1920) and (int(year)<2022):
                inputFile1="./PY_SCRIPTS/NS/novaScotiaFemale.py -i NS.csv -y " +str(year) + " -o OUTPUTS/NS_FEMALE" 
                outputFile1="OUTPUTS/NS_FEMALE" + str(year)+".csv"
                inputFile2="./PY_SCRIPTS/NS/novaScotiaMale.py -i NS.csv -y " +str(year) + " -o OUTPUTS/NS_MALE" 
                outputFile2="OUTPUTS/NS_MALE" + str(year)+".csv"
                
                os.system(inputFile1)
                outputFile1=pandas.read_csv(str(outputFile1))
                os.system(inputFile2)
                outputFile2=pandas.read_csv(str(outputFile2))
                print("\nThere were",len(outputFile1),"female names registered in Nova Scotia in", str(year))
                print("\nThere were",len(outputFile2),"male names registered in Nova Scotia in", str(year))
                break
            else:
                print("\nPlease enter a year between 1920 and 2022")

    #exits if 1111 is entered
    elif prov==str(1111):
        return
   

    
