import os
import csv
        
csvpath = os.path.join("Resources","PyBank_Data.csv")

with open(csvpath, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader)

