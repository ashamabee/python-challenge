import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
                #skips first row(header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
#The total number of months included in the dataset
    MonthList = []
#The net total amount of "Profit/Losses" over the entire period
    ProfitLosses = []
    PreviousRow = 0
    FirstRow = next(csvreader)
    CurrentRow = int(FirstRow[1])
    MonthList.append(FirstRow[0])
    ProfitLosses.append(int(FirstRow[1]))
#The average of the changes in "Profit/Losses" over the entire period    
    TotalChange = 0
    TotalRows = 0
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period   
    GreatestIncrease = int(FirstRow[1])
    GreatestDecrease = int(FirstRow[1])
    for row in csvreader:
        #print(row)
        MonthList.append(row[0])
        ProfitLosses.append(int(row[1]))
        TotalChange = TotalChange + int(row[1]) - (CurrentRow)
        CurrentRow = int(row[1])

        if int(row[1]) > GreatestIncrease:
            GreatestIncrease = int(row[1])
            BestMonth = row[0]
        if int(row[1]) < GreatestDecrease:
            GreatestDecrease = int(row[1])
            WorstMonth = row[0]

    MonthCount = len(MonthList)
    NetTotal = sum(ProfitLosses)
    AverageChange = TotalChange/(MonthCount -1)


    print("Financial Analysis")
    print("-----------------------------")  
    print(f'Total Months: {MonthCount}')
    print(f'Total: ${NetTotal:,.0f}'.replace('$-', '-$'))
    #print(ChangesList)
    print(f'Average Change: ${AverageChange:,.2f}'.replace('$-', '-$'))
    print(f'Greatest Increase in Profits: {BestMonth} (${GreatestIncrease:,.0f})'.replace('$-', '-$'))
    print(f'Greatest Decrease in Profits: {WorstMonth} (${GreatestDecrease:,.0f})'.replace('$-', '-$'))

output_path = os.path.join("Analysis", "Analysis.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------------"])  
    csvwriter.writerow([f'Total Months: {MonthCount}'])
    csvwriter.writerow([f'Total: ${NetTotal:,.0f}'.replace('$-', '-$')])
    csvwriter.writerow([f'Average Change: ${AverageChange:,.2f}'.replace('$-', '-$')])
    csvwriter.writerow([f'Greatest Increase in Profits: {BestMonth} (${GreatestIncrease:,.0f})'.replace('$-', '-$')])
    csvwriter.writerow([f'Greatest Decrease in Profits: {WorstMonth} (${GreatestDecrease:,.0f})'.replace('$-', '-$')])
