import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyqrcode
from MyQR import myqr

from PIL import Image

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)

client = gspread.authorize(creds)

sheet = client.open("new_entries").sheet1
sheets2 = client.open("ps").sheet1


#pprint(row)



i=1
j=".png"
for x in range(186,268):
    

    sheets2.update_cell(i,4,str(x)+str(j))
    i+=1
    

