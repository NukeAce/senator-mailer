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

  4a: Open [Heroku](https://heroku.com) and sign up if you haven't.
  
  4b: Create a new app

  4c: Configure app to connect with your GitHub project in the Deploy > Deploy Method tab

  4d: Configure the .env variables using settings > Reveal Config Vars and entering YOUR_GMAIL_ACCOUNT & YOUR_GMAIL_PASSWORD in the key area and your Gmail Credentials in the corresponding value area

- Step5: 
  To Schedule the mail to send to the senators

  5a: In your app dashboard to resources and search for Heroku Scheduler and add it to your deployment.(its free!)

  5b: In Heroku Scheduler click create job, set the time and add 
  ```bash
  python senatormailer.py
  ```
  in the Run Command field.

  Save job and you're done!!


  **JOIN THE FIGHT TO END SARS! HOLD YOUR LEADERS ACCOUNTABLE!! [#ENDSARS](https://twitter.com/hashtag/endsars?lang=en)**

*PS: Stuck? We all get stuck open an issue or shoot a dm to [@hmedtijani](https://twitter.com/hmedtijani)*
    


