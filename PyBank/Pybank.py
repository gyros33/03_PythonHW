#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


budget_csv = os.path.join("Resources", "budget_data.csv")
total_months = 0
total_profits = 0
last_profit = 0
avg_change = 0
change = []
dates = []


# In[3]:


with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    
    # Read through each row of data after the header
    for row in csvreader:
        #create change and dates arrays
        change.append(int(row[1]) - last_profit)
        dates.append(row[0])
        #account for the last item
        last_profit = int(row[1])
        #calculate total months
        total_months += 1
        #calculate the total profits
        total_profits += int(row[1])
        
    
        


# In[4]:


#remove initial digit of 0
change.pop(0)
#calculate the average change
avg_change = round(sum(change) / (total_months - 1),2)


# In[5]:


#calculate the max change
max_profit = max(change)


# In[6]:


#caulculate the lowest change
min_profit = min(change)


# In[7]:


#find the dates for those changes (+1 because of the removed data)
max_date = dates[change.index(max_profit)+1]
min_date = dates[change.index(min_profit)+1]


# In[8]:


#print to terminal
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")


# In[9]:


#print to file
report_file = os.path.join("Resources", "report.txt")

with open(report_file, 'w', newline='') as file:

    file.write("Financial Analysis\n")
    file.write("---------------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profits}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {max_date} (${max_profit})\n")
    file.write(f"Greatest Decrease in Profits: {min_date} (${min_profit})\n")

