#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    if len(argv) <4:
        print(
        "Usage: ./PY_SCRIPTS/quebecBoys.py -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:o:",
                                    ["input=", "output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/quebecBoys.py -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/quebecBoys.py -i <input file name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName1 = outputFileNameBase  + ".csv"

    names_M=[]
    rowList=[]
    ranks_M=[]
    years_M=[]
    
    for year in range (2000,2021):
    
        with open(inputFileName) as csvDataFile:

            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for row in csvReader:
                rowList.append(row)

            for row_M in range (len(rowList)):
                ranks_M.append(rowList[row_M][1])
                names_M.append(rowList[row_M][0])
                years_M.append(year)
                

    if len(rowList) > 0:
        people = {'Rank':ranks_M,'Name': names_M,'Year':years_M}
        people_df = pd.DataFrame(people)

         #filtering rows with Rank = 0
        people_df = people_df[people_df.Rank != "0"]

        people_df.sort_values(["Rank","Name","Year"],
                                axis=0,
                                ascending=[True,True,True],
                                inplace=False)

        people_df.to_csv(outputFileName1,
                                sep=',',
                                index=False,
                                encoding='utf-8')
            
        
if __name__ == "__main__":
  main(sys.argv[1:])
#   End of quebecBoys.py
