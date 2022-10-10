# Jeff Pinegar
# jeffpinegar1@gmail.com
# October 10, 2022

# PyBank Challenge

import os
import csv

# Identify the source file, and set path to the file
csvpath = os.path.join('.','Resources', 'budget_data.csv')

# open a csv file and read it in
# creating a dictionary using the header row as keys
with open(csvpath,'r' ) as f:                        
    data = csv.DictReader(f, delimiter=',')
    mylist=list(data)

# Calculate the number of month in the data set.
numMonths = len(mylist)

# Initialize the variables use for analysis
amt=0
maxGainAmt=0
maxGainMonth=None
maxLossAmt=0
maxLossMonth=None
totalPandL=0

# Look through the data one date at a time
for date in mylist:

    #calculate the net profit and loss
    amt=int(date['Profit/Losses'])
    totalPandL += amt

    # Determine maximum gain amount and month
    if amt > maxGainAmt:
        maxGainAmt = amt
        maxGainMonth=date['Date']

    # Determine greatest loss amount and month
    if amt < maxLossAmt:
        maxLossAmt = amt
        maxLossMonth=date['Date']
      
# build the output message one line at a time
mystring = '\n============================================' + '\n'
mystring = mystring + '>>>>>>>>>>    P & L Analysis    <<<<<<<<<<<<' + '\n'
mystring = mystring + '==================cd ..
==========================' + '\n'
mystring = mystring + 'Total number of month = '+ str(numMonths) + '\n'
mystring = mystring + 'Net profit and loss over '+ str(numMonths) + ' = '+ '${:,}'.format(totalPandL) + '\n'
mystring = mystring + 'The average change per month = '+ '${:,.2f}'.format(totalPandL/numMonths) + '\n'
mystring = mystring + 'The greatest gain occurred on ' + str(maxGainMonth) + ' for ' + '${:,.2f}'.format(maxGainAmt) + '\n'
mystring = mystring + 'The greatest loss occurred on ' + str(maxLossMonth) + ' for ' + '${:,.2f}'.format(maxLossAmt)

# Print the results to the screen
print (mystring)

# Open the file using "write" mode. Specify the variable to hold the contents
textfile = os.path.join('.','Analysis', 'Bank_Analysis.txt')
text_file = open(textfile, 'wt', encoding="utf-8")
text_file.write(mystring)
text_file.close()
