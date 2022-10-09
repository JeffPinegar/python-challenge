import os
import csv

# Set path for file source file
csvpath = os.path.join('.','Resources', 'election_data.csv')

# open a csv file and read it in
# creating a dictionary with the the header rows and keys
with open(csvpath,'r' ) as f:                        
    mydata = csv.DictReader(f, delimiter=',')
    mylist=list(mydata)


# The total number of votes cast
numVotes = len(mylist)

# A complete list of candidates who received votes
# uses the property of set - only unique values so duplicates are eleminated
thecandidates=set()  #this is needed of python will create a dictionary
for vote in mylist:
    thecandidates.add(vote['Candidate'])


# The total number of votes each candidate won
# create a dictionary from the keys of 'thecanidates' setting the initial value of each to 0
voteTally= dict.fromkeys(thecandidates,0)
for vote in mylist:
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
    resultsMessage.append(f'{name} recieved {formattedVoteTally} votes for {formattedPer} of the vote. \n')
resultsMessage.append(f'--------------------------------------------------------------------------' + '\n')
resultsMessage.append(f'The winner is: {theWinnerIs} \n')


# Print results to the screen
print(*resultsMessage)


#Write the results to a file
# Open the file using "write" mode. Specify the variable to hold the contents
textpath = os.path.join('.','Analysis', 'Election_Results.txt')
text_file = open(textpath, 'wt', encoding="utf-8")
lineNum=0
for line in resultsMessage:
    text_file.write(resultsMessage[lineNum])
    lineNum +=1
text_file.close()


