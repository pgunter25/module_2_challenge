from pathlib import Path
import csv


def save_csv(output_path, list):

    '''Testing code to see which loans made it into the list. '''
    #for x in range(len(list)):
        #print(list[x])

    #uses csv writer to write the list provided as part of the function call to a CSV. 
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in list:
           csvwriter.writerow(row)