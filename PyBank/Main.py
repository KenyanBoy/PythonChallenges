import os
import csv

budget_data = os.path.join("/Users/ernestbondi/Documents/GitHub/PythonChallenges/PyBank/Resources/budget_data.csv")

total_months = 0
Profit = []
Loss = []
average = 0
total_PL = 0
Date = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader,None)

    #Reading the header row
    #csv_header = next(csvreader)

    # Add to our total months-counter 
    row_one = next(csvreader)
    total_months += 1

    total_PL += float(row_one[1])
    number = float(row_one[1])

    for row in csvreader:

        #Add the months counter
        total_months += 1
#keep track of the dates
        Date.append(row[0])

        average = float(row[1])- number
        #Add change into the profuts
        Profit.append(average)
        #set the average row
        #average = float(row[1])

        

        #The TOTAL amount of the profit and Loss
        total_PL = total_PL + float(row[1])

    #Greatest Increase
    increase = max(Profit)
    increase_index = Profit.index(increase)
    increase_date = Date[increase_index]    

    #Lowest Increase - Same as Greatest formula
    decrease = min(Profit)
    decrease_index = Profit.index(decrease)
    decrease_date = Date[decrease_index]

    #Change in Prifit and Loss over the whole period
    average_change = average/total_months
   

#Output similar to Pypoll format

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_PL)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {increase_date} (${str(increase)})")
print(f"Greatest Decrease in Profits: {decrease_date} (${str(decrease)})")

#Exporing to output file
#Output similar to Pypoll format
output = open("/Users/ernestbondi/Documents/GitHub/PythonChallenges/PyBank/Analysis/output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_PL)}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {increase_date} (${str(increase)})")
line7 = str(f"Greatest Decrease in Profits: {decrease_date} (${str(decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))






