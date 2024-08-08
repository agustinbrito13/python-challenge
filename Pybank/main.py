

import os
import csv


budget_data = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
   

 #Initialize variables for total months, total profit, and max and min profit,
 #999999 in case theres not any negative decrease
    total_months = 0
    total_profit_losses = 0
    changes = []
    previouscell = 0
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 99999999
    greatest_decrease_date = ""

    
    
    # Read through each row of data after the header
    for row in csv_reader:
     
     total_months = total_months + 1
     
     #calculate total profit loss 
     total_profit_losses = total_profit_losses + int(row[1])
     if total_months > 1:

          
         total_change = int(row[1]) - previouscell
        #mondays presentation 
         changes.append(total_change)
 # Check for greatest increase
         if total_change > greatest_increase:
           greatest_increase = total_change
           greatest_increase_date = row[0]

   #check for decrease 

         if total_change < greatest_decrease:
            greatest_decrease = total_change
            greatest_decrease_date = row[0]        


     previouscell = int(row[1])

          
   


 
  #chat GPT  
average_change = sum(changes)/len(changes)










# Print the results
print("Financial Analysis")
print("--------------------------")
print(f"total_months :{total_months}")
print(f"Total:${total_profit_losses}")
print("Average Change""$" + str(round(average_change,2)))
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in profits:{greatest_decrease_date} ($){greatest_decrease})")



        
    
