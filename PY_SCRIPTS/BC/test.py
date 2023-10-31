#!/usr/bin/env python3

import sys
import getopt
import pandas as pd

def print_usage():
    print('Usage: top_names_for_year.py -i <file> -y <year>')


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

    df = pd.read_csv(inputFileName)

    #filtering dataframe to only include rows for the specified year
    df = df[df['Year'] == year]

    #grouping the rows by name and sum the rank values to get total rank for each name
    name_ranks = df.groupby('Name')['Rank'].sum()

    name_ranks.to_csv(outputFileName,
                                    sep=',',
                                    index=False,
                                    encoding='utf-8')


if __name__ == "__main__":
    main(sys.argv[1:])