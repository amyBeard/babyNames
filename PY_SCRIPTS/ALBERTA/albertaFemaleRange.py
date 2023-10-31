#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/ALBERTA/albertaFemaleRange.py
#./PY_SCRIPTS/ALBERTA/albertaFemaleRange.py -i ALBERTA.csv -1 <year1> -2 <year2> -o OUTPUTS/albertaFemale 

#script goes through alberta csv and makes csv that covers a span of 
#years for female data 
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 7:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:1:2:o:",
                                    ["input=","year1=","year2=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
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

    #variables
    names_F = []
    ranks_F= []
    rows=[]
    years_F=[]
    femaleList=[]

    #open csv file, delineate based on commas and append rows to list
    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if int(row[4])>=year1 and int(row[4])<=year2:
                rows.append(row)
    

        #if rows contain 'GIRL' add to femaleList
        for row_1 in range(len(rows)):
            if (rows[row_1][3].upper()=='GIRL'):
                femaleList.append(rows[row_1])

        #from female list append ranks, names, and years to lists  
        for row_F in range (len(femaleList)):
            ranks_F.append(femaleList[row_F][0])
            names_F.append(femaleList[row_F][1])
            years_F.append(femaleList[row_F][4])    
        
        #Add info gathered to dataframe and export to csv file
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
#   End of albertaFemaleRange.py