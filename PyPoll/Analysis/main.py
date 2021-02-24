# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

row_count = 0
candidates = []
Khan_counts = 0
Correy_counts = 0
Li_counts = 0
Tooley_counts = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Establishes the first row as header
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # Determines the number of rows, which equals the number of votes
        row_count = row_count + 1
        # Appends the row[1] candidate value into the list candidates
        candidates.append(row[2])
        # Checks for the number of votes of each candidate, if it finds it, count increases
        if row[2] == "Khan":
            Khan_counts += 1
        elif row[2] == "Correy":
            Correy_counts += 1
        elif row[2] == "Li":
            Li_counts += 1
        elif row[2] == "O'Tooley":
            Tooley_counts += 1

    Khan_percent = round(Khan_counts/row_count * 100, 3)
    Correy_percent = round(Correy_counts/row_count * 100, 3)
    Li_percent = round(Li_counts/row_count * 100, 3)
    Tooley_percent = round(Tooley_counts/row_count * 100, 3)

    winner = max(set(candidates), key=candidates.count)

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(row_count))
    print("----------------------------")
    print(f'Khan: {Khan_percent}% ({Khan_counts})')
    print(f'Correy: {Correy_percent}% ({Correy_counts}')
    print(f'Li: {Li_percent}% ({Li_counts})')
    print(f"O'Tooley: {Tooley_percent}% ({Tooley_counts})")
    print("----------------------------")
    print("Winner: " + winner)
    print("----------------------------")

output_file = os.path.join("pypoll.txt")

with open(output_file, "w") as datafile:
    print("Election Results", file=datafile)
    print("----------------------------", file=datafile)
    print("Total Votes: " + str(row_count), file=datafile)
    print("----------------------------", file=datafile)
    print(f'Khan: {Khan_percent}% ({Khan_counts})', file=datafile)
    print(f'Correy: {Correy_percent}% ({Correy_counts}', file=datafile)
    print(f'Li: {Li_percent}% ({Li_counts})', file=datafile)
    print(f"O'Tooley: {Khan_percent}% ({Khan_counts})", file=datafile)
    print("----------------------------", file=datafile)
    print("Winner: " + winner, file=datafile)
    print("----------------------------", file=datafile)
