import os
import csv
import numpy

output_path = os.path.join('Resources','budget_data.csv')
input_path = os.path.join('Analysis', 'Financial Analysis.txt')

#create variables to store lists
date = []
profit = []

with open(output_path, 'r') as csvfile:
    csvreader = (csv.reader(csvfile, delimiter=','))
    
    csvheader = next(csvreader)
    
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
    
    fProfit = [int(i) for i in profit]
 
    #find the different between two values in fProfit
    diff = numpy.diff(fProfit)
    #find the average change
    avChange = numpy.average(diff).round(2)
    #find the min and max
    maxchange = max(numpy.diff(fProfit))
    minchange = min(diff)
    #find the date index
    for index, s in enumerate(diff):
        if s == maxchange:
            maxdate_index = index + 1
        elif s == minchange :
            mindate_index = index + 1


    print('Financial Analyis\n\n'+'---------------------------------\n\n')
    print(f'Total Months: {len(date)}\n\n')
    print(f'Total: ${sum(fProfit)}\n\n')
    print(f'Average Change = {avChange}\n\n')
    print(f'Greatest Increase in Profits: {date[maxdate_index]} ${maxchange}\n\n')
    print(f'Greatest Decrease in Profits: {date[mindate_index]} ${minchange}')    
        

#print all the values into a textfile
with open(input_path,'w') as textfile:
    thisline = textfile.write
    thisline('Financial Analyis\n\n'+'---------------------------------\n\n')
    thisline(f'Total Months: {len(date)}\n\n')
    thisline(f'Total: ${sum(fProfit)}\n\n')
    thisline(f'Average Change = {avChange}\n\n')
    thisline(f'Greatest Increase in Profits: {date[maxdate_index]} ${maxchange}\n\n')
    thisline(f'Greatest Decrease in Profits: {date[mindate_index]} ${minchange}')