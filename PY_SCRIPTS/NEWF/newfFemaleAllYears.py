#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/NEWF/newfFemaleAllYears.py
#./PY_SCRIPTS/NEWF/newfFemaleAllYears.py -i NEWFOUNDLAND -o OUTPUTS/newfFemale

#This script processes all data for newfoundland and outputs a csv file
#with all female data for all years

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 1:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfFemaleAllYears.py -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:o:",
                                    ["input=", "output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfFemaleAllYears.py -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/NEWF/newfFemaleAllYears.py -i <input file name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName1 = outputFileNameBase  + ".csv"

    #vars
    names_F=[]
    rowList=[]
    ranks_F=[]
    years_F=[]
    
    #have to add for loop due to file structure
    #files are all seperated by years, so must cycle through all years
    for year in range (2003,2021):
    
        inputFileName1=inputFileName+"/NF_"+str(year)+".csv"

        #open csv file, delineate based on commas and append rows to list
        with open(inputFileName1) as csvDataFile:

            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for row in csvReader:
                rowList.append(row)

            #add ranks, female names, and years to lists
            #2010 has female and male names swapped
            for row_F in range (len(rowList)):
                ranks_F.append(rowList[row_F][1])
                if (year!=2010):
                    names_F.append(rowList[row_F][2])
                else:
                    names_F.append(rowList[row_F][0])
                years_F.append(year)
                
    #Add info gathered to dataframe and export to csv file
    if len(rowList) > 0:
        people = {'Rank':ranks_F,'Name': names_F, 'Year': years_F}
        people_df = pd.DataFrame(people)

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
#   End of newfFemaleAllYears.py