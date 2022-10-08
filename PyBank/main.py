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
      


# Printing the outputs
print(f'Total number of month = {numMonths}')
print(f'Net profit and loss over {numMonths} = ','${:,}'.format(totalPandL))
print(f'The average change per month = ', '${:,.2f}'.format(totalPandL/numMonths))
print(f'The greatest gain occured on {maxGainMonth} for', '${:,.2f}'.format(maxGainAmt))
print(f'The greatest loss occured on {maxLossMonth} for', '${:,.2f}'.format(maxLossAmt))