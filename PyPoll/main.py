# Import modules
import os
import csv

# Path for csv file
election_csv = os.path.join("resources","election_data.csv")

# Open the csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    # Print heading
    print(" ")
    print("                     Election Results")
    print("------------------------------------------------------")

    # Set variables to defaults
    total_votes = 0
    list_of_candidates = []
    dict1 = {}

    # Loop through csv file to calculate a complete list of candidates who 
    # received votes and the number of votes they won
    for row in csvreader:
        candidate_name = str(row[2])

        if candidate_name not in list_of_candidates:
            list_of_candidates.append(candidate_name)
            dict1[candidate_name] = 1
        else:
            dict1[candidate_name] += 1

        # Calculate the total number of votes cast
        total_votes += 1

    # Calculate the percentage of votes each candidate won, the winner
    # of the election based on popular vote, and print all results

    print(f"Total Votes: {total_votes}")
    print(f"------------------------------------------------------")
    
    # Loop through dictionary
    for k, v in dict1.items():

        # Calcualte the percentage of votes
        percent_votes = (v / total_votes) * 100

        # print the list of candidates, their percentage of votes won,
        # and their votes won
        print(f"{k}: {percent_votes:.3f}% ({v})")

    print(f"------------------------------------------------------") 

    # Calculate and print the winner of the election to the terminal
    winner = max(dict1, key = dict1.get)
    print(f"Winner: {winner}")
    print(f"------------------------------------------------------")   

# Specify output path
pypoll_analysis = os.path.join("Analysis", "PyPoll-Analysis.txt")

# Open the text file, initialize text writer, and write data to the text file
with open(pypoll_analysis, 'w') as txtfile:
    txtfile.write(f" \n")
    txtfile.write(f"                     Election Results\n")
    txtfile.write(f"------------------------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------------------------------------\n")
    
    for k, v in dict1.items():
        percent_votes = (v / total_votes) * 100
        txtfile.write(f"{k}: {percent_votes:.3f}% ({v})\n")

    txtfile.write(f"------------------------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"------------------------------------------------------\n") 