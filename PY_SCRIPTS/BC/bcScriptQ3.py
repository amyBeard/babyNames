#!/usr/bin/env python3

import sys
import getopt
import pandas as pd

def print_usage():
    print('Usage: top_names_for_year.py -i <file> -n <name>')

def top_names_for_year(csv_file_path, name):
    #reading CSV file into a pandas dataframe
    df = pd.read_csv(csv_file_path)

    #filtering dataframe to only include rows for the specified name
    df = df[df['Name'] == name]

    #printing the rows showing the name, rank, and year
    print(f"Data for name {name}:")
    for index, row in df.iterrows():
        print(f"{row['Rank']},{name},{row['Year']}")

def main(argv):
    #setting default values
    csv_file_path = None
    name = None

    #parsing command line arguments
    try:
        opts, args = getopt.getopt(argv, "hi:n:", ["inputFile=", "name="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            csv_file_path = arg
        elif opt in ("-n", "--name"):
            name = arg

    #checking that required arguments are provided
    if csv_file_path is None or name is None:
        print_usage()
        sys.exit(2)

    #calling top_names_for_year function with the specified arguments
    top_names_for_year(csv_file_path, name)

if __name__ == "__main__":
    main(sys.argv[1:])
