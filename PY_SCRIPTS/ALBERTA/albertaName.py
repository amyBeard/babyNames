#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/ALBERTA/albertaName.py
#./PY_SCRIPTS/ALBERTA/albertaName.py -i ALBERTA.csv -n <name> -o OUTPUTS/alberta_ 

#script searches for a name in Alberta csv and adds data to a csv
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 6:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemaleAllYears.py -i <input file name> -n <name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:n:o:",
                                    ["input=","name","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemaleAllYears.py -i <input file name> -n <name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemaleAllYears.py -i <input file name> -n <name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-n", "--name"):
            name=arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + str(name) + ".csv"

    #vars
    names = []
    ranks= []
    years=[]
    nameList=[]

    #open csv file, delineate based on commas and append rows to list
    #rows are only appended if the second element stripped of spaces
    #is the same as the desired name
    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if (row[1].strip(" ")==str(name)):
                nameList.append(row)
    
        #from nameList ranks, names, and years are appened to appropriate lists
        for row in range (len(nameList)):
            ranks.append(nameList[row][0])
            names.append(nameList[row][1].strip(" "))
            years.append(nameList[row][4])    
        
        #Add info gathered to dataframe and export to csv file
        if len(nameList) > 0:
            people = {'Rank':ranks,'Name': names, 'Year': years}
            people_df = pd.DataFrame(people)

            people_df.sort_values(["Rank","Name","Year"],
                                    axis=0,
                                    ascending=[True,True,True],
                                    inplace=False)


            people_df.to_csv(outputFileName,
                                    sep=',',
                                    index=False,
                                    encoding='utf-8')
        


if __name__ == "__main__":
  main(sys.argv[1:])
#   End of albertaName.py