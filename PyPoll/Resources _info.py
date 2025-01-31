import os
import csv

#set up path from Python challenge, make sure you are in python challenge as a start
csvpath = os.path.join('Resources', 'election_data.csv')

#defining info
candidate_dict={} #dictionary of candidate
candidate_list = [] #List of Candidate
percentages = 0 #setting perectages as int
total_number_of_votes = 0 #setting total_number_of_votes as int
voter_counts = 0#setting voter_counts as int
greatest_vote = 0

#open path
with open(csvpath) as csvfile:
    #setup to remove , that divides info
    csvreader = csv.reader(csvfile, delimiter=',')   
    # Read the header row first and removes it from being pullled
    next (csvreader) 
    for line in csvreader:
        #adding up the vote count
        total_number_of_votes += 1
        #naming the line
        name = line[2]
        #grabing candidate's info     
        if name not in candidate_list:
            candidate_list.append(name)
            candidate_dict[name] = 0
        # else: 
        candidate_dict[name] += 1 
    #pring total number of votes
    print(f"Total Votes: {total_number_of_votes}")
    print("--------------------------------")
    #moving items into a list to print in rows
    #for candidate in candidate_list:
    #   candidate_dict[candidate]

    #exporting results to text file
    fileoutput = open("Analysis/analysis.txt", "w")
    fileoutput.write(f"Election Results\n")  
    fileoutput.write(f"-------------------------\n") 
    fileoutput.write(f"Total Votes: {total_number_of_votes}\n")
    fileoutput.write(f"-------------------------\n") 

    #making candidate list
    for candidate in candidate_list:
        vote_counts = candidate_dict.get(candidate)  

        #percentages of candidates votes
        percentages = ((vote_counts /total_number_of_votes) * 100)

        # printing candidate results
        print(f"{candidate}: {percentages:.3f}% {str(candidate_dict[candidate])}")

        # finds winner
        fileoutput.write(f"{candidate}: {percentages:.3f}% {str(candidate_dict[candidate])}\n")
    # pulls winners name from the dictionary list
    for key in candidate_dict.keys():
        if candidate_dict[key] > greatest_vote:
            winner = key
            greatest_vote = candidate_dict[key]
    print("--------------------------------") 
    print(f"Winner: {winner}")
    print("--------------------------------")  
       
# exports information into text file
fileoutput.write(f"-------------------------------\n")
fileoutput.write(f"Winner: {winner}\n")
fileoutput.write(f"-------------------------------\n")