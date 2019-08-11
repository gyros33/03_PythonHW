#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


poll_csv = os.path.join("Resources", "election_data.csv")
total_votes = 0
candidate_votes = {}


# In[3]:


with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csvfile)
    
    # Read through each row of data after the header
    for row in csvreader:
        #Calculate total votes
        total_votes += 1
        
        #add unique candidates to a list
        if row[2] not in candidate_votes.keys():
            candidate_votes[row[2]] = 0
        
        #add a vote to the candidate
        candidate_votes[row[2]] += 1


# In[4]:


#calculate percentage of votes
vote_percent = [
    round((x / total_votes)*100,4)
    for x in list(candidate_votes.values())
         ]

#find the winner's index
winner_index = vote_percent.index(max(vote_percent))

#find the winner
candidates = list(candidate_votes.keys())
winner = candidates[winner_index]


# In[5]:


print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
for rows in range(len(candidates)):
    print(f"{candidates[rows]}: {vote_percent[rows]}% ({candidate_votes[candidates[rows]]})")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")


# In[6]:


#print to file
report_file = os.path.join("Resources", "report.txt")

with open(report_file, 'w', newline='') as file:

    file.write("Election Results\n")
    file.write("-----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-----------------------------\n")
               
    for rows in range(len(candidates)):
        file.write(f"{candidates[rows]}: {vote_percent[rows]}% ({candidate_votes[candidates[rows]]})\n")
    
    file.write("-----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-----------------------------\n")
    

