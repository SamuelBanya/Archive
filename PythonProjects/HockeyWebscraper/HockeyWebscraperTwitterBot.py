# coding=utf-8

from bs4 import BeautifulSoup
import random
import requests
import xlsxwriter
import twitter
import ftplib

# 9-11-2018:
# This project is finally complete, and will run at 1 PM every day to post results on Twitter

# 9-10-2018:
# Currently having unicode issues since I'm forced to use Python 2 on the stupid
# shared webhosting server. However, I found a good resource that might
# clarify the current error I'm getting:

# https://nedbatchelder.com/text/unipain.html

# 9-6-2018:
# I was able to just use the dataLocation variable as the link, and successfully post to twitter

# All that's left is to just add the team logos to this project, and include them in a separate image
# dictionary

# 8-27-2018:
# I tried removing spaces from the Excel report name with .replace(' ', ''), but its still giving me an HTTP 404 Error regarding
# Urllib.request.urlretrieve()

# I'll try to keep getting help from IRC though, but I'm thinking that it might need a pure URL instead.

# 8-22-2018:
# Getting closer with the ftp request though now its giving me an unknown URL error 

# Read more of the docs regarding urllib.request:
# https://docs.python.org/3/library/urllib.request.html

# Relevant StackOverflow Examples:
# https://stackoverflow.com/questions/17960942/attributeerror-module-object-has-no-attribute-urlretrieve
# https://stackoverflow.com/questions/12613797/python-script-uploading-files-via-ftp

# 8-21-2018:
# I've been trying to use the documentation on ftplib, as well as this StackOverflow case, but haven't seen any files actually be uploaded to the server, fix this:
# https://docs.python.org/3/library/ftplib.html
# https://stackoverflow.com/questions/12613797/python-script-uploading-files-via-ftp

# 8-20-2018:
# I finally was able to pop the Montreal Canadiens value with a related example from Stack Overflow in which you replace the dictionary key with the one you want to remove
# in the same assignment statement, and then you use the .pop() function to pop the original key out of the dictionary.

# Will now work on incorporating the FTP module from Python in conjunction with the InMotionHosting email to create a server side link for the user to download the link.
# Once that works, I will run this on a Cron job to run once per hour on my Twitter account to finish the project.

# 8-14-2018:
# I've been working on this for the past couple days to get it up to speed. So far, this saves to an .xlsx file correctly. However,
# Python-Twitter does not handle .xlsx files apparently (through trial and error). I also tried using Tweepy, another Python module for Twitter
# but confirmed through GitHub that they only support jpg, png, and gif files.

# With that in mind, I need to figure out how to host the .xlsx file using the actual web server itself (InMotionHosting) through FileZilla or another client
# through Python. I'll open up a support ticket through InMotionHosting and see what I can do.

# FTP Modules For Python:
# https://docs.python.org/2/library/ftplib.html#ftplib.FTP.transfercmd
# https://www.pythonforbeginners.com/code-snippets-source-code/how-to-use-ftp-in-python

# Paramiko Guide For Python:
# https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73

# 7-30-2018:
# After much deliberating, I decided that its just better to simplify things and not consider using dictionaries for this example since its better to just return a list 
# of players with related data, as well as a season

# This makes iterating and thinking about all of it easier. Work on actually placing sample Excel data into a spreadsheet, saving it to the same directory using xlsxwriter. 
# Then, once that's working, place the scraped data inside.

# 7-25-2018:
# After painstakingly going through each season's object property, I was able to fix one issue that involved a double link for the seasonHeaderLinks and seasonHeaderData lists.
# Luckily, I fixed this by popping the first value out of the list, and was able to add every data point available.

# The next step is to place this onto an Excel .csv file, open it in the directory to save it, save it, then add it as an attachment to an e-mail to finish the project

# 7-19-2018:
# After being able to use the .find_next_sibling() method on individual items, I was able to retrieve links within specific tags
# I then assembled all the relevant information from the team's table, and everything currently works. The next step is to construct an object to hold this data
# by using the HockeyReferenceSeasonData class

# 7-18-2018:
# After using a two-pronged approach by demoing the current problem aka website I'm scraping for this project in the Python terminal aka IDLE BEFORE actually writing the solution
# in this script, I was able to keep coding more efficiently without burning out due to run times. Very cool approach. I was able to rip the th tag for the header row
# and the individual stat rows for the hockey team's website that the user requested

# Now that I have the data, work on creating objects with this data.

# 7-17-2018:
# Created a sorted version of the dictionary in the "displayDictionaryValues" function, since I wanted to display alphabetic names of the hockey teams to the user

# I created a variable called hockeyReferenceTeamWebsites, which indexes into the teamLinks variable with the "href" attribute
# I then created a hockeyReferenceTeamNames list variable to rip the .text values out of the teamLinks variable.

# I then created a dictionary called "linkDictionary" with dict() and zip() methods to match the hockey team name with its website from hockey-reference.com 

# Now that I have this information together, I'm able to use the value from the hockeyTeamName variable, which is the hockey team name that the user passes in, and then 
# index into this linkDictionary so that I can scrape that specific team's website.

# Now that we have the website that the user wants, work on scraping data from table rows that are present.

# 7-16-2018:
# Rethought everything, and realized I should be doing the same kind of scrape for the Hockey Reference Table website as well, since the individual NHL team websites have WAY more relevant
# information than just a row per team.

# Continue with actually scraping the individual websites

# 7-11-2018:
# By using the in keyword, I was able to get closer to what I want. The issue now that I need to take care of is to add in another if condition where
# it only looks at rows that contain a "href" attribute since these are the only teams that are currently TRUELY active, i.e. the current Anaheim Ducks, NOT
# "The Mighty Ducks" etc, and other team name changes present in the active franchise team table.

# Also, another person on IRC mentioned the idea to use PANDAS instead next time for a situation like this to rip data from a table. I'll do this if needed next time too.

# I tried spending even more time to use if statement to hone in on table rows that only contained an href value, but this is hard to do while cycling through the 
# for loop. This ultimately created a list of lists, which I DO NOT want. I want actual <td> tags that were correctly obtained by only looking at parts of the table
# that contained an "href" string since this would ultimately mean its a current team. Rethink this.

# 7-9-2018:
# Got closer today by using the .select() method by specifying the td with the data-stat attribute
# I tried indexing into this by using the "year-min" value for data-stat, but this didn't give back anything

# Keep trying to reference the BS4 documentation's "Find tags by attribute value:" section

# 6-26-2018:
# Was sick with mono for the past several weeks. Back on this project, and am trying to get the "yearTeamStarted" variable to assign itself as a list of data-stat values
# from a td tag associated with each team. Fix this.

# 6-6-2018:
# I feel great about this project, because I was able to finally re-think it over, and go with my initial hunch, which was to go straight for the <div> tag 
# that contained just the active franchise hockey teams, and NOT teams that have been long dead.

# With this idea in mind, I went after the div tag with id = "div_active_franchises", by first providing "div" as the first argument to soup.find(), and then 
# providing a dictionary key value object {"id": "div_active_franchises"} to find the allActiveFranchisesDivData. I then ripped the tbody tag from this data
# by using soup.find("tbody") on this variable. Then, I used soup.select(".full_table") to hone in on the tr tags with the "full_table" class

# I iterated through it with a for loop print statement, and got the data I want. Now, I have to place this data into another object called hockeyTeamReferenceData() 
# which will contain even more team based statistics. The goal after that is to then match the user's input to this team data, and then add that to the running team object

# It might make sense to just add to the existing playerList data object as well to create an overall object that contains player information, and team information. 

# A minor note that the text between the <a> tag containing the Hockey Reference team's webpage might be good to use to define the overall team somehow with a 
# "teamName" variable

# Very fun so far.

# 6-4-2018:
# I tried using soup.find_all() in several different ways to ultimately get the exact table of current franchise hockey teams. However, it's not as easy as I thought
# since I thought I would be able to just specify the exact class of the overarching table, class_="active_franchises_clone"

# However, the current approach is to just use soup.find_all() to rip all tables. And then from that object, I will then pull out <tr> tags with class_="full_table"

# The problem with just looking for table row <tr> tags with this class_="full_table" is that you get table rows for both active AND defunct teams listed on the 
# same page. I'm thinking that this could be totally avoided by deliberately going after the correct table, and then using .next_sublings() from BeautifulSoup4 
# to get a streamlined and more logical / direct approach.

# I don't necessarily like this approach of scraping all tables  since the <table> tag with class_="active_franchises_clone" would give me the specific table I want, 
# it's not producing any values when I print it as a test statement.

# I'll post this on IRC to get further help from someone who knows BeautifulSoup4 a bit more.

# 5-31-2018:
# I added a function called askHockeyTeamName(), which might seem unnecessary, but I will need that information later for another function on a separate website
# called Hockey Reference, in which I will use the team name to specifically look for even more team stats that aren't provided on the NHL website. This function 
# returns the hockeyTeamName variable which basically comes from the input() that the user gives.

# I added that variable, hockeyTeamName, as a parameter for the NHLTeamRosterSearch() function, and that worked just fine.

# I am currently working on hockeyReferenceStatScrape(), which is a function that scrapes data from Hockey Reference's website. I successfully was able to
# rip the <tbody> tag data that I need. What I need to do next is to index into this scraped data, using the hockeyTeamName variable, and then
# create a hockeyTeamData() class which will hold this information. After that, I should think about combining the list of player objects into this data,
# and possibly make a list containing all player objects, and another list containing team data stats.

# The end goal would be to then either display the data for the user, or e-mail the results to the user depending on their final input

# 5-30-2018:
# I figured out that you can obtain the current index numerical value using (list name).index(for loop iterator variable)

# By using this, I was able to index into the individual lists I accumulated, and then assigned player object property variables
# to those list values since all lists of data are the same length.

# Start working on a function that will scrape the following website for further team related stats:
# https://www.hockey-reference.com/teams/

# 5-24-2018:
# I used the idea of adding a "Player" class whose attributes would then be dicated by available list data, aka firstNameList, lastNameList, hometownList, etc.

# I simply used the name, "Frank", as a test, and later accessed it using the dot operator with the print statement. At this point, it actually works, but I still
# have to figure out how I am going to also convert the "f" and "l" variables to integers so I can index into the relevant lists to create objects

# The idea at this point is to make a list of objects instead of going the dictionary route, since this makes sense. I could maybe then make a dictionary using the
# first and last name pair as the key, and the entire object as its value, which makes sense in a way. Figure out how to index into the other lists.

# 5-14-2018:
# Added items from firstNameList and lastNameList together to create key pairs to later make a master dictionary for hockey players
# It will look something like this:

# {"key": "Wayne Gretzky" ... etc}

# This means that each player will have their own dictionary of information, but will be ultimately referenced by their initial key of firstName + lastName 

# Work on incorporating other lists of data into the dictionary

# 5-8-2018:
# Trying to reason how to make a master list of dictionaries for each player. I have the desired output, but I might have to look up relevant
# answers on StackOverflow.

# Someone on IRC mentioned using: ' '.join((first_name, last_name)).lower for keys

# 5-7-2018:
# I was able to successfully use .find_all() to rip player number, shooting hand, player height, player weight, and player hometown for each of the players

# However, the issue now is that the birthday is usually a span tag underneath an overarching td tag. I could try to use the span tag's class name
# but this same class name, aka class="xs-sm-md-only" AND class="all-but-xs-sm-md", which are basically long and shorthand forms
# of dates is ALSO used for heights as well

# UPDATE: After tinkering with it, I was just able to literally rip the date using "td", class_="birthdate-col"

# However, I used [:] to slice into the string version of the date in order to create short and long hand forms of the date if the user wants it later on

# Goal at this point is to now rip scores and stats from: https://www.hockey-reference.com/teams/

# Very cool progress so far

# 5-2-2018:
# I thought about this project, and realized that the NHL website is not a good source for scores for teams for some weird reason
# That being noted, I can still use the work I have done so far, because I can just use the NHL website for a team roster section
# This section will contain a dictionary of the following information, which is available on every team's roster
# # 	Pos 	Sh 	Ht 	Wt 	Born 	Birthplace

# With this in mind, focus on getting these items to make a cool dictionary database. Later once this is finished, use the following
# website to scrape for scores:

# https://www.hockey-reference.com/teams/

# Another thought is to keep the roster and scores as options by the user, much like the music webscraper where I prompted
# the user for either notes or chords with just a "1" or "2" value to make things simple

# 5-1-2018:
# I successfuly used dict(zip()) methods correctly. However, since this creates a dictionary, its better to just add this assignment
# statement to a variable, and not cycling through them with a for loop HENCE why you only saw the key value each time

# I also used [:-1] to strip the team name string of its last space character, so that the user can look at the available hockey team names
# and then type in the name of the hockey team to scrape the webpage for that particular team

# What's cool is that by creating another r, requests.get() variable, you're able to search deeper into a website for more information

# Rip the score information from the hockey team websites next

# 4-30-2018:
# I tried simply dict() and zip() to use the dict() constructor, and the zip() method to just use two lists to create
# key value pairs, but its only still adding team names, and not their website links. Fix this.

# 4-25-2018:
# I consolidated much of the code based on the .find("a") idea, and just to rip team text using the .text property, and using
# .get("href") to obtain the links into separate lists

# I then learned about the .zip() method to cycle through both lists, and then using the dictionary specific .update() method for dictionaries that functions 
# like the .append() function from arrays

# However, this is only creating dictionaries that contain the team name. Fix this.

# 4-24-2018:
# I found a related StackOverflow answer regarding how to rip text from an HTML element in BS4 by using .text on the item in the list itself during
# the for loop
# https://stackoverflow.com/questions/8112922/beautifulsoup-innerhtml

# By using a third list called fullHockeyTeamNameList, I was able to use .append
# to append parts from hockeyTeamCities and hockeyTeamNames lists, and create a reference
# list I could use to store into dictionaires for the user to reference the team's website

# Work on ripping out the website for the team next, and add it to the fullHockeyTeamNameList
# as a dictionary aka keys and values


# 4-23-2018:
# Getting closer, using the following StackOverflow answer, and found out that you can pass in a second parameter for .find_all(), by providing class_="" as a second parameter
# https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class

# 4-20-2018:
# I started trying this project with a Google search, but realized that the score tables they give you are generated from a
# "Sports App", so I'm better off just scraping data from NHL's website instead.

# webscraperSearch() was the initial attempt

# teamNameScrape() is the attempt to rip the names of all the teams, so I don't have
# to copy and paste the team names by hand

# webscraperSearch2() is the attempt to scrape the NHL webpage

hockeyTeamDictionary = {}

class Player(object):
    pass

class HockeyReferenceSeasonData(object):
    pass

def NHLTeamNameScrape():
    r = requests.get("https://www.nhl.com/info/teams")
    soup = BeautifulSoup(r.text, "html.parser")
    hockeyTeamLinks = soup.find_all("a", class_="team-city")
    hockeyTeamNameList = []
    hockeyTeamHrefLinks = []
    # print("\n\nNow going through hockeyTeamLinks to rip team name text: \n\n")
    for item in hockeyTeamLinks:
        teamNameString = str(item.text)
        # TEST LINE 313 Modified to not include byte characters
        # teamNameString = (item.text).encode('utf-8')
        spaceRemovedTeamNameString = teamNameString[:-1]
        hockeyTeamNameList.append(spaceRemovedTeamNameString)
        hockeyTeamHrefLinks.append(item.get("href"))
    # print("\n\nNow going through hockeyTeamNameList to display team names: \n\n")
    # for item in hockeyTeamNameList:
        # print("Hockey Team Name = " + item)
    # print("\n\nNow going through hockeyTeamHrefLinks to display team links: \n\n")
    # for item in hockeyTeamHrefLinks:
        # print("Hockey Team Website Link = " + item)
    # print("\n\nNow creating key value pairs for hockeyTeamDictionary: \n\n")
    dictionary = dict(zip(hockeyTeamNameList, hockeyTeamHrefLinks))
    # print("\n\nNow going through dictionary key-value pairs: \n\n")
    # print(dictionary)
    return dictionary

def changeMontrealTeamName(hockeyTeamDictionary):
  modifiedHockeyTeamDictionary = hockeyTeamDictionary
  for key in modifiedHockeyTeamDictionary:
      print("key = " + str(key))
  modifiedHockeyTeamDictionary['Montreal Canadiens'] = modifiedHockeyTeamDictionary.pop('Montréal Canadiens')
  # modifiedHockeyTeamDictionary[b'Montreal Canadiens'] = modifiedHockeyTeamDictionary.pop(b'Montr\xc3\xa9al Canadiens')
  return modifiedHockeyTeamDictionary

def displayDictionaryValues(modifiedHockeyTeamDictionary):
  # print("\n\nHere are the current NHL teams to choose from: \n\n")
  sortedTeamDictionary = sorted(modifiedHockeyTeamDictionary)
  # for key in sortedTeamDictionary:
	  # print(key)
    # print(repr(key))

def chooseRandomTeam(modifiedHockeyTeamDictionary):
    randomNumber = random.randrange(0, len(modifiedHockeyTeamDictionary))
    randomTeam = list(modifiedHockeyTeamDictionary.keys())[randomNumber]
    print("\n\nrandomNumber = " + str(randomNumber) + "/n/n")
    print("\n\nKey found at that position = " + str(randomTeam))
    return randomTeam

def askHockeyTeamName():
    hockeyTeamName = input("\n\nPlease enter the name of the hockey team shown above that you wish to research stats of (Make sure to copy and paste for French Canadian team names):\n\n")
    return hockeyTeamName

def NHLTeamRosterSearch(modifiedHockeyTeamDictionary, hockeyTeamName):
    r = requests.get(str(modifiedHockeyTeamDictionary[hockeyTeamName]) + "/roster")
    soup = BeautifulSoup(r.text, "html.parser")
    firstNameList = soup.find_all("span", class_="name-col__item name-col__firstName")
    # print("\n\nNow going through first names:\n\n")
    # for item in firstNameList:
        # print("firstName = " + str(item.text))
    lastNameList = soup.find_all("span", class_="name-col__item name-col__lastName")
    keyList = []
    # print("\n\nNow going through last names:\n\n")
    # for item in lastNameList:
        # print("lastName = " + str(item.text))
    playerNumberList = soup.find_all("td", class_="number-col fixed-width-font")
    # print("\n\nNow going through player numbers:\n\n")
    # for item in playerNumberList:
        # print("playerNumber = " + str(item.text))
    shootingHandList = soup.find_all("td", class_="shoots-col fixed-width-font")
    # print("\n\nNow going through shooting hands for players:\n\n")
    # for item in shootingHandList:
        # print("Player's Shooting Hand = " + str(item.text))
    playerHeightList = soup.find_all("td", class_="height-col fixed-width-font")
    # print("\n\nNow going through heights of all players:\n\n")
    # for item in playerHeightList:
        # print("Player's Height = " + str(item.text))
    playerWeightList = soup.find_all("td", class_="weight-col fixed-width-font")
    # print("\n\nNow going through weights of all players:\n\n")
    # for item in playerWeightList:
        # print("Player's Weight = "  + str(item.text) + " pounds")
    playerBirthdayList = soup.find_all("td", class_="birthdate-col")
    shortDatePlayerBirthdayList = []
    longDatePlayerBirthdayList = []
    for item in playerBirthdayList:
        regularDate = str(item.text)
        shortDate = regularDate[:8]
        shortDatePlayerBirthdayList.append(shortDate)
        longDate = regularDate[8:]
        longDatePlayerBirthdayList.append(longDate)
    # print("\n\nNow going through birthdays of all players (shorthand):\n\n")
    # for item in shortDatePlayerBirthdayList:
        # print("Player's Birthday (shorthand) = " + item)
    # print("\n\nNow going through birthdays of all players (longhand):\n\n")
    # for item in longDatePlayerBirthdayList:
        # print("Player's Birthday (longhand) = " + item)
    playerHometownList = soup.find_all("td", class_="hometown-col")
    # print("\n\nNow going through hometowns of all players:\n\n")
    # for item in playerHometownList:
        # print("Player's Hometown = " + str(item.text))

    # Available Lists of Data:
    # for firstName, lastName, playerNumber, shootingHand, playerHeight, playerWeight, shortDatePlayerBirthday, longDatePlayerBirthday, playerHometown in zip(firstNameList, lastNameList, playerNumberList, shootingHandList, playerHeightLIst, playerWeightLIst, shortDatePlayerBirthdayList, longDatePlayerBirthdayLIst, playerHometownList):
    playerList = []

    keyList = []

    for (f, l) in zip(firstNameList, lastNameList):
        newPlayer = Player()
        newPlayer.firstName = firstNameList[firstNameList.index(f)].text
        newPlayer.lastName = lastNameList[firstNameList.index(f)].text
        newPlayer.playerNumber = playerNumberList[firstNameList.index(f)].text
        newPlayer.shootingHand = shootingHandList[firstNameList.index(f)].text
        newPlayer.playerHeight = playerHeightList[firstNameList.index(f)].text
        newPlayer.playerWeight = playerWeightList[firstNameList.index(f)].text
        newPlayer.playerShortDateBirthday = shortDatePlayerBirthdayList[firstNameList.index(f)]
        newPlayer.playerLongDateBirthday = longDatePlayerBirthdayList[firstNameList.index(f)]
        newPlayer.playerHometown = playerHometownList[firstNameList.index(f)].text
        key = str(newPlayer.firstName + " " + newPlayer.lastName)
        playerList.append(newPlayer)
        keyList.append(key)

    # print("\n\nNow going through playerList Object List\n\n")
    # for item in playerList:
        # print("Player Object = " + str(item))
        # print("Player's First Name = " + str(item.firstName))
        # print("Player's Last Name = " + str(item.lastName))
        # print("Player's Player Number = " + str(item.playerNumber))
        # print("Player's Shooting Hand = " + str(item.shootingHand))
        # print("Player's Height = " + str(item.playerHeight))
        # print("Player's Weight = " + str(item.playerWeight))
        # print("Player's Birthday (Short Date) = " + str(item.playerShortDateBirthday))
        # print("Player's Birthday (Long Date) = " + str(item.playerLongDateBirthday))
        # print("Player's Hometown = " + str(item.playerHometown))

    playerListDictionary = dict(zip(keyList, playerList))

    return playerListDictionary

def hockeyReferenceStatScrape(hockeyTeamName):
    r = requests.get("https://www.hockey-reference.com/teams/")

    soup = BeautifulSoup(r.text, "html.parser")

    activeTeamTable = soup.find("div", {"id":"div_active_franchises"})

    teamLinks = activeTeamTable.find_all("a")

    hockeyReferenceTeamWebsites = []

    hockeyReferenceTeamNames = []

    for item in teamLinks:
        # print("\nitem = " + str(item["href"]))
        fullLink = "https://www.hockey-reference.com" + str(item["href"])
        hockeyReferenceTeamWebsites.append(fullLink)
        hockeyReferenceTeamNames.append(item.text)

    # print("\n\nNow Cycling Through Hockey Reference Team Websites List: ")

    # for item in hockeyReferenceTeamWebsites:
        # print("\n\nitem = " + item)

    # print("\n\nNow Cycling Through Hockey Team Names From Hockey Reference Website: ")
    # for item in hockeyReferenceTeamNames:
        # print("\n\nitem = " + item)

    linkDictionary = dict(zip(hockeyReferenceTeamNames, hockeyReferenceTeamWebsites))

    # print("\n\nNow cycling linkDictionary: ")

    # print(linkDictionary)

    # print("\n\nNow attempting to index into linkDictionary using hockeyTeamName: ")

    # print("linkDictionary[hockeyTeamName] = " + linkDictionary[hockeyTeamName])

    # print(repr(linkDictionary))

    # print(linkDictionary)

    print('hockeyTeamName = ' + str(hockeyTeamName))

    print('linkDictionary[hockeyTeamName] = ' + str(linkDictionary[hockeyTeamName]))

    r = requests.get(linkDictionary[hockeyTeamName])

    soup = BeautifulSoup(r.text, "html.parser")

    # print("\n\nNow printing user's requested Hockey-Reference Website:")

    # print(soup)

    teamTable = soup.find("div", {"class": "overthrow table_container"})

    tHead = teamTable.find("thead")

    tableHeaders = tHead.find_all("th")

    # print("\n\nNow going through contents in tableHeaders:")

    # for item in tableHeaders:
        # print("\n\nitem = " + str(item))

    tableHeaderList = []

    for item in tableHeaders:
        tableHeaderList.append(item)

    seasonHeaders = soup.find_all("th", {"data-stat":"season"})

    seasonHeaderLinks = []

    seasonHeaderData = []

    for item in seasonHeaders:
        seasonHeaderLinks.append("https://www.hockey-reference.com" + str(item.find_next("a")["href"]))
        seasonHeaderData.append(item.find_next("a").text)

    # print("\n\n***NOW GOING THROUGH seasonHeaderLinks:")

    # for item in seasonHeaderLinks:
        # print("\n\nitem = " + str(item))

    # print("\n\n***NOW GOING THROUGH seasonHeaderData:")

    # for item in seasonHeaderData:
        # print("\n\nitem = " + str(item))

    # Pop first value for seasonHeaderLinks and seasonHeaderData to fix
    # length of list issue:

    seasonHeaderLinks.pop(0)

    seasonHeaderData.pop(0)

    leagueTDs = soup.find_all("td", {"data-stat": "lg_id"})

    leagueTDsLinks = []

    for item in leagueTDs:
        leagueTDsLinks.append("https://www.hockey-reference.com" + str(item.find_next("a")["href"]))

    # print("\n\n***NOW GOING THROUGH leagueTDsLinks:")

    # for item in leagueTDsLinks:
        # print("\n\nitem = " + item)

    tBody = teamTable.find("tbody")

    tableRows = tBody.find_all("tr")

    # print("\n\nNow going through all rows in tableRows:")

    # for item in tableRows:
        # print("\n\nitem = " + str(item))

    gamesPlayedTags = soup.find_all("td", {"data-stat": "games"})

    gamesPlayedData = []

    for item in gamesPlayedTags:
        gamesPlayedData.append(item.text)

    # print("\n\nNow going through all data points in gamesPlayedData:")

    # for item in gamesPlayedData:
        # print("\n\nitem = " + item)

    gamesWonTags = soup.find_all("td", {"data-stat": "wins"})

    gamesWonData = []

    for item in gamesWonTags:
        gamesWonData.append(item.text)

    # print("\n\nNow going through all data points in gamesWonData:")

    # for item in gamesWonData:
        # print("\n\nitem = " + item)

    gamesLostTags = soup.find_all("td", {"data-stat": "losses"})

    gamesLostData = []

    for item in gamesLostTags:
        gamesLostData.append(item.text)

    # print("\n\nNow going through all data points in gamesLostData:")

    # for item in gamesLostData:
        # print("\n\nitem = " + item)

    gamesTiedTags = soup.find_all("td", {"data-stat": "ties"})

    gamesTiedData = []

    for item in gamesTiedTags:
        gamesTiedData.append(item.text)

    # print("\n\nNow going through all data points in gamesTiedData:")

    # for item in gamesTiedData:
        # print("\n\nitem = " + item)

    gamesLostAtOvertimeTags = soup.find_all("td", {"data-stat": "losses_ot"})

    gamesLostAtOvertimeData = []

    for item in gamesLostAtOvertimeTags:
        gamesLostAtOvertimeData.append(item.text)

    # print("\n\nNow going through all data points in gamesLostAtOvertimeData:")

    # for item in gamesLostAtOvertimeData:
        # print("\n\nitem = " + item)

    seasonPointsTags = soup.find_all("td", {"data-stat": "points"})

    seasonPointsData = []

    for item in seasonPointsTags:
        seasonPointsData.append(item.text)

    # print("\n\nNow going through all data points in seasonPointsData:")

    # for item in seasonPointsData:
        # print("\n\nitem = " + item)

    seasonPointsPercentageTags = soup.find_all("td", {"data-stat": "points_pct"})

    seasonPointsPercentageData = []

    for item in seasonPointsPercentageTags:
        seasonPointsPercentageData.append(item.text)

    # print("\n\nNow going through all data points in seasonPointsPercentageData:")

    # for item in seasonPointsPercentageData:
        # print("\n\nitem = " + item)

    simpleRatingSystemTags = soup.find_all("td", {"data-stat": "srs"})

    simpleRatingSystemData = []

    for item in simpleRatingSystemTags:
        simpleRatingSystemData.append(item.text)

    # print("\n\nNow going through all data points in simpleRatingSystemData:")

    # for item in simpleRatingSystemData:
        # print("\n\nitem = " + item)

    teamRankTags = soup.find_all("td", {"data-stat": "rank_team"})

    teamRankData = []

    for item in teamRankTags:
        teamRankData.append(item.text)

    # print("\n\nNow going through all data points in teamRankData:")
    # for item in teamRankData:
    # print("\n\nitem = " + item)

    playoffsTeamRankTags = soup.find_all("td", {"data-stat": "rank_team_playoffs"})

    playoffsTeamRankData = []

    for item in playoffsTeamRankTags:
        playoffsTeamRankData.append(item.text)

    # print("\n\nNow going through all data points in playoffsTeamRankData:")

    # for item in playoffsTeamRankData:
        # print("\n\nitem = " + item)

    coachesTags = soup.find_all("td", {"data-stat": "coaches"})

    coachesLinks = []

    coachesData = []

    for item in coachesTags:
        coachesLinks.append("https://www.hockey-reference.com" + str(item.find_next("a")["href"]))
        coachesData.append(item.text)

    # print("\n\nNow going through all coachesLinks:")

    # for item in coachesLinks:
        # print("\n\nitem = " + item)

    # print("\n\nNow going through all data points in coachesData:")

    # for item in coachesData:
        # print("\n\nitem = " + item)

    seasonDataKeyList = []

    seasonDataList = []

    seasonDataKeyList = seasonHeaderData

    # print("\n\nNow Cycling Through seasonDataKeyList: ")

    # for item in seasonDataKeyList:
        # print("\n\nitem = " + str(item))

    for item in seasonDataKeyList:
        newSeason = HockeyReferenceSeasonData()
        newSeason.seasonName = seasonHeaderData[seasonDataKeyList.index(item)]
        newSeason.gamesPlayed = gamesPlayedData[seasonDataKeyList.index(item)]
        newSeason.gamesWon = gamesWonData[seasonDataKeyList.index(item)]
        newSeason.gamesLost = gamesLostData[seasonDataKeyList.index(item)]
        newSeason.gamesTied = gamesTiedData[seasonDataKeyList.index(item)]
        newSeason.gamesLostAtOvertime = gamesLostAtOvertimeData[seasonDataKeyList.index(item)]
        newSeason.seasonPoints = seasonPointsData[seasonDataKeyList.index(item)]
        newSeason.seasonPointsPercentage = seasonPointsPercentageData[seasonDataKeyList.index(item)]
        newSeason.simpleRating = simpleRatingSystemData[seasonDataKeyList.index(item)]
        newSeason.teamRank = teamRankData[seasonDataKeyList.index(item)]
        newSeason.playoffsTeamRank = playoffsTeamRankData[seasonDataKeyList.index(item)]
        newSeason.coach = coachesData[seasonDataKeyList.index(item)]
        newSeason.coachLink = coachesLinks[seasonDataKeyList.index(item)]
        newSeason.teamSeasonLink = seasonHeaderLinks[seasonDataKeyList.index(item)]
        newSeason.leagueSeasonLink = leagueTDsLinks[seasonDataKeyList.index(item)]
        seasonDataList.append(newSeason)

    # print("\n\nNow Cycling Through SeasonDataList: ")

    # for item in seasonDataList:
        # print("\n\nitem = " + str(item))
        # print("\n\nitem.seasonName = " + str(item.seasonName))
        # print("\n\nitem.teamSeasonLink = " + str(item.teamSeasonLink))
        # print("\n\nitem.leagueSeasonLink = " + str(item.leagueSeasonLink))
        # print("\n\nitem.gamesPlayed = " + str(item.gamesPlayed))
        # print("\n\nitem.gamesWon = " + str(item.gamesWon))
        # print("\n\nitem.gamesLost = " + str(item.gamesLost))
        # print("\n\nitem.gamesTied = " + str(item.gamesTied))
        # print("\n\nitem.gamesLostAtOvertime = " + str(item.gamesLostAtOvertime))
        # print("\n\nitem.seasonPoints = " + str(item.seasonPoints))
        # print("\n\nitem.seasonPointsPercentage = " + str(item.seasonPointsPercentage))
        # print("\n\nitem.simpleRating = " + str(item.simpleRating))
        # print("\n\nitem.teamRank = " + str(item.teamRank))
        # print("\n\nitem.playoffsTeamRank = " + str(item.playoffsTeamRank))
        # print("\n\nitem.coach = " + str(item.coach))
        # print("\n\nitem.coachLink = " + str(item.coachLink))

    # print("\n\ntype() for seasonDataKeyList: " + str(type(seasonDataKeyList)))

    # print("\n\n\ntype() for seasonDataList: " + str(type(seasonDataList)))

    # dictionary = dict(zip(objectKeyList, seasonDataList))

    # dictionary = dict(zip(seasonDataKeyList, seasonDataList))
    # print("\n\nNow going through dictionary that contains seasons and related data:")
    # print(seasonDataList)

    # return seasonDataList

    seasonDataDictionary = dict(zip(seasonDataKeyList, seasonDataList))

    return seasonDataDictionary

    # Data Present:
    # website = linkDictionary[hockeyTeamName]
    # seasonHeaderLinks, seasonHeaderData
    # leagueTDs, leagueTDsLinks
    # gamesPlayedData
    # gamesWonData
    # gamesLostData
    # gamesTiedData
    # gamesLostAtOvertimeData
    # seasonPointsData
    # seasonPointsPercentageData
    # simpleRatingSystemData
    # teamRankData
    # playoffsTeamRankData

def createExcelFileAndTwitterPost(hockeyTeamName, playerListDictionary, seasonDataDictionary):
    # print("\n\nNow going through playerlist Dictionary:")

    # Use "in enumerate("dictionary".items()) to cycle through dictionary data

    # i = index, k = key, v = value
    # for i, (k, v) in enumerate(playerListDictionary.items()):
        # print("index: {} key: {} value: {}".format(i, k, v.firstName))

    # print("\n\nNow Going Through seasonData Dictionary: ")

    # for i, (k, v) in enumerate(seasonDataDictionary.items()):
        # print("index: {} key: {} value: {}".format(i, k, v.seasonName))

    workbookName = 'hockeywebscraperdata/' + str(hockeyTeamName).replace(' ', '') + "Data.xlsx"
    
    # workbookName = str(hockeyTeamName + " Data.xlsx")

    # workbook = xlsxwriter.Workbook(str(hockeyTeamName) + " Data.xlsx")

    workbook = xlsxwriter.Workbook(workbookName)

    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    italic = workbook.add_format({'italic': True})

    boldItalic = workbook.add_format({'bold': True, 'italic': True})

    leftAlign = workbook.add_format({'align': "left"})

    rightAlign = workbook.add_format({'align': "right"})

    worksheet.write(0,0, str(hockeyTeamName + " Data"), bold)

    # worksheet.write(row, column, data)
    worksheet.write(2, 0, "Current Player Data (NHL.com)", boldItalic)
    worksheet.write(3, 1, "Name", bold)
    worksheet.write(3, 2, "Player Number", bold)
    worksheet.write(3, 3, "Shooting Hand", bold)
    worksheet.write(3, 4, "Player Height", bold)
    worksheet.write(3, 5, "Player Weight", bold)
    worksheet.write(3, 6, "Player Short Date Birthday", bold)
    worksheet.write(3, 7, "Player Long Date Birthday", bold)
    worksheet.write(3, 8, "Player Hometown", bold)

    x = 4

    for i, (k, v) in enumerate(playerListDictionary.items()):
        worksheet.write(x, 1, str(v.firstName + " " + v.lastName), leftAlign)
        worksheet.write(x, 2, v.playerNumber, rightAlign)
        worksheet.write(x, 3, v.shootingHand, rightAlign)
        worksheet.write(x, 4, v.playerHeight, rightAlign)
        worksheet.write(x, 5, v.playerWeight, rightAlign)
        worksheet.write(x, 6, v.playerShortDateBirthday, rightAlign)
        worksheet.write(x, 7, v.playerLongDateBirthday, rightAlign)
        worksheet.write(x, 8, v.playerHometown, rightAlign)

        x += 1

    teamHeaderStartRow = 5 + len(playerListDictionary)

    worksheet.write(teamHeaderStartRow, 0, "Team Data (Hockey-Reference.com)", boldItalic)

    teamDataTableHeadersRow = 6 + len(playerListDictionary)

    worksheet.write(teamDataTableHeadersRow, 1, "Season Name", bold)
    worksheet.write(teamDataTableHeadersRow, 2, "Games Played", bold)
    worksheet.write(teamDataTableHeadersRow, 3, "Games Won", bold)
    worksheet.write(teamDataTableHeadersRow, 4, "Games Lost", bold)
    worksheet.write(teamDataTableHeadersRow, 5, "Games Tied", bold)
    worksheet.write(teamDataTableHeadersRow, 6, "Games Lost At Overtime", bold)
    worksheet.write(teamDataTableHeadersRow, 7, "Season Points", bold)
    worksheet.write(teamDataTableHeadersRow, 8, "Season Points Percentage", bold)
    worksheet.write(teamDataTableHeadersRow, 9, "Simple Rating (Hockey-Reference)", bold)
    worksheet.write(teamDataTableHeadersRow, 10, "Team Rank", bold)
    worksheet.write(teamDataTableHeadersRow, 11, "Playoffs Team Rank", bold)
    worksheet.write(teamDataTableHeadersRow, 12, "Coach Name", bold)
    worksheet.write(teamDataTableHeadersRow, 13, "Coach Link", bold)
    worksheet.write(teamDataTableHeadersRow, 14, "Team Season Link", bold)
    worksheet.write(teamDataTableHeadersRow, 15, "NHL League Season Link", bold)

    x = 7 + len(playerListDictionary)

    for i, (k, v) in enumerate(seasonDataDictionary.items()):
        worksheet.write(x, 1, v.seasonName, leftAlign)
        worksheet.write(x, 2, v.gamesPlayed, rightAlign)
        worksheet.write(x, 3, v.gamesWon, rightAlign)
        worksheet.write(x, 4, v.gamesLost, rightAlign)
        worksheet.write(x, 5, v.gamesTied, rightAlign)
        worksheet.write(x, 6, v.gamesLostAtOvertime, rightAlign)
        worksheet.write(x, 7, v.seasonPoints, rightAlign)
        worksheet.write(x, 8, v.seasonPointsPercentage, rightAlign)
        worksheet.write(x, 9, v.simpleRating, rightAlign)
        worksheet.write(x, 10, v.teamRank, rightAlign)
        worksheet.write(x, 11, v.playoffsTeamRank, rightAlign)
        worksheet.write(x, 12, v.coach, rightAlign)
        worksheet.write(x, 13, v.coachLink, rightAlign)
        worksheet.write(x, 14, v.teamSeasonLink, rightAlign)
        worksheet.write(x, 15, v.leagueSeasonLink, rightAlign)

        x += 1

    # Set column widths based on cell content:
    worksheet.set_column(1, 1, 25)
    worksheet.set_column(2, 2, 25)
    worksheet.set_column(3, 3, 25)
    worksheet.set_column(4, 4, 25)
    worksheet.set_column(5, 5, 25)
    worksheet.set_column(6, 6, 25)
    worksheet.set_column(7, 7, 25)
    worksheet.set_column(8, 8, 25)
    worksheet.set_column(9, 9, 25)
    worksheet.set_column(10, 10, 25)
    worksheet.set_column(11, 11, 40)
    worksheet.set_column(12, 12, 40)
    worksheet.set_column(13, 13, 50)
    worksheet.set_column(14, 14, 50)
    worksheet.set_column(15, 15, 50)

    workbook.close()
    
    # print("\n\n.xlsx Excel file saved successfully. Goodbye!\n\n")
    
    return workbookName


def postToTwitter(hockeyTeamName, workbookName):
  # Post To Twitter Using Python-Twitter
    
  api = twitter.Api(
          consumer_key="",
          consumer_secret="",
          access_token_key="",
          access_token_secret=""
  )
 
  print('hockeyTeamName = ' + str(hockeyTeamName))

  logoPath = 'hockeywebscraperdata/logos/' + hockeyTeamName + ' Logos.gif'

  print('logoPath = ' + str(logoPath))

  status = api.PostUpdate("Here is the Excel .xlsx data for the " + str(hockeyTeamName) + "! Feel free to download it for your own use! " + "Link: musimatic.net/pythonprojectwebsites/HockeyWebscraper/" + str(workbookName), media=logoPath)

hockeyTeamDictionary = NHLTeamNameScrape()

modifiedHockeyTeamDictionary = changeMontrealTeamName(hockeyTeamDictionary)

displayDictionaryValues(modifiedHockeyTeamDictionary)

# hockeyTeamName = askHockeyTeamName()

# print(repr(hockeyTeamName))

hockeyTeamName = chooseRandomTeam(modifiedHockeyTeamDictionary)

playerListDictionary = NHLTeamRosterSearch(modifiedHockeyTeamDictionary, hockeyTeamName)

seasonDataDictionary = hockeyReferenceStatScrape(hockeyTeamName)

workbookName = createExcelFileAndTwitterPost(hockeyTeamName, playerListDictionary, seasonDataDictionary)

postToTwitter(hockeyTeamName, workbookName)
