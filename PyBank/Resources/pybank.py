import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    Month = []
    Profit_Loss=[]
    Profit_change = []

    for row in csvreader:
        Month.append(row[0])
        Profit_Loss.append(int(row[1]))
        
#Find total months and net total profit/loss
Month_Total = len(Month)
Net_Profit= sum(Profit_Loss)

#Find Average Change
for i in range (1, Month_Total):
     change= Profit_Loss[i] - Profit_Loss[i-1]
     Profit_change.append(change)

Average_Change = sum(Profit_change)/len(Profit_change)

#Greatest Increase
Greatest_Increase= max(Profit_change)
Greatest_Increase_Month = Month[Profit_change.index(Greatest_Increase)+1]

#Greastest Decrease
Greatest_Decrease= min(Profit_change)
Greatest_Decrease_Month = Month[Profit_change.index(Greatest_Decrease)+1]

#Print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Month_Total}")
print(f"Total: ${Net_Profit}")
print(f"Average Change: ${Average_Change:.2f}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} (${Greatest_Decrease})")

#Print to new txt file
filepath = os.path.join('PyBank', 'Resources','PyBank_Results.txt')
with open(filepath, "w") as text_file:
    print(f"Financial Analysis", file=text_file)
    print(f"----------------------------", file=text_file)
    print(f"Total Months: {Month_Total}", file=text_file)
    print(f"Total: ${Net_Profit}", file=text_file)
    print(f"Average Change: ${Average_Change:.2f}", file=text_file)
    print(f"Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase})", file=text_file)
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} (${Greatest_Decrease})", file=text_file)