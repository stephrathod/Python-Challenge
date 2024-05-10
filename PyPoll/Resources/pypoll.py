import os
import csv
#open file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    Vote_Total = 0
    Candidates = {}
#Count Votes for candidates
    for row in csvreader:
        candidate_name = row[2]
        Vote_Total += 1
        Candidates[candidate_name] = Candidates.get(candidate_name, 0) + 1

# Vote per Candidate Percent
results = []
for candidate_name, candidate_votes in Candidates.items():
    candidate_percent = (candidate_votes / Vote_Total) * 100
    results.append((candidate_name, candidate_percent, candidate_votes))

# Find winner
winner = max(results, key=lambda x: x[2])

# Print
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Vote_Total}")
print("-------------------------")
for candidate_name, candidate_percent, candidate_votes in results:
    print(f"{candidate_name}: {candidate_percent:.3f}% ({candidate_votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")


#Print to new txt file
filepath = os.path.join('PyPoll', 'Resources', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {Vote_Total}", file=text_file)
    print(f"-------------------------", file=text_file)

    for candidate_name, candidate_percent, candidate_votes in results:
        print(f"{candidate_name}: {candidate_percent:.3f}% ({candidate_votes})", file=text_file)

    print(f"-------------------------", file=text_file)
    print(f"Winner: {winner[0]}", file=text_file)
    print(f"-------------------------", file=text_file)