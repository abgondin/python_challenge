# Modules
import os
import csv
import sys

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

profit_losses_list = []
change_sum = 0
greatest_increase = 0
greatest_decrease = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skips the header and points to the first data row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Determine first row value
    first_row = next(csvreader)
    previousvalue = int(first_row[1])
    row_count = 1
    total = previousvalue

    # Read each row of data after the header
    for row in csvreader:
        # Determines the number of rows which equate to months
        row_count = row_count + 1
        # Determines the total profit/losses
        total = total + int(row[1])
        # Calculates the difference in change
        nextvalue = int(row[1])
        # print(nextvalue)
        change = 0
        change = nextvalue - int(previousvalue)
        # print(change)
        change_sum = change_sum + change
        # print(change_sum)
        # Establishes the current row as new previous value
        previousvalue = int(row[1])
        # print(previousvalue)

        # Compares the profit/loss value between rows with greatest
        # Greatest has to be initialised outside for loop, otherwise resets
        if change > greatest_increase:
            # If change is bigger, stores as new greatest
            greatest_increase = change
            # Stores the corresponding month
            greatestmonth = row[0]
        if change < greatest_decrease:
            # If row is bigger, stores as new greatest
            greatest_decrease = change
            # Stores the corresponding month
            lowestmonth = row[0]

    avg_change = round((change_sum) / (row_count - 1), 2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total))
print("Average Change: $" + str(avg_change))
print(
    f'Greatest Increase in Profits: {greatestmonth} (${greatest_increase})')
print(
    f'Greatest Decrease in Profits: {lowestmonth} (${greatest_decrease})')

output_file = os.path.join("pybank.txt")

with open(output_file, "w") as datafile:
    print("Financial Analysis", file=datafile)
    print("----------------------------", file=datafile)
    print("Total Months: " + str(row_count), file=datafile)
    print("Total: $" + str(total), file=datafile)
    print("Average Change: $" + str(avg_change), file=datafile)
    print(
        f'Greatest Increase in Profits: {greatestmonth} (${greatest_increase})', file=datafile)
    print(
        f'Greatest Decrease in Profits: {lowestmonth} (${greatest_decrease})', file=datafile)
