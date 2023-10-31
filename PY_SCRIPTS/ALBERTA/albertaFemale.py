#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/ALBERTA/albertaFemale.py
#./PY_SCRIPTS/ALBERTA/albertaFemale.py -i ALBERTA.csv -y <year> -o OUTPUTS/AB_FEMALE

#script takes data from general Alberta csv and compiles
#and writes a csv with all data for females in alberta
#in a sepcific year
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 6:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:y:o:",
                                    ["input=", "year=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/ALBERTA/albertaFemale.py -i <input file name> -y <year> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + str(year) + ".csv"


    #vars
    names_F = []
    ranks_F= []
    rows=[]
    femaleList=[]

    #open csv file, delineate based on commas and append rows to list
    with open(inputFileName) as csvDataFile:
        
        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:

            if int(row[4]) == year:
                rows.append(row)
    

        #if rows contain 'GIRL' add to femaleList
        for row_1 in range(len(rows)):
            if (rows[row_1][3].upper()=='GIRL'):
                femaleList.append(rows[row_1])

            
        #from female list append ranks and names to lists
        for row_F in range (len(femaleList)):
            ranks_F.append(femaleList[row_F][0])
            names_F.append(femaleList[row_F][1])
            
        
        #Add info gathered to dataframe and export to csv file
        if len(femaleList) > 0:
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
#   End of albertaFemale.py