import os
import csv

output_path = os.path.join('Resources','budget_data.csv')
#output_path = "Resources/budget_data.csv"
# print (output_path)
with open(output_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

