import os
import csv

output_path = os.path.join('Resources','election_data.csv')
input_path = os.path.join('Analysis', 'Financial Analysis.txt')

votes = []
county = []
candidate = []


with open(output_path, 'r') as csvfile:
    csvreader = (csv.reader(csvfile, delimiter=','))
    for  row in csvreader:
        votes.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    print (len(candidate))