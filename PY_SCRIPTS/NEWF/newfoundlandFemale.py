#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/NEWF/newfoundlandFemale.py
#./PY_SCRIPTS/NEWF/newfoundlandFemale.py -i NEWFOUNDLAND -y <year> -o OUTPUTS/newfFemale 

#script takes data from general Newfoundland csvs and compiles
#and writes a csv with all data for females in Newfoundland
#in a sepcific year

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 6:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfoundlandFemale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:y:o:",
                                    ["input=", "year=","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfoundlandFemale.py -i <input file name> -y <year> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/NEWF/newfoundlandFemale.py -i <input file name> -y <year> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + str(year) + ".csv"

    inputFileName=inputFileName+"/NF_"+str(year)+".csv"
     
    #variables
    names_F = []
    rowList=[]
    ranks_F= []

    #open csv file, delineate based on commas and append rows to list
    with open(inputFileName) as csvDataFile:

        next(csvDataFile)
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            rowList.append(row)

        #add ranks, female names, and years to lists
        #2010 has female and male names swapped
        for row_F in range (len(rowList)):
            ranks_F.append(rowList[row_F][1])
            if year!=2010:
                names_F.append(rowList[row_F][2])
            else:
                names_F.append(rowList[row_F][0])

        #Add info gathered to dataframe and export to csv file
        if len(rowList) > 0:
            people = {'Rank':ranks_F,'Name': names_F, 'Year':year}
            people_df = pd.DataFrame(people)

            #           What is this doing? sorts the people_df dataframe with number and name columns, with axis zero saying it should be done along the rows. It then sorts and displays the top 5 and bottom 5 names per year displayed in the form of index found at, name, number, and rank
            people_df.sort_values(["Rank","Name","Year"],
                                    axis=0,
                                    ascending=[True,True,True],
                                    inplace=False)

            #           What is this doing? writes the data in the rankedPeople_df dataframe to a csv file. Doesnt write the index, uses a comma to sperate as delimitter
            people_df.to_csv(outputFileName,
                                    sep=',',
                                    index=False,
                                    encoding='utf-8')
            
        
if __name__ == "__main__":
  main(sys.argv[1:])
#   End of newfoundlandFemale.py