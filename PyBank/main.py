# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import budget data 
import os
import csv 
#working directory

csvpath=os.path.join('Resources','budget_data.csv')
file_to_output = os.path.join('Analysis', 'budget_analysis.txt')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    #print(f"Header: {csv_header}")               

#Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    #print(len(month))
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    #print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    #print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    #print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements
output = (
   f"\n     Financial Analysis \n"
   f"------------------------------\n"
   f"Total Months: {len(month)}\n"
   f"Total: ${total_revenue}\n"
   f"Average  Change: ${monthly_change:.2f}\n"
   f"Greatest Increase in Profits: {month_increase} (${profit_increase})\n"
   f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})\n")
print(output)

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)  

   file_to_output       