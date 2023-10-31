#!/usr/bin/env python3

import sys
import getopt
import pandas as pd

def print_usage():
    print('Usage: count_names_for_year.py -i <input_file> -y <year> -o <output_file>')

def count_names_for_year(male_csv_file_path, year, output_file_path):
    #reading male CSV file into a pandas dataframe
    male_df = pd.read_csv(male_csv_file_path)

    #filtering the male dataframe to only include rows for the specified year
    male_df = male_df[male_df['Year'] == year]

    #saving the filtered data to a CSV file
    male_df.to_csv(output_file_path + ".csv", index=False)
  

def main(argv):
    #setting the default values
    male_csv_file_path = None
    year = None
    output_file_path = None

    #parsing command line arguments
    try:
        opts, args = getopt.getopt(argv, "hi:y:o:", ["inputFile=", "year=", "outputFile="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            male_csv_file_path = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--outputFile"):
            output_file_path = arg

    #checking that required arguments are provided
    if male_csv_file_path is None or year is None:
        print_usage()
        sys.exit(2)

    #calling count_names_for_year function with the specified arguments
    count_names_for_year(male_csv_file_path, year, output_file_path)

if __name__ == "__main__":
    main(sys.argv[1:])
