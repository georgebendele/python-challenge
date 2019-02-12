# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None) # skip the header

#The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

    counter = 0
    candidates = []
    votes = []
    candict = {"candidate":[], "votePercent": [], "voteCount": []}
    
# The total number of votes cast
    for rows in reader:
        counter = counter + 1
        
# A complete list of candidates who received votes
        candy = rows[2]
        if candidates.count(candy) == 0:
            candidates.append(candy)
            votes.append(0)


# The total number of votes each candidate won

        if candy == candidates[0]:
            votes[0] = float(votes[0]) + 1
        elif candy == candidates[1]:
            votes[1] = float(votes[1]) + 1
        elif candy == candidates[2]:
            votes[2] = float(votes[2]) + 1
        elif candy == candidates[3]:
            votes[3] = float(votes[3]) + 1

# The percentage of votes each candidate won

for vote in votes:
    vote = round(vote)
    candict["voteCount"].append(vote)
    percent = (vote/counter)*100
    percent = round(percent, 2)
    candict["votePercent"].append(percent)


# Create dictionary to hold candidate info
for name in candidates:
    candict["candidate"].append(name)

                    
# The winner of the election based on popular vote.

for index, count in enumerate(votes):
    if count == max(votes):
        winner = candidates[index]


print(f"\nElection Results")
print(f"\n------------------------------")
print(f"\nTotal Votes: {counter}")
print(f"------------------------------")

print(f"{candict['candidate'][0]}: {candict['votePercent'][0]}% ({candict['voteCount'][0]})")
print(f"{candict['candidate'][1]}: {candict['votePercent'][1]}% ({candict['voteCount'][1]})")
print(f"{candict['candidate'][2]}: {candict['votePercent'][2]}% ({candict['voteCount'][2]})")
print(f"{candict['candidate'][3]}: {candict['votePercent'][3]}% ({candict['voteCount'][3]})")

print(f"\n------------------------------")
print(f"Winner: {winner}")
print(f"------------------------------")

filename = 'results.txt'
with open(filename, 'w') as file_object:
    file_object.write(
                      f"\nElection Results\n"
                      f"\n------------------------------\n"
                      f"\nTotal Votes: {counter}\n"
                      f"------------------------------\n"
                      
                      f"{candict['candidate'][0]}: {candict['votePercent'][0]}% ({candict['voteCount'][0]})\n"
                      f"{candict['candidate'][1]}: {candict['votePercent'][1]}% ({candict['voteCount'][1]})\n"
                      f"{candict['candidate'][2]}: {candict['votePercent'][2]}% ({candict['voteCount'][2]})\n"
                      f"{candict['candidate'][3]}: {candict['votePercent'][3]}% ({candict['voteCount'][3]})\n"
                      
                      f"\n------------------------------\n"
                      f"Winner: {winner}\n"
                      f"------------------------------"
                      )
