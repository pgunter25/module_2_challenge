# Loan Qualifying App with Interactive CLI 

This is a python application that leverages questionary to automate the creation of an interactive command line interface for users to find out which loans they qualify for. 

---

## Technologies

Technology Requirements 
```code
Python v3.7 
Fire v0.3.1
Questionary v1.5.2
```

---

## Installation Guide

This application can be run via the command line. 


1. Create a new development environment called `loanqualifier` and install the libraries contained in the requirements section above.

  * From your terminal instance, create a new virtual environment called `loanqualifier`, using the following code:

    ```code
    conda create -n loanqualifier python=3.7 anaconda
    ```

  * Activate the new `loanqualifier` environment as follows:

    ```code
    conda activate loanqualifier
    ```

  * Install the provided requirements using the following code:

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

Follow the steps below to see which loans you qualify for. 
1. When you run the loan qualifier app, it will first prompt you to provide it with the file path for the rate-sheet. 

    ![Step 1](https://github.com/pgunter25/module_2_challenge/blob/9f5bf1ea5fb7f63b13339e508d731f86a974ddc1/images/Screen%20Shot%202022-04-04%20at%2012.13.53%20pm.png)

    *Example*
    ![Sample Path](https://github.com/pgunter25/module_2_challenge/blob/1a07ffed2fa2000a2f119f97122e1a01b0035687/images/Screen%20Shot%202022-04-04%20at%2012.18.10%20pm.png)

2. You will then be promoted to fill in details about the loan you are trying to qualify for. Provide numerical answers for the following questions. 
    * What's your credit score? 
    * What's your current amount of monthly debt? 
    * What's your total monthly income? 
    * What's your desired loan amount? 
    * What's your home value? 

    *Example*
    ![Step 2](https://github.com/pgunter25/module_2_challenge/blob/1a07ffed2fa2000a2f119f97122e1a01b0035687/images/Screen%20Shot%202022-04-04%20at%2012.19.53%20pm.png)

    *If there are no loans that you qualify for, you will be notified and the application will exit.* 

3. You will be promted to select if you would like to save the qualified loans to a csv. 

    **Yes, save the results. Continue to Step 4**

    **No, don't save the results.** 

        ![Step3](https://github.com/pgunter25/module_2_challenge/blob/1a07ffed2fa2000a2f119f97122e1a01b0035687/images/Screen%20Shot%202022-04-04%20at%2012.21.24%20pm.png)

4. Provide a file path to save the results to. 
    ![Step 4](https://github.com/pgunter25/module_2_challenge/blob/dbb962b0f6e0d242f4a7212f26cf79dcaf1c75c5/images/Screen%20Shot%202022-04-04%20at%202.04.53%20pm.png)

    *Example*

    ![Step 4](https://github.com/pgunter25/module_2_challenge/blob/dbb962b0f6e0d242f4a7212f26cf79dcaf1c75c5/images/Screen%20Shot%202022-04-04%20at%202.05.30%20pm.png)

---

## Contributors

Phoebe Gunter ([LinkedIn](https://www.linkedin.com/in/phoebe-gunter-58258251/))

Starter files for assignment from UC Berekeley FinTech Course ([Course Cirriculum Link](https://bootcamp.berkeley.edu/fintech/curriculum/))

---

## License

No license terms apply to this application repo. 

