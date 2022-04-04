# Loan Qualifying App with Interactice CLI 

Just after the title, introduce your project by describing attractively what the project is about and what is the main problem that inspires you to create this project or what is the main contribution for the potential user of your project.

---

## Technologies

Requirements 
Python v 3.7 

Imports to Application  
```import sys
import fire
import questionary
from pathlib import Path
import csv
```
This is a python application that leverages questionary to automate the creation of an interactive command line interface with the user. 

Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.

---

## Installation Guide

This application can be run via the command line. 


1. Create a new development environment called `loanqualifier` and install the libraries contained in the requirements section above.

  * From your terminal instance, create a new virtual environment called `atmdev`, using the following code:

    ```code
    conda create -n loanqualifier python=3.7 anaconda
    ```

  * Activate the new `loanqualifier` environment as follows:

    ```code
    conda activate loanqualifier
    ```

  * Navigate to the root of this activity folder and install the provided requirements using the following code:

    ```code
    pip install questionary
    pip install fire
    ```

2. Open [`atm.py`](atm/atm.py) and review the Python script. Then open [`utils.py`](atm/utils.py) and [`make_withdrawal.py`](atm/actions/make_withdrawal.py). You'll be completing the following functions:

  * `verify_pin(pin)`, located in the utils module

    * Verify that the length of the pin is six characters.

      * If true, print a validation message and return `True`.

      * If false, then return `False`.

  * `make_withdrawal(account)`, located in the actions folder

    * Use `make_deposit(account)` as a guide.

    * Complete the docstring using the docstring from `make_deposit(account)` as a guide.

    * Use the Questionary library to ask the user how much they want to deposit. Set the return equal to the variable `amount`. Make sure that `amount` is a floating point value.

    * If `amount` is less than or equal to 0.0, exit the system with an error message indicating that it’s not a valid withdrawal amount.

    * Validate that `amount` is less than or equal to `account["balance"]`.

      * If the amount is valid, adjust the `account["balance"]` for the withdrawal, and print a confirmation message and return the adjusted account.

      * If the amount isn't valid, exit the system with an error message that tells the user that they don't have enough money in the account to cover the withdrawal.

3. Run your application!


---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.
![<alt text>](<url>)

---

## Contributors

Phoebe Gunter ([LinkedIn](https://www.linkedin.com/in/phoebe-gunter-58258251/))
UC Berekeley FinTech Course ([Course Cirriculum Link](https://bootcamp.berkeley.edu/fintech/curriculum/))

---

## License

No license terms apply to this application repo. 

