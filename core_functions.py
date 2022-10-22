from dataclasses import fields
import os
import base64
from typing import List
import time
from urllib import response
from google_apis import create_service
import sys
import shutil
import threading as td
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLineEdit
import io
from googleapiclient.http import MediaIoBaseUpload

class GmailException(Exception):
	"""gmail base exception class"""

class NoEmailFound(GmailException):
	"""no email found"""

service_mail = None
service_drive = None
status = 0
dname = os.getcwd()
query_string = ""
lsStatus = 0 
gdStatus = 0


def Construct_service(api_service):
    CLIENT_SERVICE_FILE = "client-secret.json"
    try:
        if api_service == 'drive':
            API_NAME = 'drive'
            API_VERSION = 'v3'
            SCOPES = ['https://www.googleapis.com/auth/drive']
            return create_service(CLIENT_SERVICE_FILE, API_NAME, API_VERSION, SCOPES)
        elif api_service == 'gmail':
            API_NAME = 'gmail'
            API_VERSION = 'v1'
            SCOPES = ['https://mail.google.com/']
            return create_service(CLIENT_SERVICE_FILE, API_NAME, API_VERSION, SCOPES)

    except Exception as e:
        print(e)
        return None

def login():
    global service_mail
    service_mail = Construct_service('gmail')


def logout():
    shutil.rmtree(os.path.join(os.getcwd(), 'token files'))


def search_emails(service, query_string: str, label_ids: List = None):
    try:
        message_list_response = service.users().messages().list(
            userId='me',
            labelIds=label_ids,
            q=query_string
        ).execute()

        message_items = message_list_response.get('messages')
        next_page_token = message_list_response.get('nextPageToken')
        while next_page_token:
            message_list_response = service.users().messages().list(
                userId='me',
                labelIds=label_ids,
                q=query_string,
                pageToken=next_page_token
            ).execute()

            message_items.extend(message_list_response.get('messages'))
            next_page_token = message_list_response.get('nextPageToken')
        return message_items
    except Exception as e:
        raise NoEmailFound('No emails returned')


def get_file_data(service, message_id, attachment_id, file_name, save_location):
    response = service.users().messages().attachments().get(
        userId='me',
        messageId=message_id,
        id=attachment_id
    ).execute()

    file_data = base64.urlsafe_b64decode(
        response.get('data').encode('UTF-8'))
    return file_data


def get_message_detail(service, message_id, msg_format='metadata', metadata_headers: List = None):
    message_detail = service.users().messages().get(
        userId='me',
        id=message_id,
        format=msg_format,
        metadataHeaders=metadata_headers
    ).execute()
    return message_detail


def save_attachments():
    global status
    global service_mail
    global query_string
    # query_string = 'is:unread has:attachment after:2022/9/7'
    print(query_string)
    save_location = dname

    while status:

        email_messages = search_emails(service_mail, query_string)

        for email_message in email_messages:
            messageId = email_message['threadId']
            
            messageDetail = get_message_detail(
                service_mail, email_message['id'], msg_format='full', metadata_headers=['parts'])
            messageDetailPayload = messageDetail.get('payload')

            #Getting Subject of Mail
            for item in messageDetailPayload['headers']:
                if item['name'] == 'Subject':
                    if item['value']:
                        MessageSubject = '{0} ({1})'.format(item['value'], messageId)
                    else:
                        MessageSubject = '(No Subject) ({0})'.format(messageId)

            if(gdStatus):
                folder_id = create_folder_drive(service_drive, MessageSubject)['id']

            if 'parts' in messageDetailPayload:
                for msgPayload in messageDetailPayload['parts']:
                    mime_type = msgPayload['mimeType']
                    file_name = msgPayload['filename']
                    body = msgPayload['body']
                    if 'attachmentId' in body:
                        attachment_id = body['attachmentId']
                        attachment_content = get_file_data(
                                                           service_mail, email_message['id'], attachment_id, file_name, save_location)
                        
                        if(lsStatus):
                            with open(os.path.join(save_location, file_name), 'wb') as _f:
                                _f.write(attachment_content)
                                print(
                                    f'File {file_name} is saved at {save_location}')
                        elif(gdStatus):
                            fh = io.BytesIO(attachment_content)
                            file_metadata = {
                                'name': file_name, 
                                'parents': [folder_id]
                            }

                            media_body = MediaIoBaseUpload(fh, mimetype = mime_type, chunksize=1024*1024, resumable=True)

                            file = service_drive.files().create(
                                body = file_metadata, 
                                media_body = media_body,
                                fields = 'id'
                            ).execute()

                            print(F'Folder created with ID: "{file.get("id")}".')

            time.sleep(0.5)
    return 


def start_download(k):
    # global service
    global status
    status = k
    # service = create_service('client-secret.json',
    #                               'gmail', 'v1', ['https://mail.google.com/'])

    trd = td.Thread(target=save_attachments, args=())

    trd.start()

def stop_download(k):
    global status
    status = k
    
def choose_directory():
    global dname
    dname = QFileDialog.getExistingDirectory(
        None, 
        caption="Select Download Location"
    )
    print(dname)

def create_folder_drive(service, folder_name, parent_folder=[]):
    file_metadata = {
        'name': folder_name, 
        'parents': parent_folder, 
        'mimeType': 'application/vnd.google-apps.folder'
    }

    file = service.files().create(body = file_metadata, fields = 'id').execute()
    return file


def filters(email_from, domain, date, unread, localStorage, gDrive):
    global query_string
    global service_drive
    global lsStatus, gdStatus
    lsStatus = localStorage
    gdStatus = gDrive

    if(gdStatus):
        service_drive = Construct_service('drive')
    if(unread):
        query_string = "is:unread "+" has:attachment "+"after:"+date
    else:
        query_string = "after:"+date
