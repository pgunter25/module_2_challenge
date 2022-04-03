from pathlib import Path
import csv

def save_csv(output_path, list):

    '''Testing code to see which loans made it into the list. '''
    #for x in range(len(list)):
        #print(list[x])

    #uses csv writer 
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Adds the loans from the inexpensive loan data dictionary into the csv file. 
        for row in list:
           csvwriter.writerow(row)