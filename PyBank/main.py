# Modules
import os
import csv

# Path for csv file
budget_csv = os.path.join("resources","budget_data.csv")

# Open the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)
    row = next(csvreader)

    # Print heading
    print(" ")
    print("                Financial Analysis")
    print("----------------------------------------------------")
    print(" ")
 
    # Set variables to default values
    total_months = 0
    total_amount = 0
    prev_profit_losses = int(row[1])
    profit_losses_change = 0
    list_of_changes = []
    total_months += 1
    total_amount += int(row[1])
    count_of_averages = 0
    greatest_increase_amnt = int(row[1])
    greatest_decrease_amnt = int(row[1])
   
    # Loop through rows in csv file and make calculations
    for row in csvreader:

        # Calculate the total number of months included in the dataset
        total_months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period
        profit_losses_change = int(row[1]) - prev_profit_losses
        list_of_changes.append(profit_losses_change)
        prev_profit_losses = int(row[1])
        count_of_averages += 1

        # Calculate the greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_increase_amnt:
            greatest_increase_amnt = int(row[1])
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in profits (date and amount) over the entire period
        elif int(row[1]) < greatest_decrease_amnt:
            greatest_decrease_amnt = profit_losses_change
            greatest_decrease_month = row[0] 

    # Calculate the average of the changes in "Profit/Losses"
    average_change = sum(list_of_changes) / count_of_averages

    # Calculate the greatest increase in profits over the entire period
    greatest_increase_amnt = max(list_of_changes)

    # Print analysis to the terminal
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amnt})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amnt})")

# Specify output path
pybank_analysis = os.path.join("Analysis","PyBank-Analysis.txt")

# Open the text file, initialize text writer, and write data to the text file
with open(pybank_analysis, 'w') as txtfile:
    txtfile.write(f"                Financial Analysis\n")
    txtfile.write(f"----------------------------------------------------\n")
    txtfile.write(f" \n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_amount}\n")
    txtfile.write(f"Average Change: ${round(average_change,2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amnt})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amnt})\n")