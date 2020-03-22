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

print (f'Khan: {str(round(khan_percentage,4))}% ({vote_khan}) ')

print(f'Correy: {str(round(correy_percentage,4))}% ({vote_correy}) ')

print (f"Li Votes: {str(round(li_percentage,4))}% ({vote_li})")

print (f"O'Tooley Votes: {str(round(otooley_percentage,4))}% ({vote_otooley})")

print("-----------------")
print("Winner: Khan")

#locates directory for new text file
output_path = os.path.join("py_poll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
new_text_file = open(output_path, 'w')
new_text_file.write("Election Results\n")
new_text_file.write("-----------------\n")
new_text_file.write(f'Total Votes: {total_votes}\n')
new_text_file.write(f'Khan: {str(round(khan_percentage,4))}% ({vote_khan})\n ')
new_text_file.write(f'Correy: {str(round(correy_percentage,4))}% ({vote_correy})\n ')
new_text_file.write(f"Li Votes: {str(round(li_percentage,4))}% ({vote_li})\n")
new_text_file.write(f"O'Tooley Votes: {str(round(otooley_percentage,4))}% ({vote_otooley})\n")
new_text_file.write("-----------------\n")
new_text_file.write("Winner: Khan\n")
new_text_file.close()