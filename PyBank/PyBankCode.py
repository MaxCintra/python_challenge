import os
import csv

createfilepath =  os.path.join('analysis', 'PyBankAnalysis.txt')
budget_data_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv, newline='') as csv_file:

	reader = csv.reader(csv_file)
	next(reader)
	profit =[]
	month_count = []
	profit_change = []

	#goes through the csv pulling and adding the calues into the lists
	for row in reader:
		profit.append(int(row[1]))
		month_count.append(row[0])
	for i in range(len(profit)-1):
		profit_change.append(profit[i+1]-profit[i])

#finds largest adn smallest change
increase = max(profit_change)
decrease = min(profit_change)

#grabs location where date data is located in referance to the max and min values
month_max = profit_change.index(max(profit_change))+1
month_min = profit_change.index(min(profit_change))+1

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month_count[month_max]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_min]} (${(str(decrease))})")

with open(createfilepath, "w") as f:
	f.write("Financial Analysis\n")
	f.write("------------------------\n")
	f.write(f"Total Months: {len(month_count)}"+"\n")
	f.write(f"Total: ${sum(profit)}"+"\n")
	f.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}"+"\n")
	f.write(f"Greatest Increase in Profits: {month_count[month_max]} (${(str(increase))})"+"\n")
	f.write(f"Greatest Decrease in Profits: {month_count[month_min]} (${(str(decrease))})"+"\n")