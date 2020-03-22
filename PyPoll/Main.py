import os
import csv

# set path for file
csv_path = os.path.join("Resources","election_data.csv")
print("Election Results")
print(".........................................")
# open the csv file as reading
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    # read the headers
    headers = next(csv_reader)
    Total_Count = 0
    candidates_list = []
    vote_count = [0,0,0,0]
    for row in csv_reader:
        Total_Count += 1
        if str(row[2]) not in candidates_list:
            candidates_list.append(str(row[2]))
        if row[2] == "Khan":
            vote_count[0] += 1
        elif row[2] == "Correy":
            vote_count[1] += 1
        elif row[2] == "Li":
            vote_count[2] += 1
        elif row[2] == "O'Tooley":
            vote_count[3] += 1
    print("Total Votes: " + str(Total_Count))
    print("........................................")
    #print(candidates_list)
    #print(vote_count)
    
    percentage_vote = []
    percentage = 0
    for i in vote_count:
        percentage = round(float(int(i) / int(Total_Count)),3)
        percentage_vote.append(str(percentage))
    #print(percentage_vote)
    
    new=zip(candidates_list,vote_count,percentage_vote)

    output_file = os.path.join("output.csv")
    with open(output_file,'w',newline = '') as datafile:
        writer = csv.writer(datafile, delimiter=",")
        # wite the header on the output file
        writer.writerow(["Candidate","Percentage_Votes","Total_Votes"])
        writer.writerows(new)

    
    output_path = os.path.join("output.csv")
    with open(output_path) as rfile:
        csvreader = csv.reader(rfile,delimiter=",")
        # read the headers
        headers = next(csvreader)
        win = 0
        win_name = " "
        for row in csvreader:
            if int(row[1]) > win:
                win = int(row[1])
                win_name = str(row[0])
            x = round(float(float(row[2]) * 100),3)
            print(str(row[0])+": "+str(x)+"00% ("+str(row[1])+")")
        print("........................................................")
        print("Winner: "+str(win_name))
        print("......................................")
        
















