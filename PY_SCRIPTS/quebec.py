#!/usr/bin/env python3

#libraries
import csv
import pandas as pd
import os
import sys
import getopt

#defining a class to represent each record, consists of name, year, rank: blueprint
class Row:
    #setting the record with a name and empty years and rank dictionaries
    def __init__(self, person):
        self.name = person
        self.years = {} # dictionary of year:value pairs
        self.rank = {} # dictionary of year:rank pairs
    #getting the years of the record
    def yearFind(self):
        return self.years
    #getting the rank of the record for a given year
    def getRank(self, year):
        return self.rank[year]
    #updating the rank of the record for a given year
    def newRecordRank(self, year, rank):
        self.rank[year] = rank
#defining a function to sort records based on their frequency in a given year
def sortingFrequency(record, year):
    years = record.years
    if year in years:
        #sorting first by frequency, then by name, then by first character's ASCII value
        return (-int(years[year]), record.name, ord(record.name[0]))
    else:
        #if the year is not in the record's (rows) years, give it a frequency of 0
        return (0, record.name, ord(record.name[0]))

#definging the main function
def main(argv):

    if len(argv) <4:
        print(
        "Usage: ./PY_SCRIPTS -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    try:
        (opts, arg) = getopt.getopt(argv, "i:o:",
                                    ["input=", "output="])
    except getopt.GetoptError:
        print(
        "Usage: ./PY_SCRIPTS/ -i <input file name> -o <output file name base>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
            "Usage: ./PY_SCRIPTS/ -i <input file name> -o <output file name base>"
            )
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase  + ".csv"
    #setting the  start and end years based off of this csv file
    beginning = 1980
    end = 2019

    #initializing empty list for records, a dictionary to map names to record indices, and a counter for record indices
    records = []
    record_names = {}
    record_count = 0

    #opening the input CSV file
    with open(inputFileName, encoding="UTF-8") as csvfile:
        #reading the CSV file using the csv module
        reader = csv.reader(csvfile)
        #iterating over each row
        for row in reader:
            #skipping the header row
            if row[0] != "Name":
                #creating a new Record object and add its year:value pairs to its dictionary
                record = Row(row[0])
                years = record.years
                for year in range(beginning, end):
                    years[year] = row[year - beginning + 2].replace(',', '')
                #adding the record to the list, add the name:record index pair to the dictionary, and increment the counter
                records.append(record)
                record_names[row[0]] = record_count
                record_count += 1

    #for each year, sorting the records based on frequency and update their ranks
    for year in range(beginning, end):
        sorted_frequency_records = sorted(records, key=lambda x: sortingFrequency(x, year))
        for j, record in enumerate(sorted_frequency_records, 1):
            records[record_names[record.name]].newRecordRank(year, j)

    #writing into the output CSV file
    with open(outputFileName, 'w', newline='') as file:
        writer = csv.writer(file)
        #writing the header row
        writer.writerow(["Rank", "Name", "Year"])
        #iterating over each year
        for year in range(beginning, end):
            #intializing temporary variables
          sorted_frequency_records = sorted(records, key=lambda x: sortingFrequency(x, year))
        for j, record in enumerate(sorted_frequency_records, 1):
            records[record_names[record.name]].newRecordRank(year, j)

        #opening the output CSV file
    with open(outputFileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Name", "Year"]) #writing in a header
        for year in range(beginning, end):
            #initializing temporary variables to hold current and next rank
            temp, new_rank = -1, 0
            #sorting ranked list which frequency, name and year for each row in the rows, by current year
            ranked_list = [(record.name, record.getRank(year)) for record in records if year in record.rank]
            #sorting the ranked_list by the frequency in ascending
            ranked_list.sort(key=lambda x: x[1])
            for record in ranked_list:
                #finding the years in which the current record appears
                years = records[record_names[record[0]]].yearFind()
                #if current row is first one found for current year, rank is one
                if temp == -1:
                    temp = years[year]
                    new_rank = 1
                #else if it isnt, then compare the current row to the previous and adjust the rank value in accordance
                else:
                    if temp != years[year]:
                        temp = years[year]
                        #incrementing the new rank
                        new_rank += 1
                #checking if our current row has data for our current year
                if years[year] != '0':
                    #alternating the columns in accordance to desired output
                    writer.writerow([new_rank, record[0].title(), year]) 


if __name__ == "__main__":
    main(sys.argv[1:])


