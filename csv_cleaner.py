#Should be able to read CSV files and removes empty rows 
#and spits output

import csv

#use regex to remove the dollar signs
#use the pattern \p{Sc}

import re   


#open the csv file
with open ('example.csv', mode = 'r') as file:

    #Create a CSV reader object
    csv_reader = csv.reader(file)
    
    #read the header    
    header = next(csv_reader)
    print(f"Header: {header}")

    #Read each row of the CSV file
    for row in csv_reader:
        print(f"Row: {row}")

