#import os & csv
import os
import csv

#create path to read csv file
csvpath = os.path.join('Resources', 'budget_data.csv')


#csv module read
with open(csvpath) as infile:

    # csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(infile, delimiter=',')

    # reads the header row first
    csv_header = next(csvreader)
    
    # Print Messages to match format in HW
    print("Financial Analysis")
    print("-----------------")

    # variable that will become the counter for dates
    months = 0

    # variable that will become the balance for profits/losses in column 2
    balance = 0
    
    # variable for change of value
    change = 0

    #variable for max profit change
    max_profit_change = 0

    # Set first value flag
    first_val_YN = False

    # read through each row of data from column 1
    for row in csvreader:
        #set first_val = row[1]
        if first_val_YN is False:
            first_val = int(row[1])
            first_val_YN = True

        #count every row in column 1 list; Column 1 = row [0]
        months += 1

        #adding every row value in column 2 list; Column 2 = row[1]
        balance += int(row[1])
        
        #row86 value
        last_val = int(row[1])
    next
    
    #math expression for average change. (months - 1) = the amount of rows - 1 because there are 85 changes compared to 86 rows
    change = (last_val - first_val)/(months-1)

    # F print message that displays number of months
    print(f'Total Months: {months}')
    print(f'Total ${balance} ')
    print(f'Average Change: ${str(round(change,2))} ')