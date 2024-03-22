import os
import csv

# Path to the budget data CSV file
budget_data_csv = os.path.join("budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Count the total number of months
        total_months += 1
        
        # Extract profit/loss from the row
        profit_loss = int(row[1])
        
        # Calculate the total profit/loss
        total_profit_loss += profit_loss
        
        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])

        # Store the current profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index]

greatest_decrease = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the analysis results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
