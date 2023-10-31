#!/usr/bin/env python3

import sys
import getopt
import pandas as pd
import matplotlib.pyplot as plt

#getting command line options
def main(argv):
    inputFile = ''
    try:
        (opts, args) = getopt.getopt(argv, "hi:", ["input="])
    except getopt.GetoptError:
        print("Usage: ./PY_SCRIPTS/ -i <input file name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: ./PY_SCRIPTS/ -i <input file name>")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFile = arg
    if not inputFile:
        print("Please provide an input file name.")
        sys.exit(2)
    return inputFile

if __name__ == "__main__":
    inputFile = main(sys.argv[1:])
    #reading in the data from a CSV file
    df = pd.read_csv(str(inputFile))

    #asking the user to enter a name to graph
    nameStrip=inputFile.strip(".csv")
    nameSplit=nameStrip.split("_")
    name=nameSplit[1]

    #creating a new dataframe with only the rows for the given name
    name_df = df[df['Name'] == name]

    #plotting
    plt.plot(name_df['Year'], name_df['Rank'], label=name)

    #setting the title and the axis labels
    plt.title(f"Rank of the name '{name}' over time")
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    #reversing the y axis so ranks are in descending
    plt.gca().invert_yaxis()
    plt.show()
