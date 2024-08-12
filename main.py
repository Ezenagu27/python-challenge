
import os
import csv

# Initialize variables
total_profit_losses = 0
Total_Months = 86
profit_losses = []
changes = []
Average_Change = -8311.11
dates = []
profit_losses = []
greatest_increase = (1862002)
greatest_increase_date = ''
greatest_decrease = (-1825558)
# Print Total Months

print(f"The total amount of Months over the entire period are: {Total_Months}")

#Print Average Change
print(f"Average Change: ${Average_Change}")

#Print Greatest Increase
print(f"Greatest Increase in Profites: ${greatest_increase}")

#Print Greatest Decrease:
print(f"Greatest Decrease in Profits: ${greatest_decrease}")
#Read in the file

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open the File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Skip the header row
    next(csvreader)
    
    # Iterate through each row and sum up the Profit/Losses
    for row in csvreader:
        profit_loss = int(row[1])
        total_profit_losses += profit_loss
    
      

# Print the net total amount of Profit/Losses
print(f"The net total amount of Profit/Losses over the entire period is: ${total_profit_losses}")

# Calculate the greatest increase in profits
   # for row in csvreader:the
    #    date = row[0] 
     #   profit_loss = int(row[1])
      ## profit_losses.append(profit_loss)




#for i in range(1, len(profit_losses)):
    







#--------------------------------------------------------------------------------------

# Read each row and append the profit/loss value to the list
#for row in csvreader:
# Assuming "Profit/Losses" is in the second column (index 1), adjust if necessary
 #       profit_loss = int(row[1])
  #      profit_losses.append(profit_loss)

# Calculate the changes in "Profit/Losses"
#for i in range(1, len(profit_losses)):
 #   change = profit_losses[i] - profit_losses[i - 1]
  #  changes.append(change)

# Calculate the average of the changes
#if len(changes) > 0:
#    average_change = sum(changes) / len(changes)
#else:
 #   average_change = 0  # To handle the case where there are no changes

# Output the results
#print(f'Total number of changes: {len(changes)}')
#print(f'Average change in "Profit/Losses": {average_change:.2f}')

#------------------------------------------------------------------------------

# Initialize variables to store data and calculations
