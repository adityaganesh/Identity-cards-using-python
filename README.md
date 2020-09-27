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

