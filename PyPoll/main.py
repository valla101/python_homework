#import os & csv
import os
import csv

#create path to read csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Print Messages to match format in HW


#total number of votes
total_votes = 0

#declaring variable separating votes
vote_khan = 0
vote_correy = 0
vote_li = 0
vote_otooley = 0

with open(csvpath) as infile:

    # csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(infile, delimiter=',')

    # reads the header row first
    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1
        
        if row[2] == "O'Tooley":
            vote_otooley += 1
        elif row[2] == "Khan":
            vote_khan += 1
        elif row[2] == "Correy":
            vote_correy += 1
        elif row[2] == "Li":
            vote_li += 1

#calculating the vote percentage for each candidate
khan_percentage = (vote_khan/total_votes)*100
correy_percentage = (vote_correy/total_votes)*100
li_percentage = (vote_li/total_votes)*100
otooley_percentage = (vote_otooley/total_votes)*100





print("Election Results")
print("-----------------")
print(f'Total Votes: {total_votes} ')
print("-----------------")
print (f'Khan: {khan_percentage} ({vote_khan}) ')
print("-----------------")
print(f'Correy: {correy_percentage} ({vote_correy}) ')
print("-----------------")
print (f"Li Votes: {li_percentage} ({vote_li})")
print("-----------------")
print (f"O'Tooley Votes: {otooley_percentage} ({vote_otooley})")


print("Winner: Khan")