import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyqrcode
from MyQR import myqr
import time
from PIL import Image

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)

client = gspread.authorize(creds)

sheet = client.open("aditya_qr").sheet1
sheet2= client.open("nilesh_id").sheet1
i=0
j=".png"
k=".jpg"
l=1
data = sheet.get_all_records()
col = sheet.col_values(5)
col1 = sheet.col_values(4)
col2 = sheet.col_values(7)
col3 = sheet.col_values(13)
col4 = sheet.col_values(14)

for x in range (1,187):
    i+=1
    l+=1
    sheet2.update_cell(i,1,str(col[x])+str(" ")+str(col1[x]))
    sheet2.update_cell(i,2,str(col2[x]))
    sheet2.update_cell(i,3,str('tutorial_qr'+str(i)+str(j)))
    sheet2.update_cell(l,4,str('img'+str(i)+str(k)))
    time.sleep(1)

