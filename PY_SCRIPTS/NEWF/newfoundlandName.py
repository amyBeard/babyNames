#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/NEWF/newfoundlandName.py
#./PY_SCRIPTS/NEWF/newfoundlandName.py -i NEWFOUNDLAND -n <name> -o OUTPUTS/newfoundland_

#script searches for a name in Newfoundland csv and adds data to a csv
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
        "Usage: ./PY_SCRIPTS/NEWF/newfoundlandName.py -i <input file name> -n <name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:n:o:",
                                    ["input=","name","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfoundlandName.py -i <input file name> -n <name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/NEWF/newfoundlandName.py -i <input file name> -n <name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-n", "--name"):
            name=arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase + str(name) + ".csv"

    #vars
    names=[]
    ranks=[]
    years=[]
    
     #have to add for loop due to file structure
    #files are all seperated by years, so must cycle through all years
    for year in range (2003,2021):
    
        inputFileName1=inputFileName+"/NF_"+str(year)+".csv"

        #open csv file, delineate based on commas and append rows to list
        #add rows only if name is found either male names column or female column
        #adds years, names. ranks to lists if name is found
        with open(inputFileName1) as csvDataFile:

            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for row in csvReader:
                if name.upper() in row[2].upper().split("/"):
                    years.append(year)
                    ranks.append(row[1])
                    names.append(row[2])

                elif name.upper() in row[0].upper().split("/"):
                    years.append(year)
                    ranks.append(row[1])
                    names.append(row[0])
    
    #Add info gathered to dataframe and export to csv file
    if len(years) > 0:
        people = {'Rank':ranks,'Name': names,'Year':years}
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
#   End of newfoundlandName.py