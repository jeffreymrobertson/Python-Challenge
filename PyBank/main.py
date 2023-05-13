import os
import csv 

output_path = os.path.join('Resources','budget_data.csv')

#create variables to store lists
date = []
profit = []

with open(output_path, 'r') as csvfile:
    csvreader = (csv.reader(csvfile, delimiter=','))
    col_num = 1

    csvheader = next(csvreader)
    
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
    
    fProfit = [float(i) for i in profit]
    mydict = {date: fProfit for date, 
              fProfit in zip(date, fProfit)
    }

    print(sum(fProfit))
    print(len(date))


print(mydict)