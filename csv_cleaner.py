#Should be able to read CSV files and removes empty rows 
#and spits output

import csv

#path name so you can output cleaned data 

import os 


#open the csv file
with open ('example.csv', mode = 'r') as file:

    #Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    #read the header    
    header = next(csv_reader)
    print(f"Header: {header}")

    #Read each row of the CSV file
    for row in csv_reader:
        print(f"Row: {row}")

price = row['Price']
if row['Price'] =='':
    #if there is no price put none 
        print(f"none")
else:
   # converts to float
       price.replace('$','')

f = open("output.txt", "w")

print('Hello World', file=f)

f.close()
