from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('gmail', 'v1', credentials=creds)

        msgs = service.users().messages().list(userId='me', maxResults=500).execute()

        mssg_list = msgs['messages']

        print ("Total messages: ", str(len(mssg_list)))

        final_list = [ ]

        user_id='me'

        for mssg in mssg_list:
            temp_dict = { }
            m_id = mssg['id'] 
            message = service.users().messages().get(userId=user_id, id=m_id).execute()
            payld = message['payload']  
            headr = payld['headers'] 


            for one in headr: 
                if one['name'] == 'Subject':
                    msg_subject = one['value']
                    temp_dict['Subject'] = msg_subject
                else:
                    pass

            '''
            for two in headr: # getting the date
                if two['name'] == 'Date':
                    msg_date = two['value']
                    date_parse = (parser.parse(msg_date))
                    m_date = (date_parse.date())
                    temp_dict['Date'] = str(m_date)
                else:
                    pass
            '''
    
            for three in headr: 
                if three['name'] == 'From':
                    msg_from = three['value']
                    temp_dict['Sender'] = msg_from
                else:
                    pass

        
            #temp_dict['Snippet'] = message['snippet'] # fetching message snippet

            print (temp_dict)
            final_list.append(temp_dict)
            
        print ("Total messaged retrived: ", str(len(final_list)))

        with open('emails.csv', 'w', encoding='utf-8', newline = '') as csvfile: 
            fieldnames = ['Sender','Subject']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
            writer.writeheader()
            for val in final_list:
                writer.writerow(val)

    except HttpError as error:
        # TODO - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()