# 03 Python - PyBank & PyPoll

## Background

This repository contains two python projects: PyBank and PyPoll. Inside of each folder, there is:
1. An "Analysis" folder that contains the main script filed called main.py that returns a print of the analysis to the terminal and export a text file with the results, which are also in this folder.
2. A "Resources" folder that contains the CSV files used.

## Skills

 import modules | read/write files | variables | lists | dictionaries | iterations | debugging | big data

## PyBank

The financial dataset is called budget_data.csv and is composed of two columns: Date and Profit/Losses. The goal is to create a Python script for analyzing the financial records of a company, that calculates each of the following:

1. The total number of months included in the dataset.
2. The net total amount of "Profit/Losses" over the entire period.
3. The average of the changes in "Profit/Losses" over the entire period.
4. The greatest increase in profits (date and amount) over the entire period.
5. The greatest decrease in losses (date and amount) over the entire period.

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)

## PyPoll

The poll dataset is called election_data.csv and is composed of three columns: Voter ID, County, and Candidate. The goal is to create a Python script that analyzes the votes and calculates each of the following:

1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate won.
5. The winner of the election based on popular vote.

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------


