#!/usr/bin/env python3

#libraries
import csv
import pandas as pd
import os
import sys
import getopt

#defining a class to represent each row
class Row:
    #setting the record with a name and empty years and rank dictionaries
    def __init__(self, person):
        self.record_name = person
        self.record_years = {} #creating the dictionary for year
        self.record_rank = {} #making ictionary for rank
    #returns to us the rank of the record for a given year
    def getRank(self, year):
        return self.record_rank[year]  
    #returns to us the years of the record
    def yearFind(self):
        return self.record_years  
    #updating the rank of the record for a given year
    def newRecordRank(self, year, rank):
        self.record_rank[year] = rank
#defining a function to sort records based on their frequency in a given year
def sort_frequency(record, year):
    years = record.record_years
    if year in years:
        #sorting first by frequency, then by name, then by first character
        return (-int(years[year]), record.record_name, ord(record.record_name[0]))
    else:
        #in the case that the year is not in the record's (rows) years, give it a frequency of 0
        return (0, record.record_name, ord(record.record_name[0]))

#defining the main function
def main(argv):

    #command line argument expects 4 arguments
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
    #setting the start and end years
    beginning = 1922
    end = 2022

    #setting empty list for records, a dictionary to map names to record indices, and a counter for record indices
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
                years = record.record_years
                for year in range(beginning, end):
                    years[year] = row[year - beginning + 2].replace(',', '')
                #adding the record to the list, adding the name:record index pair to the dictionary, and incrementing the counter
                records.append(record)
                record_names[row[0]] = record_count
                record_count += 1

    #for every year, sorting the records based on frequency and update their ranks
    for year in range(beginning, end):
        sorted_frequency_records = sorted(records, key=lambda x: sort_frequency(x, year))
        for j, record in enumerate(sorted_frequency_records, 1):
            records[record_names[record.record_name]].newRecordRank(year, j)

    #opening the output CSV file
    with open(outputFileName, 'w', newline='') as file:
        writer = csv.writer(file)
        #writing the header row
        writer.writerow(["Rank", "Name", "Year"])
        #iterating over each year
        for year in range(beginning, end):
            #initializing temporary variables
          sorted_frequency_records = sorted(records, key=lambda x: sort_frequency(x, year))
        for j, record in enumerate(sorted_frequency_records, 1):
            records[record_names[record.record_name]].newRecordRank(year, j)

        #opening the output CSV file
    with open(outputFileName, 'w', newline='') as file:
        #writing into the csv file
        writer = csv.writer(file)
        #alternating the order of the columns
        writer.writerow(["Rank", "Name", "Year"])
        #iterating through defined beginning and defined end
        for year in range(beginning, end):
            #setting variables temp and newrank equal to -1 and 0 respectively to keep track of rank changes
            temp, new_rank = -1, 0
            #sorting ranked list which frequency, name and year for each row in the rows, by current year
            ranked_list = [(record.record_name, record.getRank(year)) for record in records if year in record.record_rank]
            ranked_list.sort(key=lambda x: x[1])
            for record in ranked_list:
                #finding the years in which the current record appears
                years = records[record_names[record[0]]].yearFind()
                if temp == -1:
                    #if current row is first one found for current year, rank is one
                    temp = years[year]
                    new_rank = 1
                #else if it isnt, then compare the current row to the previous and adjust the rank value in accordance
                else:
                    if temp != years[year]:
                        temp = years[year]
                        #increment the new rank
                        new_rank += 1
                #checking if our current row has data for our current year
                if years[year] != '0':
                    #alternating the columns
                    writer.writerow([new_rank, record[0].title(), year])


if __name__ == "__main__":
    main(sys.argv[1:])

