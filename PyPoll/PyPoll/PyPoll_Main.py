import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csv_reader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

   
   #print title
    print(f'Election Results')
    print(f'--------------------------------------')

    # Read each row of data after the header and get row count - total votes
    row_count =sum(1 for row in csvreader)
    print(f'Total Votes: {row_count}')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
     
   #define variables
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    otoole_votes = 0
    votes = 0

#if statement, find out how many votes for each canidate
    for row in csvreader:
        votes = str(row[2])
        if votes == "Khan":
            Khan_votes = Khan_votes + 1
        elif votes == "Li":
            Li_votes = Li_votes + 1
        elif votes == "Correy":
            Correy_votes = Correy_votes + 1
        
    otoole_votes = (row_count-(Khan_votes +Li_votes+Correy_votes))
    
    #check vote output
    #print(Khan_votes)
    #print(Li_votes)
    #print(Correy_votes)
    #print(otoole_votes)

    
    #find percentage of total votes for each canidate
    khan_percent = (Khan_votes/row_count)*100
    li_percent = (Li_votes/row_count)*100
    correy_percent = (Correy_votes/row_count)*100
    otoole_percent = (otoole_votes/row_count)*100

   
   #round percentage found above to 3 decimal places
    khan_percent = round(khan_percent,3)
    li_percent = round(li_percent,3)
    correy_percent = round(correy_percent,3)
    otoole_percent = round(otoole_percent,3)

    

    #output data - candidate, percentage and votes

    print(f'--------------------------------------')
    print(f'Kahn: {khan_percent}% ({Khan_votes})')
    print(f'Li: {li_percent}% ({Li_votes})')
    print(f'Correy: {correy_percent}% ({Correy_votes})')
    print(f"O'Tooley: {otoole_percent}% ({otoole_votes})")
    print(f'--------------------------------------')


 #The winner of the election based on popular vote.

    if khan_percent > li_percent and khan_percent > correy_percent and khan_percent > otoole_percent:
        print(f"Khan Wins!")

    if li_percent > khan_percent and li_percent > correy_percent and li_percent > otoole_percent:
        print(f"Li Wins")

    if correy_percent > li_percent and correy_percent > khan_percent and correy_percent > otoole_percent:
        print(f"Correy Wins!")

    if otoole_percent > li_percent and otoole_percent > correy_percent and otoole_percent > khan_percent:
        print(f"O'Tooley Wins!")