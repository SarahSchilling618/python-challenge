import os
import csv

polling_csv = os.path.join("..", "Resources", "election_data.csv")

with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    data = list(csvreader)

totalvotes = len(data) # Calculate the total number of votes cast

votes_per_candidate = {} # Stores votes for each candiate

for row in data:
    candidate = row[2] # Accounts for each candidate in the data
    if candidate in votes_per_candidate:
        votes_per_candidate[candidate] += 1
    else:
        votes_per_candidate[candidate] = 1

# Calculate the percentage of votes each candidate won
percentage_per_candidate = {}
for candidate, votes in votes_per_candidate.items():
    percentage = (votes / totalvotes) * 100
    percentage_per_candidate[candidate] = round(percentage, 2)

winner = max(votes_per_candidate, key=votes_per_candidate.get) # Calculates who got the most votes

# Prints results to terminal
print("Election Results")
print("--------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------")
for candidate, votes in votes_per_candidate.items():
    percentage = percentage_per_candidate[candidate]
    print(f"{candidate}: {percentage}% ({votes})")
print("--------------------")
print(f"Winner: {winner}")
print("--------------------")

# Prints results as a .txt file
with open('election_data.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("--------------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("--------------------\n")
    for candidate, votes in votes_per_candidate.items():
        percentage = percentage_per_candidate[candidate]
        file.write(f"{candidate}: {percentage}% ({votes})\n")
    file.write("--------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------\n")