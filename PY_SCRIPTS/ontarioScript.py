#!/usr/bin/env python3

import pandas as pd
import sys
import getopt

#parsing command-line arguments
input_file = ''
output_file = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], 'hi:o:', ['help', 'input=', 'output='])
except getopt.GetoptError:
    print('Usage: python script.py -i <input_file> -o <output_file>')
    sys.exit(2)
for opt, arg in opts:
    if opt in ('-h', '--help'):
        print('Usage: python script.py -i <input_file> -o <output_file>')
        sys.exit()
    elif opt in ('-i', '--input'):
        input_file = arg
    elif opt in ('-o', '--output'):
        output_file = arg

#reading the CSV file into a DataFrame
df = pd.read_csv(input_file, header=None, names=['Year', 'Name', 'Count', 'Rank'])

#grouping the DataFrame by year and calculate the rank based on the count
df['rank'] = df.groupby('Year')['Count'].rank(ascending=False, method='dense')

#converting the rank column to integers
df['Rank'] = df['Rank'].astype(int)

#reeordering the columns
df = df[['Rank', 'Name', 'Year']]

#writing the updated DataFrame back to a CSV file
df.to_csv(output_file + ".csv", index=False)
