#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    if len(argv) < 6:
        print(
        "Usage: ./PY_SCRIPTS/novaScotiaFemale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:y:o:",
                                    ["input=", "year=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/novaScotiaFemale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/novaScotiaFemale.py -i <input file name> -y <year> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + str(year) + ".csv"

    
    names_F = []
    ranks_F= []
    rows=[]
    totals_F=[]

    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if int(row[0]) == year:
                rows.append(row)

        for row_1 in range(len(rows)):
            if (rows[row_1][1].upper()=='F'):
                names_F.append(rows[row_1][2]) 
                totals_F.append(rows[row_1][3])
        
        for totals in totals_F:
            ranks_F.append(totals_F.index(totals)+1)

        if len(names_F) > 0:
            people = {'Rank':ranks_F,'Name': names_F,'Year': year}
            people_df = pd.DataFrame(people)

            people_df.sort_values(["Rank","Name", "Year"],
                                    axis=0,
                                    ascending=[True,True,True],
                                    inplace=False)

            people_df.to_csv(outputFileName,
                                    sep=',',
                                    index=False,
                                    encoding='utf-8')
        


if __name__ == "__main__":
  main(sys.argv[1:])
#   End of novaScotiaFemale.py