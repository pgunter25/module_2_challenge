# Loan Qualifying App with Interactice CLI 

This is a python application that leverages questionary to automate the creation of an interactive command line interface with the user to find out which loans they are qualified for. 

---

## Technologies

Requirements 
```code
Python v3.7 
Fire v0.3.1
Questionary v1.5.2
```

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

2. Clone the git repo by following the instructions below 

    ```code
    git clone https://github.com/pgunter25/module_2_challenge.git
    ```

3. Navigate into the folder that you cloned from github. Run [`app.py`](module_2_challenge/app.py) to see which loans you qualify for. 

    ```code
    python app.py
    ```


---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.
1. When you run the loan qualifier app, it will first prompt you to provide it with the file path for the rate-sheet. 
![Step 1](https://github.com/pgunter25/module_2_challenge/blob/9f5bf1ea5fb7f63b13339e508d731f86a974ddc1/images/Screen%20Shot%202022-04-04%20at%2012.13.53%20pm.png)

*Example 
    ![Sample Path](https://github.com/pgunter25/module_2_challenge/blob/9f5bf1ea5fb7f63b13339e508d731f86a974ddc1/images/Screen%20Shot%202022-04-04%20at%2012.13.53%20pm.png)

---

## Contributors

Phoebe Gunter ([LinkedIn](https://www.linkedin.com/in/phoebe-gunter-58258251/))
Starter files for assignment from UC Berekeley FinTech Course ([Course Cirriculum Link](https://bootcamp.berkeley.edu/fintech/curriculum/))

---

## License

No license terms apply to this application repo. 

