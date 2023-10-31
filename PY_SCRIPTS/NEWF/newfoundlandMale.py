#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/NEWF/newfoundlandMale.py
#./PY_SCRIPTS/NEWF/newfoundlandMale.py -i NEWFOUNDLAND -y <year> -o OUTPUTS/newfMale 

#script takes data from general Newfoundland csvs and compiles
#and writes a csv with all data for males in Newfoundland
#in a sepcific year

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 4:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfoundlandMale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:y:o:",
                                    ["input=", "output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfoundlandMale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/NEWF/newfoundlandMale.py -i <input file name> -y <year> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName1 = outputFileNameBase + str(year) + ".csv"

    inputFileName=inputFileName+"/NF_"+str(year)+".csv"
    
    #variables
    names_M=[]
    rowList=[]
    ranks_M=[]

    #open csv file, delineate based on commas and append rows to list
    with open(inputFileName) as csvDataFile:

        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            rowList.append(row)

        #add ranks, male names, and years to lists
        #2010 has female and male names swapped
        for row_M in range (len(rowList)):
            ranks_M.append(rowList[row_M][1])
            if year!=2010:
                names_M.append(rowList[row_M][0])
            else:
                names_M.append(rowList[row_M][2])
        

        #Add info gathered to dataframe and export to csv file
        if len(rowList) > 0:
            people = {'Rank':ranks_M,'Name': names_M}
            people_df = pd.DataFrame(people)

            people_df.sort_values(["Rank","Name"],
                                    axis=0,
                                    ascending=[True,True],
                                    inplace=False)

            rankedPeople_df = people_df.assign(Year=year)

            rankedPeople_df.to_csv(outputFileName1,
                                    sep=',',
                                    index=False,
                                    encoding='utf-8')
            
        
if __name__ == "__main__":
  main(sys.argv[1:])
#   End of newfoundlandMale.py