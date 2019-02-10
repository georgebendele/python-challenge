# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None) # skip the header
    

# Your task is to create a Python script that analyzes the records to calculate each of the following:
    
# The total number of months included in the dataset
    # set month counter to baseline
    countMonths = 0
    # set summed P/L to baseline
    addrows = 0
    # stores a list of all P/L values
    plval = []
    # stores a list of change in P/L from one month to next
    plchange = []
    
    maxval = 0
    maxName = ""
    minval = 0
    minName = ""
    
    # iterate through rows
    for rows in reader:
        # add to month count for each entry
        countMonths = countMonths + 1
        
# The net total amount of "Profit/Losses" over the entire period
        # change column 2 string to number
        current_row = float(rows[1])
        # adds row value to the sum of all previous P/L values
        addrows = addrows + current_row

# The average of the changes in "Profit/Losses" over the entire period
        # store P/L values in list
        plval.append(current_row)
        # if there are 2 or more months, then calculate average profit/loss
        if countMonths > 1:
            thischange = (current_row - plval[-2])
            # adds change in P/L to list
            plchange.append(thischange)
            # averages P/L changes and rounds to 2 decimals
            avg_change = round(sum(plchange)/len(plchange),2)
    
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


            if current_row > maxval:
                maxval = current_row
                maxName = rows[0]
                maxChange = max(plchange)
            elif current_row < minval:
                minval = current_row
                minName = rows[0]
                minChange = min(plchange)
                
# Print results

    print(f"\nFinancial Analysis")
    print(f"_______________________________")
    print(f"Total Months: {countMonths}")
    print(f"Total: ${addrows}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {maxName} ${maxChange}")
    print(f"Greatest Decrease in Profits: {minName} ${minChange}")

filename = 'results.txt'
with open(filename, 'w') as file_object:
    file_object.write(
                  f"\nFinancial Analysis\n"
                  f"_______________________________\n"
                  f"Total Months: {countMonths}\n"
                  f"Total: ${addrows}\n"
                  f"Average Change: ${avg_change}\n"
                  f"Greatest Increase in Profits: {maxName} ${maxChange}\n"
                  f"Greatest Decrease in Profits: {minName} ${minChange}"
                      )



