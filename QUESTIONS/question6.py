#!/usr/bin/env python3
# Libraries
import os
import sys
import choiceFunctions
import pandas

def question5():

    
    #if statements based on prov
    prov=choiceFunctions.provChoice()
    
    if prov==str(1):
        #BC
        #running the commands below while user input is for bc
        while True:
            #calling the year choice function twice and storing into two different variables for the range
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            #if the year choice 1 is in range and so is the second year choice
            if (int(year1)>=1922) and (int(year1)<2022) and (int(year2)>=1922) and (int(year2)<2022) and year1<=year2:
                #calling the sex choice function for user input
                sex=choiceFunctions.sexChoice()
                #if choice is female: 
                if (sex==str(1)):
                    #runnign bc script to create the output file
                    bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_GIRLS.csv -o OUTPUTS/bcGirlsNew"
                    os.system(bcScript)
                    #setting input file equal to command line to run script for Q6 for newly formatted file as input
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ6.py -i OUTPUTS/bcGirlsNew.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/bcFemale" 
                    outputFile="OUTPUTS/bcFemale.csv"
                elif (sex==str(2)):
                    #runnign bc script to create the output file
                    bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_BOYS.csv -o OUTPUTS/bcBoysNew"
                    os.system(bcScript)
                    #setting input file equal to command line to run script for Q6 for newly formatted file as input
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ6.py -i OUTPUTS/bcBoysNew.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/bcMale " 
                    outputFile="OUTPUTS/bcMale.csv"
                elif (sex==str(1111)):
                    return
                #runnign input file to create the newly formatted file
                os.system(inputFile)
                #runnign the output file to print the desired output from newly formatyed file
                os.system(outputFile)
                outputFile=pandas.read_csv(str(outputFile))
                #printinng read information
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 1980 and 2020 and make sure that year1 <= year2")
        
    elif prov==str(2):
        #ALBERTA
        #while loop makes sure inputs are correct and that system only runs once
        while True:
            #get inputs from user and make sure years are within limit
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            if (int(year1)>=1980) and (int(year1)<2021) and (int(year2)>=1980) and (int(year2)<2021) and year1<=year2:
                sex=choiceFunctions.sexChoice()
                #based on sexChoice function, assign input and output file names
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/ALBERTA/albertaFemaleRange.py -i ALBERTA.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/albertaFemale " 
                    outputFile="OUTPUTS/albertaFemale_" + str(year1)+ "-" + str(year2) + ".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/ALBERTA/albertaMaleRange.py -i ALBERTA.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/albertaMale " 
                    outputFile="OUTPUTS/albertaMale_" + str(year1)+ "-" + str(year2) + ".csv"
                #exits if 1111 is entered
                elif (sex==str(1111)):
                    return
                
                #run inputfile snd read and display outputFile
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 1980 and 2020 and make sure that year1 <= year2")
        
        

    elif prov==str(3):
        #ON
        #running the commands below while user input is for bc
        while True:
            #calling the year choice function twice and storing into two different variables for the range
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            #if the year choice 1 is in range and so is the second year choice
            if (int(year1)>=1917) and (int(year1)<2021) and (int(year2)>=1917) and (int(year2)<2021 and year1<=year2):
                #calling the sex choice function for user input
                sex=choiceFunctions.sexChoice()
                #if sex is female
                if (sex==str(1)):
                    #runnign bc script to create the output file
                    ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_female.csv -o OUTPUTS/ontarioGirlsNew"
                    os.system(ontarioScript)
                    #setting input file equal to command line to run script for Q6 for newly formatted file as input, running with bcScript since input format is same
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ6.py -i OUTPUTS/ontarioGirlsNew.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/onFemale" 
                    outputFile="OUTPUTS/onFemale.csv"
                    #running the second command line
                    os.system(outputFile)
                elif (sex==str(2)):
                    ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_male.csv -o OUTPUTS/ontarioBoysNew"
                    os.system(ontarioScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ6.py -i OUTPUTS/ontarioBoysNew.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/onMale" 
                    outputFile="OUTPUTS/onMale.csv"
                    os.system(outputFile)
                elif (sex==str(1111)):
                    return
                #running the command set for input file
                os.system(inputFile)
                #reading the output file using pandas
                outputFile=pandas.read_csv(str(outputFile))
                #printing what has been read
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 1980 and 2020 and make sure that year1 <= year2")

    elif prov==str(4):
        #QUEBEC
        #running the commands below while user input is for bc
        while True:
            #calling the year choice function twice and storing into two different variables for the range
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            #if the year choice 1 is in range and so is the second year choice
            if (int(year1)>=1922) and (int(year1)<2022) and (int(year2)>=1922) and (int(year2)<2022) and year1<=year2:
                #calling the sex choice function for user input
                sex=choiceFunctions.sexChoice()
                #if sex is female
                if (sex==str(1)):
                    #runnign bc script to create the output file
                    bcScript="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_FEMALE.csv -o OUTPUTS/quebecGirlsNew"
                    os.system(bcScript)
                      #setting input file equal to command line to run script for Q6 for newly formatted file as input, running with bcScript since input format is same
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ6.py -i OUTPUTS/quebecGirlsNew.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/quebecFemale" 
                    outputFile="OUTPUTS/quebecFemale.csv"
                elif (sex==str(2)):
                    bcScript="./PY_SCRIPTS/BC/bcScript.py -i QUEBEC/QUEBEC_MALE.csv -o OUTPUTS/quebecBoysNew"
                    os.system(bcScript)
                    inputFile="./PY_SCRIPTS/BC/bcScriptQ6.py -i OUTPUTS/quebecBoysNew.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/quebecMale " 
                    outputFile="OUTPUTS/quebecMale.csv"
                elif (sex==str(1111)):
                    return
                #running input file and output file
                os.system(inputFile)
                os.system(outputFile)
                #reading output file using pandas
                outputFile=pandas.read_csv(str(outputFile))
                #printing the output file
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 1980 and 2020 and make sure that year1 <= year2")

    elif prov==str(5):
        #NEWFOUNDLAND
        ##while loop makes sure inputs are correct and that system only runs once
         while True:
            #get inputs from user and make sure years are within limit
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            if (int(year1)>=2003) and (int(year1)<2021) and (int(year2)>=2003) and (int(year2)<2021 and year1<=year2):
                sex=choiceFunctions.sexChoice()
                #based on sexChoice function, assign input and output file names
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/NEWF/newfFemaleRange.py -i NEWFOUNDLAND -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/newfFemale " 
                    outputFile="OUTPUTS/newfFemale_" + str(year1)+ "-" + str(year2) + ".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/NEWF/newfMaleRange.py -i NEWFOUNDLAND -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/newfMale " 
                    outputFile="OUTPUTS/newfMale_" + str(year1)+ "-" + str(year2) + ".csv"
                #exits if 1111 is entered
                elif (sex==str(1111)):
                    return
                
                #run inputfile snd read and display outputFile
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 2003 and 2020 and make sure that year1 <= year2")


    elif prov==str(6):
        #NEWBRUNSWICK
        while True:
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            if (int(year1)>=1980) and (int(year1)<2018) and (int(year2)>=1980) and (int(year2)<2018 and year1<=year2):
                sex=choiceFunctions.sexChoice()
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/newbrunswick/nbFemaleRange.py -i NB.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/nbFemale " 
                    outputFile="OUTPUTS/nbFemale_" + str(year1)+ "-" + str(year2) + ".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/newbrunswick/nbMaleRange.py -i NB.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/nbMale " 
                    outputFile="OUTPUTS/nbMale_" + str(year1)+ "-" + str(year2) + ".csv"
                elif (sex==str(1111)):
                    return
                
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 1980 and 2018 and make sure that year1 <= year2")

    elif prov==str(7):
        #NOVA SCOTIA
        while True:
            year1=choiceFunctions.yearChoice()
            year2=choiceFunctions.yearChoice()
            if (int(year1)>=1920) and (int(year1)<2022) and (int(year2)>=1920) and (int(year2)<2022 and year1<=year2):
                sex=choiceFunctions.sexChoice()
                if (sex==str(1)):
                    inputFile="./PY_SCRIPTS/NS/nsFemaleRange.py -i NS.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/nsFemale " 
                    outputFile="OUTPUTS/nsFemale_" + str(year1)+ "-" + str(year2) + ".csv"
                elif (sex==str(2)):
                    inputFile="./PY_SCRIPTS/NS/nsMaleRange.py -i NS.csv -1" +str(year1) +" -2 "+ str(year2) + " -o OUTPUTS/nsMale " 
                    outputFile="OUTPUTS/nsMale_" + str(year1)+ "-" + str(year2) + ".csv"
                elif (sex==str(1111)):
                    return
                
                os.system(inputFile)
                outputFile=pandas.read_csv(str(outputFile))
                print(outputFile)
                break
            else:
                print("\nPlease enter a years between 1920 and 2022 and make sure that year1 <= year2")

    #exits if 1111 is entered
    elif prov==str(1111):
        return