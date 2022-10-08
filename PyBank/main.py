import os
import csv

# Set path for file
csvpath = os.path.join('.','Resources', 'budget_data.csv')
print(csvpath)

# open a csv file and read it in
# creating a dictionary with the the header rows and keys
with open(csvpath,'r' ) as f:                        # This assume the input file is in the same location as the python file
    data = csv.DictReader(f, delimiter=',')
    mylist=list(data)

# Calculate the number of month in the data set.
numMonths = len(mylist)

amt=0
maxGainAmt=0
maxGainMonth=None
maxLossAmt=0
maxLossMonth=None
totalPandL=0
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
      


mystring = 'Total number of month = '+ str(numMonths) + '\n'
mystring = mystring + 'Net profit and loss over '+ str(numMonths) + ' = '+ '${:,}'.format(totalPandL) + '\n'
mystring = mystring + 'The average change per month = '+ '${:,.2f}'.format(totalPandL/numMonths) + '\n'
mystring = mystring + 'The greatest gain occured on ' + str(maxGainMonth) + ' for ' + '${:,.2f}'.format(maxGainAmt) + '\n'
mystring = mystring + 'The greatest loss occured on ' + str(maxLossMonth) + ' for ' + '${:,.2f}'.format(maxLossAmt)

print (mystring)

# Open the file using "write" mode. Specify the variable to hold the contents
text_file = open('Bank_Analysis.txt', 'wt', encoding="utf-8")
text_file.write(mystring)
text_file.close()
