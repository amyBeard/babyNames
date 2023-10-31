#!/usr/bin/env python3

import sys
import getopt
import pandas as pd

def print_usage():
    print('Usage: count_names_for_years.py -i <input_file> -1 <start_year> -2 <end_year> -o <output_file>')

def count_names_for_years(male_csv_file_path, start_year, end_year, output_file_path):
    #reading male CSV file into a pandas dataframe
    male_df = pd.read_csv(male_csv_file_path)

    #filtering the male dataframe to only include rows for the specified year range
    male_df = male_df[(male_df['Year'] >= start_year) & (male_df['Year'] <= end_year)]

    #saving the filtered data to a CSV file
    male_df.to_csv(output_file_path + ".csv", index=False)

def main(argv):
    #setting the default values
    male_csv_file_path = None
    start_year = None
    end_year = None
    output_file_path = None

    #parsing command line arguments
    try:
        opts, args = getopt.getopt(argv, "hi:1:2:o:", ["inputFile=", "startYear=", "endYear=", "outputFile="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            male_csv_file_path = arg
        elif opt in ("-1", "--startYear"):
            start_year = int(arg)
        elif opt in ("-2", "--endYear"):
            end_year = int(arg)
        elif opt in ("-o", "--outputFile"):
            output_file_path = arg

    #checking that required arguments are provided
    if male_csv_file_path is None or start_year is None or end_year is None:
        print_usage()
        sys.exit(2)

    #calling count_names_for_years function with the specified arguments
    count_names_for_years(male_csv_file_path, start_year, end_year, output_file_path)

if __name__ == "__main__":
    main(sys.argv[1:])
