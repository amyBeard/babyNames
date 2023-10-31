#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/NEWF/newfFemaleRange.py
#./PY_SCRIPTS/NEWF/newfFemaleRange.py -i NEWFOUNDLAND -1 <year1> -2 <year2> -o OUTPUTS/newfFemale

#script goes through Newfoundland csv and makes csv that covers a span of 
#years for female data 

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd


def main(argv):

    #section checks if command line argument is valid and exits if not. Then gathers and process info based on argument
    if len(argv) < 7:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:1:2:o:",
                                    ["input=","year1", "year2","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/NEWF/newfFemaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-1", "--year1"):
            year1 = int(arg)
        elif opt in ("-2", "--year2"):
            year2 = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName1 = outputFileNameBase  + "_" + str(year1) + "-" +str(year2) + ".csv"

    #variables
    names_F=[]
    rowList=[]
    ranks_F=[]
    years_F=[]
    
    #neccesary for loop instead with inputed years
    for year in range (year1,year2+1):
    
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
#   End of newfFemaleRange.py