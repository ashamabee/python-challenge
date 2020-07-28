import os
import csv
import operator
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
                #skips first row(header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
#The total number of votes cast
    VoteList = []
#A complete list of candidates who received votes
    Candidates = {}
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

    for row in csvreader:
        VoteList.append(row[0])
        CurrentC = row[2]
        if row[2] in Candidates:
            Candidates[row[2]] = Candidates[row[2]] + 1
            
        else:
            Candidates[row[2]] = 1

    TotalVotes = len(VoteList)
    Winner = max(Candidates.items(), key=operator.itemgetter(1))[0]
    Candidates
    
    KhanPercent = Candidates["Khan"]/TotalVotes *100
    CorreyPercent = Candidates["Correy"]/TotalVotes *100
    LiPercent = Candidates["Li"]/TotalVotes *100
    OTooleyPercent = Candidates["O'Tooley"]/TotalVotes *100
    
    print("Election Results")
    print("-----------------------------") 
    print(f'Total Votes: {TotalVotes}')
    print("-----------------------------")
    print(f'Khan: ({Candidates["Khan"]}) {KhanPercent:,.3f}%'.replace('$-', '-$'))
    print(f'Correy: ({Candidates["Correy"]}) {CorreyPercent:,.3f}%'.replace('$-', '-$'))
    print(f'Li: ({Candidates["Li"]}) {LiPercent:,.3f}%'.replace('$-', '-$'))
    print(f'OTooley: ({Candidates["Correy"]}) {OTooleyPercent:,.3f}%'.replace('$-', '-$'))
    print("-----------------------------") 
    print(f'Winner: {Winner}')
    print("-----------------------------") 

output_path = os.path.join("Analysis", "Analysis.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------------"])  
    csvwriter.writerow([f'Total Votes: {TotalVotes}'])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f'Khan: ({Candidates["Khan"]}) {KhanPercent:,.3f}%'.replace('$-', '-$')])
    csvwriter.writerow([f'Correy: ({Candidates["Correy"]}) {CorreyPercent:,.3f}%'.replace('$-', '-$')])
    csvwriter.writerow([f'Li: ({Candidates["Li"]}) {LiPercent:,.3f}%'.replace('$-', '-$')])
    csvwriter.writerow([f'OTooley: ({Candidates["Correy"]}) {OTooleyPercent:,.3f}%'.replace('$-', '-$')])
    csvwriter.writerow(["-----------------------------"]) 
    csvwriter.writerow([f'Winner: {Winner}'])
    csvwriter.writerow(["-----------------------------"]) 