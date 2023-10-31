#!/usr/bin/env python3
#chmod 777 ./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py
#./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py -i NB.csv -o OUTPUTS/NBmaleAllYears

import sys
import getopt
import csv
import pandas as pd


def main(argv):

    if len(argv) < 4:
        print(
        "Usage: ./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:o:",
                                    ["input=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py -i <input file name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + ".csv"

    
    names_M = []
    ranks_M= []
    rows=[]
    years_M=[]
    maleList=[]
    totals_M=[]

    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            rows.append(row)
    

        for row_1 in range(len(rows)):
            if (rows[row_1][1].upper()=='M'):
                maleList.append(rows[row_1])

            
        counter=0
        totals_M.append([])
        for row_M in range (len(maleList)):
            if maleList[row_M][0] == maleList[(row_M)-1][0]:
                names_M.append(maleList[row_M][2])
                years_M.append(maleList[row_M][0])
                totals_M[counter].append(maleList[row_M][3])
            else:
                totals_M.append([])
                counter+=1
                names_M.append(maleList[row_M][2])
                years_M.append(maleList[row_M][0])
                totals_M[counter].append(maleList[row_M][3])

        for i in range (len(totals_M)):
            for totals in totals_M[i]:
                ranks_M.append(totals_M[i].index(totals)+1)
        
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
#   End of nbMaleAllYears.py