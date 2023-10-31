#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/newbrunswick/nbName.py
#./PY_SCRIPTS/newbrunswick/nbName.py -i NB.csv -n <name> -o OUTPUTS/nb_ 

import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    if len(argv) < 6:
        print(
        "Usage: ./PY_SCRIPTS/newbrunswick/nbName.py -i <input file name> -n <name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:n:o:",
                                    ["input=","name","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/newbrunswick/nbName.py -i <input file name> -n <name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/newbrunswick/nbName.py -i <input file name> -n <name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-n", "--name"):
            name=arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + str(name) + ".csv"

    
    names = []
    totals= []
    years=[]
    nameList=[]
    ranks=[]
    ranks1=[]
    maleList=[]
    names2=[]
    sex=''

    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        count=0
        for row in csvReader:

            if (row[2].upper()==str(name).upper()):
                if count==0:
                    sex=row[1]
                    count+=1
                nameList.append(row)
    
        if sex=='M':
            newInputFile="./PY_SCRIPTS/newbrunswick/nbMaleAllYears.py -i NB.csv -o OUTPUTS/NBmaleAllYears"
            newOutputFile="OUTPUTS/NBmaleAllYears.csv"
            os.system(newInputFile)
            with open(newOutputFile) as csvDataFile2:
                next(csvDataFile2)
                csvReader2 = csv.reader(csvDataFile2, delimiter=',')    
                for row2 in csvReader2: 
                    if row2[1]==str(name).upper():
                        ranks.append(row2[0])

        if sex=='F':
            newInputFile="./PY_SCRIPTS/newbrunswick/nbFemaleAllYears.py -i NB.csv -o OUTPUTS/NBfemaleAllYears"
            newOutputFile="OUTPUTS/NBfemaleAllYears.csv"
            os.system(newInputFile)
            with open(newOutputFile) as csvDataFile2:
                next(csvDataFile2)
                csvReader2 = csv.reader(csvDataFile2, delimiter=',')    
                for row2 in csvReader2: 
                    if row2[1]==str(name).upper():
                        ranks.append(row2[0])           


        for row in range (len(nameList)):
            
            names.append(nameList[row][2])
            years.append(nameList[row][0])


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
#   End of nbName.py