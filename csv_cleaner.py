#Should be able to read CSV files and removes empty rows 
#and spits output

import csv

#path name so you can output cleaned data 


#imports Regex
import re


def clean_row(row):
    price = row['Price']
    if price =='':
    #if there is no price put None 
        row['Price'] = None
    else:
     #For the price row replace $ with nothing and just
     #leaves the price 
      price = re.sub(r'[^\d.]','', price)
      #price = price.replace('$','')
      #what was in the price row is now a float
      row['Price'] = float(price)
    return row
    

def main():
#Error handling for if we can't find the file
    try:
#open the csv file
        with open ('example.csv', mode = 'r') as file:

            #Create a CSV reader object
            csv_reader = csv.DictReader(file)
            #collect all cleaned rows
            clean_rows = []

            #Read each row of the CSV file
            for row in csv_reader:
                cleaned = clean_row(row)
                clean_rows.append(cleaned)

        #Checks that the loops is done and rows are collected
        if not clean_rows:
            print("No data found in the file.")
            return

        with open('output.csv', mode='w', newline='') as f:
            # use the column names from the first cleaned row as headers
            writer = csv.DictWriter(f, fieldnames=clean_rows[0].keys())
            # write the header row
            writer.writeheader()
            # write all cleaned rows
            writer.writerows(clean_rows)
        print(f"Done. {len(clean_rows)} rows written to output.")

        for row in clean_rows: #Prints the output to command line
            print(row)

    except FileNotFoundError:
        print("We can't find the file")
if __name__ == "__main__":
# open output file for writing
    main()
