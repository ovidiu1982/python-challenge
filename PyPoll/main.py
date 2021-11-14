# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:19:18 2021

@author: ovidiu
"""

# --- import packages to read/write CSV files and create dynamic paths to the I/O files ---
import csv
import os

# -- define function to fix percentage format to 3 decimal points ---
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

# --- define relative path for the input and output files ---
inputfile=os.path.join('Resources','election_data.csv')
outputfile = os.path.join('Analysis', 'budget_analysis.txt')

# --- create empty lists and variables for storing values and calculations from data ---
UniqueCandidates = []
VoteCounts = []
VotePercent = []
TotalVotes = 0
WinnerCount = 0

# --- read the CSV file ---
with open(inputfile, 'r') as electiondata:
    reader = csv.reader(electiondata, delimiter=",")

    # --- store header rows into a Headers list ---
    Headers = next(reader)

    # --- for loop to go through each row in the CSV file and count the total number of votes ---

    for row in reader:
        TotalVotes += 1
    
        # --- get unique candidate names and individual vote counts and store in lists ---
        # if row[2] (candidate name) is not in the UniqueCandidates list, i.e. if it is the first instance of the name
        if row[2] not in UniqueCandidates:

            #append the name to UniqueCandidates and a value of 1 to VoteCounts list
            UniqueCandidates.append(row[2])
            VoteCounts.append(1)

        # if row[2] (candidate name) is in the UniqueCandidates list
        else:

            # get the index of the candidate from the UniqueCandidates list in order to increase the vote count by 1
            CandidateIndex = UniqueCandidates.index(row[2])
            VoteCounts[CandidateIndex] += 1
        

# --- calculate percentage of votes for each candidate ---
for i in range(len(VoteCounts)):
    VotePercent.append(VoteCounts[i] / TotalVotes)

# --- calculate the winner based on most votes ---
for i in range(len(VoteCounts)):

    # if the number of votes is greater than WinnerCount (initially zero)
    if VoteCounts[i] > WinnerCount:
        
        #update WinnerCount to the number of votes at index i
        WinnerCount = VoteCounts[i]

        #update Winner to the candidate name at index i
        Winner = UniqueCandidates[i]

#--- create a text file with the analysis output ---
with open(outputfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {TotalVotes}\n"
                   f"----------------------------\n"
                   )

    # --- for loop to iteratively write each candidate's info ---
    for i in range(len(UniqueCandidates)):
        textfile.write(f"{UniqueCandidates[i]}: {fixPercent(VotePercent[i])} ({VoteCounts[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {Winner}\n"
                   f"----------------------------\n"
                  )

# --- read the output file and print analysis to terminal ---
with open (outputfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)