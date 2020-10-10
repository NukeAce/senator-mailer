# Senator-Reminder
A simple Python script to "remind" our Nigerian senators about the ongoing fight🤼🔥 to [#ENDSARS](https://twitter.com/hashtag/endsars?lang=en)😡🛑🚫👮🏾‍♂️

This script will send a reminder email to Nigerian Senators once a day until our demands are met!

***Note: Make sure to have Python 3 installed***
## Dependencies
- [x] Requests library
- [x] [NGLEADERS](http://ngleadersdb.herokuapp.com/api)- An api with detailed information about Nigerian Senators 📚📑

## Usage
- Step 1: Clone this GitHub repository in a local directory
  ```bash
  git clone https://github.com/NukeAce/Bookscraper.git
  ```

- Step 2: Run requirements.txt file to install dependencies  
  ```bash
  pip install -r requirements.txt
  ```
- Step 3: Create a throwaway Gmail account and go to Manage Accounts > Security > Less Secure App Access

- Step 3.5 (*optional*):
  
    For local testing/development install python-dotenv to access environment variables,

    ```bash
    pip install python-dotenv
    ```
    then in the .env file fill your gmail email and password.
    
    Change the api request to a list of dictionaries(I included one in the comments above it) and run the script with
    ```bash
    python senatormailer.py
    ```
    to test. 


- Step 4: 
  Deploy to Heroku using the following steps:

  Step4a: Open [Heroku](https://heroku.com) and sign up if you haven't.
  
  Step4b: TBC
    


