from pathlib import Path
import csv
import questionary
import sys

from qualifier.utils.save_csv import save_csv
from qualifier.utils.fileio import load_csv


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    #Checks to see if there are any qualifying loans before asking the user for a file path to save the results. 
    if len(qualifying_loans) == 0:
        sys.exit("No results will be saved as there are no qualified loans")
    
    #Quesitonary implementation to ask if the user wants to save their results. 
    save_results = questionary.confirm("Do you want to save the results of your qualifying loan?").ask()
    if save_results == True:

        #Requests a file path for the qualifying bank loans from the user via the command line. 
        csvpath = questionary.text("Enter a file path save the qualifying bank loans (.csv):").ask()
        csvpath = Path(csvpath)
        #Checks the csv path exists before attempting to write to the CSV path. 
        if csvpath.exists():
          save_csv(csvpath, qualifying_loans)
        else: 
            sys.exit(f"Oops! Can't find this path: {csvpath}")

        return load_csv(csvpath)

    else:
        sys.exit("Qualified loans will not be saved to a csv")