import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyqrcode
from MyQR import myqr

from PIL import Image

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds1.json", scope)

client = gspread.authorize(creds)

sheet = client.open("aditya_qr").sheet1

data = sheet.get_all_records()
col = sheet.col_values(5)
col1 = sheet.col_values(4)
col2 = sheet.col_values(7)
col3 = sheet.col_values(13)
col4 = sheet.col_values(14)
#pprint(row)



i=0
j=".png"
for x in range(1,187):

    i+=1
    url = col2[x]+str(" ")+col[x]+str(" ")+col1[x]+str(" ")+col4[x]+str(" ")+col3[x]
    qrobj = pyqrcode.create(str(url))
    with open('test.png', 'wb') as f:
        qrobj.png(f, scale=10)

    # Now open that png image to put the logo
    img = Image.open('test.png')
    width, height = img.size
    
    # How big the logo we want to put in the qr code png
    logo_size = 90

    # Open the logo image
    logo = Image.open('ISA-1.png')

    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    img.save('tutorial_qr'+str(i)+str(j))
    
