import os
import csv

# Path to the CSV file
election_data = os.path.join("Resources", "election_data.csv")

# Initialize total votes variable and dictionary for candidate votes
total_votes = 0
candidates_votes = {}

# Open and read the CSV file
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file)

    # Read the header row first
    csv_header = next(csv_reader)

    # Iterate through each row
    for row in csv_reader:
        # Increment the total votes by 1 for each row
        total_votes += 1

        # Get the candidate name from the current row
        candidate_name = row[2]

        # Check if the candidate is already in the dictionary
        if candidate_name in candidates_votes:
            # If candidate exists, increment their vote count
            candidates_votes[candidate_name] += 1
        else:
            # If candidate is new, add them to the dictionary with 1 vote
            candidates_votes[candidate_name] = 1

# Find the winner
winner = max(candidates_votes, key=candidates_votes.get)
winner_votes = candidates_votes[winner]

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} votes ({percentage:.2f}%)")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
