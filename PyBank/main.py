#imports relevant libraries
import csv
import os

#creates path to relevant directory
csvpath = os.path.join('Resources','budget_data.csv')

#opens and reads as a csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    budget_header = next(csvreader)
    print('---------------------------------------------------------')
    
    #creates empty lists for csv row data of interest
    month=[]
    pnl=[]
    change=[]

    #appends data to new lists
    for row in csvreader:
        month.append(row[0])
        pnl.append(row[1])

    #converts to right data type    
    pnl=[int(i) for i in pnl]
    month=[str(i)for i in month]

    #creates total for 'profit and loss'    
    pnlsum = 0
    for i in pnl:
       pnlsum=pnlsum+i
    
    #calculates greatest, least and average change in 'profit and loss'
    for i in range(len(pnl)-1):
        change.append(pnl[i+1]-pnl[i])
    
    greatest_increase=max(change)
    greatest_decrease=min(change)

    increase_month=(month[change.index(greatest_increase)+1])
    decrease_month=(month[change.index(greatest_decrease)+1])
    
    change_sum = 0
    for i in change:
        change_sum = change_sum + i
    change_length = len(change)
    average_change = change_sum/change_length

#writes to separate .txt file called 'Financial_analysis.txt'
output_file = os.path.join('Financial_analysis.txt')

with open(output_file, "w") as datafile:
    datafile.write('Financial Analysis:\n---------------------------------------------------------')    
    datafile.write(f'\nTotal Months: {len(month)}')
    datafile.write(f'\nTotal: ${pnlsum}')
    datafile.write(f'\nAverage Change: ${round(average_change, 2)}')
    datafile.write(f'\nGreatest Increase in Profits: {increase_month} (${greatest_increase})')
    datafile.write(f'\nGreatest Decrease in Profits: {decrease_month} (${greatest_decrease})')

#prints financial summary
#--------------------------------------------------------------------------------------------------------
    print('Financial Analysis')
    print('---------------------------------------------------------')
    print(f'Total Months: {len(month)}')
    print(f'Total: ${pnlsum}')
    print(f'Average Change: ${round(average_change, 2)}')
    print(f'Greatest Increase in Profits: {increase_month} (${greatest_increase})') 
    print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')