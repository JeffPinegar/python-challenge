# Jeff Pinegar
# jeffpinegar1@gmail.com
# October 10, 2022

# PyBank Challenge

import os
import csv

# Identify the source file, and set path to the file
csvpath = os.path.join('.','Resources', 'election_data.csv')

# open a csv file and read it in
# creating a dictionary using the header row as keys
with open(csvpath,'r' ) as f:                        
    mydata = csv.DictReader(f, delimiter=',')
    mylist=list(mydata)


# The total number of votes cast is equal to the length of the list
numVotes = len(mylist)

# Create a complete list of candidates who received votes. 
# Sets can only contain unique elements. So adding every vote to a set will eliminate the duplicate names.
thecandidates=set()  # The empty set is create first.  This technique is used so that python does not create a dictionary
for vote in mylist:
    thecandidates.add(vote['Candidate'])


# Calculate the total number of votes each candidate received.
# Create a dictionary using the 'thecanidates' as keys and setting the initial value of each to 0
voteTally= dict.fromkeys(thecandidates,0)
for vote in mylist:                         #Accumulate the votes for each canidate
    name = vote['Candidate']
    voteTally[name] += 1


# Calculate the percentage of votes each candidate won and winner
# Use the same for loop to determin the winner
theWinnerIs = ''
winnerVotes = 0
voteAverage=dict.fromkeys(thecandidates,0)
for name in voteTally:
    voteAverage[name] = voteTally[name]/numVotes        # calculate the % for each canidate
    if voteTally[name] > winnerVotes:                   # if curren name has more votes than the last name save the name
        winnerVotes = voteTally[name]                   # set the new high mark for votes
        theWinnerIs = name                              # save the name of the person that set the high mark


# Build the results message as list of strings
resultsMessage=list()
resultsMessage.append(f'\n ===================================' + '\n')
resultsMessage.append(f'>>>>>    Election Results   <<<<<<< \n')
resultsMessage.append(f'===================================' + '\n')
formattednumVote = '{:,}'.format(numVotes)
resultsMessage.append(f'The vote total is: {formattednumVote}' '\n')
resultsMessage.append(f'--------------------------------------------------------------------------' + '\n')
for name in thecandidates:
    formattedPer = '{:,.2f}%'.format(voteAverage[name]*100)
    formattedVoteTally = '{:,}'.format(voteTally[name])
    resultsMessage.append(f'{name} received {formattedVoteTally} votes for {formattedPer} of the vote. \n')
resultsMessage.append(f'--------------------------------------------------------------------------' + '\n')
resultsMessage.append(f'The winner is: {theWinnerIs} \n')


# Print results to the screen
print(*resultsMessage)


#Write the results to a file
# Open the file using "write" mode. Specify the filename for the results
textpath = os.path.join('.','Analysis', 'Election_Results.txt')
text_file = open(textpath, 'wt', encoding="utf-8")
lineNum=0
for line in resultsMessage:
    text_file.write(resultsMessage[lineNum])
    lineNum +=1
text_file.close()


