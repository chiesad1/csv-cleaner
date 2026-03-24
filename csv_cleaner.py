#Should be able to read CSV files and removes empty rows 
#and spits output

import csv

#path name so you can output cleaned data 

import os
#imports Regex
import re


def clean_row(row):
    price = row['Price']
    if price =='':
    #if there is no price put none 
        row['Price'] = None
    else:
   
      price = re.sub(r'[^\d.]','', price)
      #price = price.replace('$','')
      row['Price'] = float(price)
    return row
    

#open the csv file
with open ('example.csv', mode = 'r') as file:

    #Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    #read the header    
    #header = next(csv_reader)
    #print(f"Header: {header}")

    #Read each row of the CSV file
    for row in csv_reader:
    #old function    
    #print(f"Row: {row}")
        #new function
        cleaned = clean_row(row)
        print(cleaned)


f = open("output.txt", "w")

print('Hello World', file=f)

f.close()
