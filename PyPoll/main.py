#imports relevant libraries
import csv
import os

#creates path to relevant directory
csvpath=os.path.join('Resources','election_data.csv')

#opens and reads as a csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    ballot_header= next(csvreader)

    print('----------------------------------')

    #creates lists for csv row data of interest
    candidate = []
    ID=[]

    #appends data to new lists and counts number of votes
    for row in csvreader:
        candidate.append(row[2])
        ID.append(row[0])
    votecount = len(ID)

    #creates a dictionary for votes
    votes = {}
    
    #adds candidate data count to dictionary, retrievable by candidate name
    for name in candidate:
        if name not in votes:
            votes[name] = 1
        else:
            votes[name] = votes[name] + 1
    
    # calculates percentage vote for each candidate
    CCS_pc = votes["Charles Casper Stockham"]/votecount*100
    DDG_pc = votes["Diana DeGette"]/votecount*100
    RAD_pc = votes["Raymon Anthony Doane"]/votecount*100

    # returns a vote count for each candidate
    Charles_Casper_Stockham = votes.get('Charles Casper Stockham')
    Diana_DeGette = votes.get('Diana DeGette')
    Raymon_Anthony_Doane = votes.get('Raymon Anthony Doane')

    #returns the key for the value with the highest count
    winner = max(votes, key=votes.get)
    
output_file = os.path.join('Analysis','Election_results.txt')

with open(output_file, "w") as datafile:
    datafile.write('Election Results\n----------------------------------')
    datafile.write(f'\nTotal Votes: {votecount}')
    datafile.write('\n----------------------------------')
    datafile.write(f'\nCharles Casper Stockham: {round(CCS_pc, 3)}% ({Charles_Casper_Stockham})')
    datafile.write(f'\nDiana DeGette: {round(DDG_pc, 3)}% ({Diana_DeGette})')
    datafile.write(f'\nRaymon Anthony Doane: {round(RAD_pc, 3)}% ({Raymon_Anthony_Doane})')
    datafile.write('\n----------------------------------')
    datafile.write(f'\nWinner: {winner}')
    datafile.write('\n----------------------------------')
    
    #prints results summary
    print('Election Results')
    print('----------------------------------')
    print(f'Total Votes: {votecount}')
    print('----------------------------------')
    print(f'Charles Casper Stockham: {round(CCS_pc, 3)}% ({Charles_Casper_Stockham})')
    print(f'Diana DeGette: {round(DDG_pc, 3)}% ({Diana_DeGette})')
    print(f'Raymon Anthony Doane: {round(RAD_pc, 3)}% ({Raymon_Anthony_Doane})')
    print('----------------------------------')
    print(f'Winner: {winner}')
    print('----------------------------------')


