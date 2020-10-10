
'''
Senator Mailer: A simple script to mail all senators powered by the NGLEADERS api. Message copied from "Coalition of Concerned Kwarans"
'''
# required libraries
import csv
import smtplib
import ssl
import requests
from os import getenv

# uncomment the code below to test locally
#from dotenv import load_dotenv

# load_dotenv()

# details of throwaway Gmail account
from_address = getenv("YOUR_GMAIL_ACCOUNT")
password = getenv("YOUR_GMAIL_PASSWORD")


# get list of senators from NGLEADERS api. 200 will be our portion always amen!
resp = requests.get('http://ngleadersdb.herokuapp.com/api/senator/all')
list_of_senators = resp.json()["data"]


# The message to be sent to the recipient
message = """Subject: URGENT! SAVE OUR CITIZENS: END SARS! END POLICE BRUTALITY

Distinguished Senator,
{name},
{party},
{district},
{state},
{zone},

PETITION AGAINST THE ACTIVITIES OF THE SPECIAL ANTI-ROBBERY SQUAD(SARS), AKS AND IGP-SQUAD

The aim of the above named is to increase the pace of justice delivery, promoting transparency and accountability, advocating for the civil rights of all Nigerians.

In spite of several reforms announced by the Inspector General of Police, cases of abuse of citizens by the operatives of the SARS/AKS have increased, without any steps taken by the High Command of the Nigerian Police Force to address the fundamental problems of the impunity of the operatives of the SARS/AKS especially in {state}. While we continue to witness the unpleasant consequences of the crime fighting strategy of the force that promotes extra-judicial and extralegal measure, extortion for self enrichment and lawlessness, the non adherence to the prescription of the law poses greater consequences for the ordinary citizens who are the victims of the brutality of the SARS/AKS/IGP X-Squad units in Nigeria.

Considering all of this,

-We hereby demand for compliance of the total disbandment of the SARS/AKS/IGP X-Squad units in all 36 States
of Nigeria and the identification of cases of ill treatment, extortion, harassment and violence in the country.
-In the spirit of fairness, justice and tranquility for victims both dead and alive, we demand an adequate compensation for affected citizens.
-We demand a list of officers who have been held culpable should be published and a transparent prosecution of all guilty officers.
-We demand that unjust harassment, extortion and intimidation of youths by the Nigerian Police Force should stop.
-We demand a public enquiry into the activities of these units in the past year, duly published in the media.
-We demand that all policemen wear identifying tags with their name clearly shown. No police officer should be found on duty 
with a gun or out of official police uniform/gear.
-We demand SARS cells across the nation be open for investigation into detainees.

The above are our demands and we appeal to you, distinguished senator, to use your good office to enforce these statements.

Thank you.

Signed:

NIGERIANS
"""


# create context for security
context = ssl.create_default_context()

# use Google's smtp server to send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)

    for senator in list_of_senators:

        server.sendmail(
            from_address,
            senator['sen_email'],
            message.format(name=senator['sen_name'].title(), party=senator['political_party'],
                           district=senator['district'], state=senator['state'], zone=senator['sen_zone']),
        )
        # print success to console
        print(f"Message sent to {senator['sen_name'].title()}")
