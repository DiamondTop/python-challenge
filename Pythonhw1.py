import os
import csv


csvpath = os.path.join("..", "Resources", "budget_data.csv")

total_list = []
PandL = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headerline = next(csvreader) # to skip the header 

    # Loop through looking for the budget data
    for row in csvreader:
        
        total_list.append(row[0])
        #print (row)
        
        PandL.append(int(row[1]))
        

#PandL.sort()
#PandL.remove('Profit/Losses') if headerline is not used, this can remove the first index

#print(len(total_list)) # array
total_count = (len(total_list))
#print (total_count)
#print (PandL)
#print(PandL[1:total_count])

total_PL_int = 0
#Converting to integer and adding values
for x in range(total_count):
    #print(x)
    #print(PandL[x])
    total_PL_int = total_PL_int + PandL[x]
output_for_remaining=[PandL[x+1]-PandL[x] for x in range(len(PandL)-1)]
    #print (PandL_int)

Average = round(sum(output_for_remaining)/(total_count -1), 2) #average values of the index
Max_increase = max(output_for_remaining) # max value
Min_increase = min(output_for_remaining) # Min value


#to find/display the index for MAX profits
index = output_for_remaining.index(Max_increase)
#print(output_for_remaining[23])
#print(Max_increase)

#print('The index of i:', index + 3)
#print('The date is: '+ total_list[index+1])
date_Max = total_list[index+1]        
#print (date_Max)
#to find/display the index for MIN profits
index = output_for_remaining.index(Min_increase)
#print(output_for_remaining[23])
#print(Min_increase)

#print('The index of i:', index + 3)
#print('The date is: '+ total_list[index+1])
date_Min = total_list[index+1]      
#print (date_Min) 


#print(total_PL_int)


#displaying the results

print("Financial Analyst Report")
print("-----------------------------------")
print("Total Months: " + str(total_count))
print("Total: $" + str(total_PL_int))
print("Average Change: $"+ str(Average))
print("Greatest increase in Profits: " + date_Max + " ($" + str(Max_increase) + ")")
print("Greatest Decrease in Profits: "+ date_Min + " ($" + str(Min_increase)+ ")" )
print (csvpath + "Test")
# Returns the length of the List


#opens and write to text file	
f= open("pythondata.txt","w+")

    #f.write("This is line %d\r\n" % (i+1))
f.write("Financial Analyst Report"+ "\n")
f.write("-----------------------------------" + "\n")
f.write("Total Months: " + str(total_count) + "\n")
f.write("Total: $" + str(total_PL_int) + "\n")
f.write("Average Change: $"+ str(Average) + "\n")
f.write("Greatest increase in Profits: "+ date_Max + " ($" + str(Max_increase) + ")" + "\n")
f.write("Greatest Decrease in Profits: "+ date_Min + " ($" + str(Min_increase) + ")" + "\n")
f.write(csvpath + "Test" + "\n")     

	
f.close() 


#print(total_list(1))

#print to excel
#
   
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


# In addition, your final script should both print the analysis to the terminal and 
# export a text file with the results.

