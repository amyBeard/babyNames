#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/newbrunswick/nbFemaleRange.py
#./PY_SCRIPTS/newbrunswick/nbFemaleRange.py -i NB.csv -1 <year1> -2 <year2> -o OUTPUTS/nbFemale 

import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    if len(argv) < 7:
        print(
        "Usage: ./PY_SCRIPTS/newbrunswick/nbFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        "!!!"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:1:2:o:",
                                    ["input=","year1=","year2=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/newbrunswick/nbFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        "***"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/newbrunswick/nbFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
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

    
    names_F = []
    ranks_F= []
    rows=[]
    years_F=[]
    femaleList=[]
    totals_F=[]

    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if int(row[0])>=year1 and int(row[0])<=year2:
                rows.append(row)
    

        for row_1 in range(len(rows)):
            if (rows[row_1][1].upper()=='F'):
                femaleList.append(rows[row_1])

        counter=0
        totals_F.append([])
        for row_F in range (len(femaleList)):
            if femaleList[row_F][0] == femaleList[(row_F)-1][0]:
                names_F.append(femaleList[row_F][2])
                years_F.append(femaleList[row_F][0])
                totals_F[counter].append(femaleList[row_F][3])
            else:
                totals_F.append([])
                counter+=1
                names_F.append(femaleList[row_F][2])
                years_F.append(femaleList[row_F][0])
                totals_F[counter].append(femaleList[row_F][3])

        for i in range (len(totals_F)):
            for totals in totals_F[i]:
                ranks_F.append(totals_F[i].index(totals)+1)
        
        if len(femaleList) > 0:
            people = {'Rank':ranks_F,'Name': names_F, 'Year': years_F}
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
#   End of nbFemaleAllYears.py