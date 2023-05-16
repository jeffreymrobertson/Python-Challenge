import os
import csv

output_path = os.path.join('Resources','election_data.csv')
input_path = os.path.join('Analysis', 'Election Data.txt')

votes = []
candidate = []
data = {"Votes": votes, "Candidates": candidate}

print(data)
with open(output_path, 'r') as csvfile:
    csvreader = (csv.reader(csvfile, delimiter=','))
    
    csvheader = next(csvreader)



    for row in csvreader:
        votes.append(row[0])
        candidate.append(row[2])
    unique_candidates = set(candidate)
    list_cand = (list(unique_candidates))
    print(list_cand)


    total_votes = len(votes)

    

   



with open(input_path, 'w') as textfile:
    tw = textfile.write

    tw('Election Results \n\n' + '-----------------------------\n\n')

    tw(f'Total Votes: {total_votes} \n\n' + '------------------------\n\n')

    tw(f'{list_cand[0]}\n\n')
    tw(f'{list_cand[1]}\n\n')
    tw(f'{list_cand[2]}\n\n')

    tw('Winner: \n\n' + '-------------------------------')