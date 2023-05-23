import os
import csv


output_path = os.path.join('Resources','election_data.csv')
input_path = os.path.join('Analysis', 'Election Data.txt')

#create variables to store data
votes = []
candidate = []

#read the csv file
with open(output_path, 'r') as csvfile:
    csvreader = (csv.reader(csvfile, delimiter=','))
    
    csvheader = next(csvreader)


    # get the candidates names
    for row in csvreader:
        votes.append(row[0])
        candidate.append(row[2])
    unique_candidates = set(candidate)
        
    list_cand = (list(unique_candidates))
    #get the total number of votes and save them
    total_votes = len(votes)

    f_tv = float(total_votes)
    # create a counter for to count the votes
    cana= 0
    canb= 0
    canc= 0
    #count the votes for each candidate
    for voters in candidate:
        if voters == list_cand[0]:
            cana += 1
        elif voters == list_cand[1]:
            canb += 1
        elif voters == list_cand[2]:
            canc += 1

    # get the percentage of votes
    pera = float((cana / f_tv)*100)
    perb = float((canb / f_tv)*100)
    perc = float((canc / f_tv)*100)

    percentage = [pera, perb, perc]
    
    #find the winner
    for winner in percentage:
        if pera > perb and pera > perc:
            winner = str(list_cand[0])
        elif perb > pera and perb > perc:
            winner = str(list_cand[1])
        else:
            winner = str(list_cand[2])

    print(f'Total Votes: {total_votes} \n\n' + '------------------------\n\n')
    
    #Print the results in the terminal
    print(f'{list_cand[0]}: {percentage[0]}% {cana}\n\n')
    print(f'{list_cand[1]}: {percentage[1]}% {canb}\n\n')
    print(f'{list_cand[2]}: {percentage[2]}% {canc}\n\n')
    print(f'Winner: {winner} \n\n' + '-------------------------------')

#print the results in the textfile
with open(input_path, 'w') as textfile:
    tw = textfile.write

    tw('Election Results \n\n' + '-----------------------------\n\n')

    tw(f'Total Votes: {total_votes} \n\n' + '------------------------\n\n')

    tw(f'{list_cand[0]}: {percentage[0]}% {cana}\n\n')
    tw(f'{list_cand[1]}: {percentage[1]}% {canb}\n\n')
    tw(f'{list_cand[2]}: {percentage[2]}% {canc}\n\n')
    tw(f'Winner: {winner} \n\n' + '-------------------------------')