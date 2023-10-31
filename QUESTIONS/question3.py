#!/usr/bin/env python3
# Libraries
import os
import sys
import choiceFunctions
import pandas
from pathlib import Path

def question3():

    #if statements based on prov
    prov=choiceFunctions.provChoice()
    
    if prov==str(1):
        #BC
        #while true run the following
        while True:
            #graph is false until user input initializes to 1
            graph=0
            #calling the sex choice function
            sex=choiceFunctions.sexChoice()
            #if user exits the sex chocie function
            if (sex==str(1111)):
                return
            #else do the following depending on the sex choice
            elif (sex==str(1)):
                #calling the name choice function, user can input thier names
                name=choiceFunctions.nameChoice()
                #runs the format file first and then the question file, same files used from bc
                bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_GIRLS.csv -o OUTPUTS/bcGirlsNew"
                os.system(bcScript)
                #runnign the correct script which reformats the formatted file to print desire output
                inputFile="./PY_SCRIPTS/BC/bcScriptQ3.py -i OUTPUTS/bcGirlsNew.csv -n " +str(name)
                os.system(inputFile)
                #callign the graph choice function
                graph=choiceFunctions.graphChoice()
            elif (sex==str(2)):
                name=choiceFunctions.nameChoice()
                bcScript="./PY_SCRIPTS/BC/bcScript.py -i BC/BC_BOYS.csv -o OUTPUTS/bcBoysNew"
                os.system(bcScript)
                inputFile="./PY_SCRIPTS/BC/bcScriptQ3.py -i OUTPUTS/bcBoysNew.csv -n " +str(name)
                os.system(inputFile)
                graph=choiceFunctions.graphChoice()
            #if graph choice is yes, graph is created based on name
            if (graph==1):
                    graphFile="./graph.py -i" + str(bcScript)
                    os.system(bcScript)
                    break
            else:
                 break

    elif prov==str(2):
        #ALBERTA
        inputFile=''
        #gets user input and assigns input/output files
        name=choiceFunctions.nameChoice()
        inputFile="./PY_SCRIPTS/ALBERTA/albertaName.py -i ALBERTA.csv -n " +str(name) + " -o OUTPUTS/alberta_ " 
        outputFile1="OUTPUTS/alberta_" + str(name)+".csv"

        #runs inputfile and checks that outputfile exists/ was created
        #then reads and prints output file
        os.system(inputFile)
        if (Path(str(outputFile1)).is_file()):
            outputFile=pandas.read_csv(str(outputFile1))
            print(outputFile)
            
            #gets graphChoice input and displays graph based on answer
            graph=choiceFunctions.graphChoice()
            if (graph==1):
                graphFile="./graph.py -i " + str(outputFile1)
                os.system(graphFile)
        else:
            print("\nNO DATA FOR THIS NAME")

    elif prov==str(3):
        #ON
        #runnign while true
        while True:
            #setting graph to 0 until it is called and initialized
            graph=0
            #calling sex choice function
            sex=choiceFunctions.sexChoice()
            if (sex==str(1111)):
                return
            #depending on sex choice do the following
            elif (sex==str(1)):
                #caling name choice function for user to input name
                name=choiceFunctions.nameChoice()
                #running script to refromat ontario first and then calling bc question file
                ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_female.csv -o OUTPUTS/ontarioGirlsNew"
                os.system(ontarioScript)
                #running the question file
                inputFile="./PY_SCRIPTS/BC/bcScriptQ3.py -i OUTPUTS/ontarioGirlsNew.csv -n " +str(name)
                os.system(inputFile)
                #calling graph choice function, asking if users want to input a graph for the chosen name
                graph=choiceFunctions.graphChoice()
            elif (sex==str(2)):
                name=choiceFunctions.nameChoice()
                ontarioScript="./PY_SCRIPTS/ontarioScript.py -i ONTARIO/ontario_male.csv -o OUTPUTS/ontarioBoysNew"
                os.system(ontarioScript)
                inputFile="./PY_SCRIPTS/BC/bcScriptQ3.py -i OUTPUTS/ontarioBoysNew.csv -n " +str(name)
                os.system(inputFile)
                graph=choiceFunctions.graphChoice()
            #if the graph is 1, then run the graphs cript for the format file
            if (graph==1):
                    graphFile="./graph.py -i" + str(bcScript)
                    os.system(bcScript)
                    break
            else:
                 break

    elif prov==str(4):
        #QUEBEC
        #following runs while quebec is selected
        while True:
            #graph is set to 0 until initialized by user after it is called
            graph=0
            #calling the sex choice function
            sex=choiceFunctions.sexChoice()
            if (sex==str(1111)):
                return
            #depending on sex coice run the following
            elif (sex==str(1)):
                #name function is called for user input 
                name=choiceFunctions.nameChoice()
                #quebec is first reformatted into our communal format
                quebec="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_FEMALE.csv -o OUTPUTS/quebecGirlsNew"
                os.system(quebec)
                #a question file is then run with bc script which prints from the communal format desired output
                inputFile="./PY_SCRIPTS/BC/bcScriptQ3.py -i OUTPUTS/quebecGirlsNew.csv -n " +str(name)
                os.system(inputFile)
                #graph choice is called
                graph=choiceFunctions.graphChoice()
            #depending on sex do the folllowing
            elif (sex==str(2)):
                #calling the name function
                name=choiceFunctions.nameChoice()
                quebec="./PY_SCRIPTS/quebec.py -i QUEBEC/QUEBEC_MALE.csv -o OUTPUTS/quebecBoysNew"
                os.system(quebec)
                inputFile="./PY_SCRIPTS/BC/bcScriptQ3.py -i OUTPUTS/quebecBoysNew.csv -n " +str(name)
                os.system(inputFile)
                graph=choiceFunctions.graphChoice()
            #running the graph.py file if selected by user
            if (graph==1):
                    graphFile="./graph.py -i" + str(bcScript)
                    os.system(bcScript)
                    break
            else:
                 break

    elif prov==str(5):
        #NEWFOUNDLAND
        #gets user input and assigns input/output files
        name=choiceFunctions.nameChoice()
        inputFile="./PY_SCRIPTS/NEWF/newfoundlandName.py -i NEWFOUNDLAND -n " +str(name) + " -o OUTPUTS/newfoundland_" 
        outputFile1="OUTPUTS/newfoundland_" + str(name)+".csv"

        #runs inputfile and checks that outputfile exists/ was created
        #then reads and prints output file
        os.system(inputFile)
        if (Path(str(outputFile1)).is_file()):
            outputFile=pandas.read_csv(str(outputFile1))
            print(outputFile)
            
            #gets graphChoice input and displays graph based on answer
            graph=choiceFunctions.graphChoice()
            if (graph==1):
                graphFile="./graph.py -i " + str(outputFile1)
                os.system(graphFile)
        else:
            print("\nNO DATA FOR THIS NAME")

    elif prov==str(6):
        #NEWBRUNSWICK
            name=choiceFunctions.nameChoice()
            inputFile="./PY_SCRIPTS/newbrunswick/nbName.py -i NB.csv -n " +str(name) + " -o OUTPUTS/nb_" 
            outputFile1="OUTPUTS/nb_" + str(name)+".csv"

            os.system(inputFile)

            if (Path(str(outputFile1)).is_file()):
                outputFile=pandas.read_csv(str(outputFile1))
                print(outputFile)
            
                graph=choiceFunctions.graphChoice()
                if (graph==1):
                     graphFile="./graph.py -i " + str(outputFile1)
                     os.system(graphFile)
            else:
                 print("\nNO DATA FOR THIS NAME")

    elif prov==str(7):
        #NOVA SCOTIA
            name=choiceFunctions.nameChoice()
            inputFile="./PY_SCRIPTS/NS/nsName.py -i NS.csv -n " +str(name) + " -o OUTPUTS/ns_" 
            outputFile1="OUTPUTS/ns_" + str(name)+".csv"

            os.system(inputFile)

            if (Path(str(outputFile1)).is_file()):
                outputFile=pandas.read_csv(str(outputFile1))
                print(outputFile)
            
                graph=choiceFunctions.graphChoice()
                if (graph==1):
                     graphFile="./graph.py -i " + str(outputFile1)
                     os.system(graphFile)
            else:
                 print("\nNO DATA FOR THIS NAME")


    #exits if 1111 is entered
    elif prov==str(1111):
        return
    
    
