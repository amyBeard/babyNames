#!/usr/bin/env python3
#chmod 777 PY_SCRIPTS/NEWF/newfMaleRange.py
#./PY_SCRIPTS/NEWF/newfMaleRange.py -i NEWFOUNDLAND -1 <year1> -2 <year2> -o OUTPUTS/newfMale

#script goes through Newfoundland csvs and makes csv that covers a span of 
#years for male data 

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
        "Usage: ./PY_SCRIPTS/NEWF/newfMaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:1:2:o:",
                                    ["input=","year1", "year2","output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/NEWF/newfMaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/NEWF/newfMaleRange.py -i <input file name> -1 <year1> -2 <year2> -o <output file name base>"
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
    names_M=[]
    rowList=[]
    ranks_M=[]
    years_M=[]
    
    #same for loop but for user specifed years
    for year in range (year1,year2+1):
    
        inputFileName1=inputFileName+"/NF_"+str(year)+".csv"


        #open csv file, delineate based on commas and append rows to list
        with open(inputFileName1) as csvDataFile:

            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for row in csvReader:
                rowList.append(row)

            #add ranks, male names, and years to lists
            #2010 has female and male names swapped
            for row_M in range (len(rowList)):
                ranks_M.append(rowList[row_M][1])
                if (year!=2010):
                    names_M.append(rowList[row_M][0])
                else:
                    names_M.append(rowList[row_M][2])
                years_M.append(year)
                

    #Add info gathered to dataframe and export to csv file
    if len(rowList) > 0:
        people = {'Rank':ranks_M,'Name': names_M, 'Year': years_M}
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
#   End of newfMaleRange.py