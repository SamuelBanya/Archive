# Progress Notes:

# Path For Program:
# C:\Users\Sam\Documents\My Programming Stuff Folder\2017 Projects\Python\02 My Own Python Projects\Twitter Webscraper

# 8-5-2018: 
# This script is now automated and live on my website as my first Twitter bot, and will run at 1 PM every day without every needing to click "Run" in Repl.it!

# 5-21-2018:
# Got this script to work on my Repl.it version to not save to the current directory, but to just post the URL of the cat image itself to Twitter 

# 4-12-2018:
# Awesome, I got it to embed the image using a parameter called "media" for the twitter.Api.PostUpdate() function.
# This pretty much works. What would be great is if I was able to run this on a server side script without having to run this every day, but its functional
# Definitely could run this on my phone at 12 pm every day and get the same result. Very happy with how this turned out :)
# This definitely makes me want to make more Twitter bots, especially with the ease of use with the Python-Twitter library, and to specifically
# make one regarding hockey, or BandsInTown to determine what math rock bands are currently in the NYC area

# 4-11-2018:
# Success! I was able to post on Twitter using the following documentation provided for the Python-Twitter module:
# https://python-twitter.readthedocs.io/en/latest/getting_started.html
# https://python-twitter.readthedocs.io/en/latest/twitter.html

# This Python script now gathers the cat of the day image, and obtains the URL, and also saves it to the current directory

# The one thing remaining is understanding why I have to subtract 1 from the day value the dayTime variable

# This might be due to Python's time function, strftime(), specifically with the %d parameter to obtain the current day

# Also, maybe gmtime() parameter should be looked at to see what if it matches my time zone, and even the
# Pet Of The Day website as well.

# 4-10-2018:
# After multiple attempts of trying to utilize this StackOverflow case, and a Python for Engineers related image scraping article,
# I was able to save the image to file in the directory!

# Next step is to utilize Twitter's API within Python and create a reposting Twitter account

# Links:
# https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
# https://stackoverflow.com/questions/32853980/temporarily-retrieve-an-image-using-the-requests-library
# https://stackoverflow.com/questions/28396036/python-3-4-urllib-request-error-http-403
# http://pythonforengineers.com/download-all-images-from-a-website/

# 4-9-2018:
# After using multiple examples from StackOverflow regarding the usage of
# urllib in a similar context, I was able to get the exact cat image's URL
# However, now it's saying it's not a valid URL

# Post this on IRC tomorrow, and find out if someone can help with urllib
# URL issues like this

import requests
# from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from time import gmtime, strftime
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
# from urllib.parse import urljoin
# import urllib
# from urllib.request import Request, urlopen
# from PIL import Image
# import urllib.parse, urllib.request
# try:
    # from urllib.parse import urlparse
# except ImportError:
     # from urlparse import urlparse 
# try:
    # from urllib.request import urlrequest
# except ImportError:
     # from urlrequest import urlrequest
import os
import sys
import twitter

# Title Screen:
print("\n\n")
print("***********************************************************")
print(
    "***********************W E L C O M E***********************")
print(
    "***************************T O*****************************")
print(
    "*********************C A T OF THE D A Y********************")
print(
    "***********************T W I T T E R***********************")
print(
    "********************W E B S C R A P E R********************")
print("***********************************************************")
print("\n\n")

print("\n\n")
print("**********************C R E A T E D ***********************")
print("***************************B Y*****************************")
print("**********************SAMUEL  BANYA************************")
print("\n\n")

r = requests.get("http://catoftheday.com/")

soup = BeautifulSoup(r.text, "html.parser")

body = r.text.encode("utf-8")

# Finding Matching Image Using Time Library Methods:
yearTime = strftime("%Y", gmtime())
monthTime = strftime("%B", gmtime())
dayTime = strftime("%d", gmtime())
# Create intDayTime variable since its off by 1 for some weird reason:
intDayTime = int(dayTime)
# Figure out why you need to subtract it by 1 on certain days --> Might be a time zone difference or the original
# website might be 12 hours to 24 hours apart
# intDayTime = intDayTime - 1
# intDayTime = intDayTime - 1
if intDayTime < 10:
	intDayTime = "0" + str(intDayTime)
else:
	intDayTime = str(intDayTime)
desiredCatImageString = "archive/" + yearTime + "/" + monthTime + "/" + intDayTime + ".jpg"
print("desiredCatImageString = " + desiredCatImageString)

images = soup.findAll("img")

for item in images:
    # print("item = " + str(item))
	# print("item's src = " + str(item.attrs["src"]))
    if item.attrs["src"] == desiredCatImageString:
        # print("****")
        # print("\n")
        # print("We've got a match!")
        # print("\n")
        # print("****")
        catName = item.attrs["alt"]
        catCharacterLocation = catName.find("Cat")
        slicedCatNameString = catName[0:catCharacterLocation]
        url = "http://catoftheday.com/"
		# catImageURL = urllib.parse.urljoin(str(url), str(item.attrs["src"]))
        catImageURL = urljoin(str(url), str(item.attrs["src"]))
        print("catImageURL = " + catImageURL)
        catImageRequest = requests.get(catImageURL)
        imageName = os.path.split(catImageURL)[1]
        # with open(imageName, "wb") as file:
        # 	file.write(catImageRequest.content)
        api = twitter.Api(
            consumer_key="",
            consumer_secret="",
            access_token_key="",
            access_token_secret=""
		)
        # print("api = " + str(api))
        # TEST CODE: TESTING TWITTER API'S .PostUpdate() FUNCTION
        # status = api.PostUpdate("I love webscraping and posting on Twitter!")
        # print("imageName = " + imageName)
        # currentPath = os.getcwd()
        # catImagePath = currentPath + "\\" + imageName
        # TEST CODE: SAVING CAT IMAGE TO FILE:
        # status = api.PostUpdate(
            # "Here is the Cat Of The Day!\n\nThe cat's name is: " +
            # slicedCatNameString +
            # "\n\nThe cat's image can be found at the following link:\n" +
            # catImageURL,
            # media=catImagePath)
        status = api.PostUpdate("Here is the Cat Of The Day!\n\nThe cat's name is: " + slicedCatNameString + "\n\nThe cat's image can be found at the following link:\n" + catImageURL, media=catImageURL)
