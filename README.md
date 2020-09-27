# Identity-cards-using-python
Creating identity cards of a database of people using google sheets and google drive api in python
# Google APIs 
So first thing we need to do is enable all the google api needed and since all the photos of our members is saved in google drive we need google drive api to download them
# Google Drive API
Go to Google API console and sign in using your gmail account and then go to library and search google drive api and enable the api. Once that is done go to its tutorial and documentation.
In documentation you will find build your drive api using different languages choose python their and follow the steps given their.
The quickstart.py file which is given their is saved as drive.py in my repository and you have to change the credentials to your credentials.json file which got downloaded.
# Connecting your drive account with google drive api
To do this step run your quickstart.py (or drive.py from my repository) and then it will open your home browser and ask you to sign in into the account which you want to use once you click done a tocken.pickle file will be downloaded DO NOT DELETTE THIS FILE. Now you have succesfully connected your google drive
# Google Sheets API 
As everything is automated we will be creating a sheet which will be later uploaded in photoshop so that we can generate all ID cards at once.
So first follow the same steps like the drive api and enable your sheets api by searching google sheets in library and enabling it.
Once you do this you get a credentials.json file for this api too and you have to share the sheets with the email id from the json file and that will setup your google sheets api
# Reading Images from google drive 
This step is to be done only if you have succesfully connected your google drive api.
Once you have done that run the drive_photos.py file from repository but some initial changes have to be done as here Iam using ID of each image in the drive to download the image the ID of each image is obtained from the google sheets response of the google form where members will have filled their credentials and you have to edit this with your own google sheet which contains id this goes without saying that you will have to share that sheet with the email id provided in json credentials file for the sheets api.
Once you have done that you can finally use all the ids and run the code and download all the images which will be locally saved.
# Creating sheets for photoshop
Now to create the final sheets for photoshop. You will get the data from your main database sheets using google sheets api like previously done and then you will write the required data in the sheets which you will be using.
# Making qr codes
Again you will be reading the sheets data using sheets api and you can then use the isa_qr.py code to create qr codes but you will have to download the additional modules.
