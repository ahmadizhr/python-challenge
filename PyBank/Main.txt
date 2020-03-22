import os
import csv

# set path for file
csv_path = os.path.join("Resources","budget_data.csv")
print("Financial Analysis")
print(".........................................")
# open the csv file as reading
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    # read the headers
    headers = next(csv_reader)

    #reading the file without header
    # loop for counting the number of months included in the dataset and the net total amount of "Profit/Losses" over the entire period
    row_count = 0
    change = []
    profit = []
    Date = []
    x = 0
    Total = 0
    for row in csv_reader:
        row_count += 1
        # adding the profits into a list
        profit.append(str(row[1]))
        # adding the Dates into the list
        Date.append(str(row[0]))
        # counting the changes of profit for each two row
        change_profit = int(row[1]) - int(x)
        # adding the changes into the list 
        change.append(str(change_profit))
        x = row[1]
        # counting the Total of net profit
        Total += int(row[1]) 
    print(f'Total Months: {row_count}')   
    print(f'Total: $ {int(Total)}')
    
    # zippig the three lists 
    new = zip(Date,profit,change)
    # create the cvsfile as writing for write the 3 merged lists
    # set the path of output
    output_file = os.path.join("output.csv")
    with open(output_file,'w', newline = '') as datafile:
        writer = csv.writer(datafile, delimiter=",")
        # wite the header on the output file
        writer.writerow(["Date","profit/losses","changes_profit"])
        # write the zipped files into csvile
        writer.writerows(new)

    # The average of the changes in "Profit/Losses" over the entire period and greatest increase and greatest decrease
    Total_changes = 0
    for i in change:
        Total_changes += int(i)
    Total_changes = Total_changes - int(change[0])
    count = len(change) - int(1)
    Avarage = round(float(Total_changes / count) , 2)
    print(f'Average  Change: $ {Avarage}')
    # open the output file as reading 
    csv_path = os.path.join("output.csv")
    with open(csv_path) as rfile:
        csvreader = csv.reader(rfile,delimiter=",")
        # skip the header
        csv_header = next(csvreader)
        # finding greatest increase profits and greatest decrease losses
        max_change = 0
        min_change = 0
        for row in csvreader:
            if int(row[2]) > max_change:
                max_change = int(row[2])
                Date_change = str(row[0])
            if int(row[2]) < min_change:
                min_change = int(row[2])
                Date_changes = str(row[0])
        print("Greatest Increase in Profits:"+" " + str(Date_change) + " "+"($" + str(max_change) + ")" )
        print("Greatest Decrease in Profits:"+" " + str(Date_changes) + " "+"($" + str(min_change) + ")" )
        
        



    

    
    
   




        












