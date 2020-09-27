from __future__ import print_function
import httplib2
import os, io
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyqrcode
from MyQR import myqr

from PIL import Image

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Nilesh").sheet1

data = sheet.get_all_records()
col5 = sheet.col_values(17)
i=1
j=".pdf"

pdf_list = [8,16,19,43,52,57,61,68,71,73,80,81,88,97,99,105,119,128,133,134,140,142,144,146,147,148,154,157,160,162,164,166,186]
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'cr.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def downloadFile(file_id,filepath):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(filepath,'wb') as f:
        fh.seek(0)
        f.write(fh.read())
for x in pdf_list:
    str1 = col5[x]   
    str2 = str1.split("=")
    str3 = str2[1]
    i+=1
    print(str2)
    print(i)
    downloadFile(str3,'pdf'+str(i)+str(j))
