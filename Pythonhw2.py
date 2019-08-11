import os
import csv

total_list = []
PandL = []

csvpath = os.path.join("..", "Resources", "election_data.csv")


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headerline = next(csvreader) # to skip the header 

    # Loop through looking for the budget data
    for row in csvreader:
        
        total_list.append(row[0])
        #print (row)
        
        PandL.append(str(row[2]))
        
#total_count as long

total_count = (len(total_list))
#print (total_count)

#print (PandL[0])


counter2 = 0
counter1 = 0
counter3 = 0
counter4 = 0
# test to see how many Kahn in the total list

name1 = "Khan"
name2 = "Correy"
name3 = "Li"
name4 = "O'Tooley"

for x in range(total_count):
    
    #print ('Hello')
    if name1 in PandL[x]:
        #print(name1 + " is in the first group")
        counter1 = counter1 + 1
        #print (counter1)
    elif name2 in PandL[x]:
#        print(name2 + " is in the first group")
        counter2 = counter2 + 1
#        print (counter2)
    elif name3 in PandL[x]:
        #print(name3 + " is in the first group")
        counter3 = counter3 + 1
        #print (counter3)
    else:
        #print(name4 + " is in the first group")
        counter4 = counter4 + 1
        #print (counter4)


#print (x)
#print (counter1)
#print (counter2)
#print (counter3)
#print (counter4)        

# to check who is the winner and return it as a string using index of array to match
winner_vote = [counter1, counter2, counter3, counter4]
no_winnervote = len(winner_vote)

Max_vote = max(winner_vote) # max value

#print (Max_vote)

index = winner_vote.index(Max_vote)

if index == 0:
        #print (name1 + " is the winner")
        winner = name1
elif index == 1:
        #print (name2 + " is the winner")
        winner = name2
elif index == 2:
        #print (name3 + " is the winner")
        winner = name3
else:
        #print (name4 + " is the winner")
        winner = name4
                    

#print (winner)
#print (index)

# to calculate the % for the 4 candidates
Khan_p = format((counter1/total_count) * 100, '.3f')
Correy_p = format((counter2/total_count) * 100, '.3f')
Li_p = format((counter3/total_count) * 100, '.3f')
O_p = format((counter4/total_count) * 100, '.3f')


#print (Khan_p)



#Print to terminal
print("Election Results")
print("-------------------------------")
print("Total Votes:" + str(total_count))
print("-------------------------------")
print(name1 + ": "+ Khan_p + "% " + "("+ str(counter1)+ ")")
print(name2 + ": "+ Correy_p + "% " + "("+ str(counter2)+ ")")
print(name3 + ": "+ Li_p + "% " + "("+ str(counter3)+ ")")
print(name4 + ": "+ O_p + "% " + "("+ str(counter4)+ ")")
print("-------------------------------")
print("Winner is " + winner)
print("-------------------------------")


#Print to text file
f= open("pythondata2.txt","w+")

    #f.write("This is line %d\r\n" % (i+1))
f.write("Election Results" + "\n")
f.write("-------------------------------"+ "\n")
f.write("Total Votes:" + str(total_count)+ "\n")
f.write("-------------------------------"+ "\n")
f.write(name1 + ": "+ Khan_p + "% " + "("+ str(counter1)+ ")" + "\n")
f.write(name2 + ": "+ Correy_p + "% " + "("+ str(counter2)+ ")" + "\n")
f.write(name3 + ": "+ Li_p + "% " + "("+ str(counter3)+ ")" + "\n")
f.write(name4 + ": "+ O_p + "% " + "("+ str(counter4)+ ")"+ "\n")
f.write("-------------------------------" + "\n")
f.write("Winner is " + winner + "\n")
f.write("-------------------------------" + "\n")


#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.