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

    # variable that will become the counter for dates
    months = 0

    # variable that will become the balance for profits/losses in column 2
    balance = 0
    
    # variable for change of value
    change = 0

    #variable for max profit change
    greatest_increase = ["",0]
    greatest_decrease = ["",999999]
    
    prev_balance = 0

    # Set first value flag
    first_val_YN = False

    # read through each row of data from column 1
    for row in csvreader:
        
        #count every row in column 1 list; Column 1 = row [0]
        months += 1

        #adding every row value in column 2 list; Column 2 = row[1]
        balance += int(row[1])
        #set first_val = row[1]
        if months == 1:
            prev_balance = int(row[1])
            # prev_baln = Value from row 1

        if months > 1:
            profit_change = int(row[1]) - prev_balance
            # month 2: profit_change = month 2 value - month 1 value
            # month 3: profit_cahnge = month 3 value - month 2 value
            prev_balance = int(row[1])
            # month 2: prev_balnce = month 2 value
            # moth 3: prev_balnce = month 3 value

            if profit_change > greatest_increase[1]:
                # if profit_change (+) > 0
                greatest_increase[0] = row[0]
                #greatest_increase[0] = Januarry
                greatest_increase[1] = profit_change
                #greatest_increase[1] = Feb - Jan (+)

            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_change
        else:
            prev_balance = int(row[1])
            first_val = int(row[1])
            
        # if first_val_YN is False:
        #     first_val = int(row[1])
        #     first_val_YN = True
        
        #row86 value
        last_val = int(row[1])
        if months > 1:
            change = (last_val - first_val)/(months-1)
    
  # Print Messages to match format in HW
    print("Financial Analysis")
    print("-----------------")
    print(f'Total Months: {months}')
    print(f'Total ${balance} ')
    print(f'Average Change: ${str(round(change,2))} ')
    print(f'Greatest Increase in Profits: {greatest_increase[0]} : ${greatest_increase[1]}')
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]} : ${greatest_decrease[1]}')

#locates directory for new text file
output_path = os.path.join("py_bank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
new_text_file = open(output_path, 'w')
new_text_file.write("Financial Analysis\n")
new_text_file.write("-----------------\n")
new_text_file.write(f'Total Months: {months}\n')
new_text_file.write(f'Total ${balance}\n')
new_text_file.write(f'Average Change: ${str(round(change,2))}\n')
new_text_file.write(f'Greatest Increase in Profits: {greatest_increase[0]} : ${greatest_increase[1]}\n')
new_text_file.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} : ${greatest_decrease[1]}\n')
new_text_file.close()