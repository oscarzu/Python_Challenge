import os
import csv
        
csvpath = os.path.join("Resources","PyBank_Data.csv")

with open(csvpath, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader)

        Months = 0
        Total_Rev_Change = 0
        Previous_Revenue = 0
        Present_Revenue = 0
        Revenue_Change = 0
        Max_Revenue_Change = 0
        Min_Revenue_Change = 0
        Total_Revenue = 0