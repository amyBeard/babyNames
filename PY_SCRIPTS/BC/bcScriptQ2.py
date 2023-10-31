#!/usr/bin/env python3

import sys
import getopt
import pandas as pd

def print_usage():
    print('Usage: top_names_for_year.py -i <file> -y <year>')

def top_names_for_year(csv_file_path, year, n=10):
    #reading CSV file into a pandas dataframe
    df = pd.read_csv(csv_file_path)

    #filter dataframe to only include rows for the specified year
    df = df[df['Year'] == year]

    #grouping the rows by name and sum the rank values to get total rank for each name
    name_ranks = df.groupby('Name')['Rank'].sum()

    #sorting the names by rank and take the top n names
    top_names = name_ranks.sort_values().head(n).index.tolist()

    #printing the top names
    print(f"Top {n} names for year {year}:")
    for name in top_names:
        print(name)

def main(argv):
    #setting the default values
    csv_file_path = None
    year = None
    n = 10
  
    #parsing the command line arguments
    try:
        opts, args = getopt.getopt(argv, "hi:y:", ["file=", "year="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--file"):
            csv_file_path = arg
        elif opt in ("-y", "--year"):
            year = int(arg)

    #checking that required arguments are provided
    if csv_file_path is None or year is None:
        print_usage()
        sys.exit(2)

    #calling top_names_for_year function with the specified arguments
    top_names_for_year(csv_file_path, year, n)

if __name__ == "__main__":
    main(sys.argv[1:])