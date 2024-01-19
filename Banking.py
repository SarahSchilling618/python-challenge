import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

data = [] # List to store data
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skips the first row
    for row in csvreader:
        data.append(row)

months = len(data) # Since we know each line of data is its own date, we use this to count the number of lines
total = sum(int(row[1]) for row in data) # Sums up all the data in row 2, which is the amount gained/lost
changes = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, len(data))] # Finds the difference between adjacent dates
averagechange = sum(changes) / len(changes) # Calculates the average change of every month

# Calculate the month that had the highest increase
max_increase = max(changes)
max_increase_index = changes.index(max_increase)
max_increase_date = data[max_increase_index + 1][0]

# Calculate the month that had the highest decrease
max_decrease = min(changes)
max_decrease_index = changes.index(max_decrease)
max_decrease_date = data[max_decrease_index + 1][0]


# Print all information to the terminal
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${averagechange:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Print all information as a text file
with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${averagechange:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")