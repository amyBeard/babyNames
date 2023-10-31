#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/ALBERTA/albertaMaleRange.py
#./PY_SCRIPTS/ALBERTA/albertaMaleRange.py -i ALBERTA.csv -1 <year1> -2 <year2> -o OUTPUTS/albertaMale 

#script goes through alberta csv and makes csv that covers a span of 
#years for male data 

import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 7:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaMaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        "!!!"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:1:2:o:",
                                    ["input=","year1=","year2=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaMaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        "***"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/ALBERTA/albertaMaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
            "___"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-1", "--year1"):
            year1=int(arg)
        elif opt in ("-2", "--year2"):
            year2=int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + "_" + str(year1) + "-" + str(year2) + ".csv"

    #vars
    names_M = []
    ranks_M= []
    rows=[]
    years_M=[]
    maleList=[]

    #open csv file, delineate based on commas and append rows to list
    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if int(row[4])>=year1 and int(row[4])<=year2:
                rows.append(row)
    
        #if rows contain 'BOY' add to maleList
        for row_1 in range(len(rows)):
            if (rows[row_1][3].upper()=='BOY'):
                maleList.append(rows[row_1])

        #from male list append ranks and names to lists 
        for row_M in range (len(maleList)):
            ranks_M.append(maleList[row_M][0])
            names_M.append(maleList[row_M][1])
            years_M.append(maleList[row_M][4])    
        
        #Add info gathered to dataframe and export to csv file
        if len(maleList) > 0:
            people = {'Rank':ranks_M,'Name': names_M, 'Year': years_M}
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
#   End of albertaMaleRange.py