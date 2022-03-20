# Song Of The Web: A Python WebScraper

# Documentation for Music21 Library:
# http://web.mit.edu/music21/doc/usersGuide/usersGuide_04_stream1.html#usersguide-04-stream1

# Update (4-5-2018):
# That tutorial from New Mexico Tech, after looking through and actually trying it out,
# made me think that the entire approach of trying to learn a GUI type application with Tkinter wouldn't
# be worth it for this program

# At this point, I will see if I can just package this together

# In terms of packaging, I tried researching, and eventually found PyInstaller to be good, but even that didn't automatically
# download all the modules needed for this script, aka music21, requests, bs4

# I settled by including everything into a single webscraperSearch() function
# and then calling it at the bottom of the program

# Project Is Finished. This successfully converts a Bing search into a midi song for the user, and I feel that is the cool final goal in the first place

# I learned in all honesty, that since I learn more from doing projects, it is better to keep the realistic newbie programmer goals in mind, than trying
# to learn absolutely complex things like Tkinter, or even how to package programs with PyInstaller, since I'm just not on that level, and am more interested
# in just webscraping, and automation using Python. I had a lot of fun, and the end result was awesome ^_^

# Update (4-4-2018):
# Teaching myself tkinter so I just add terminal commands as actual buttons on a GUI form,
# which would make this look a lot nicer, and be able to be packaged into its own distributable
# program

# Update (3-28-2018):
# Success, this totally works! I rethought the project, and created a chordStream
# object to gather chords at the same time as the noteStream, and then
# gave the user the option to either pick a note/rests based song,
# or a chord/rests based song. I then added more inputs at the end to
# ask the user what extension they prefer, and so far it works!

# Some more things to do:
# Check the notes of major and minor chords (had a couple of minor based songs
# that sounded off in some chords)
# Reference for Chords:
# http://www.michael-thomas.com/music/class/chords_notesinchords.htm
# Add PyQT to this project
# Package this project without the need of a Python shell for any user

# Update (3-27-2018):
# So far, so good. I reworked a lot of the code to be more manageable
# and not to depend on the pretty badly applicable examples from the
# documentation. I decided to literally use the idea of a note stream
# and run with it, but also include backing chords for each instance that a
# note is found. This is contained in an array of chords, and then played for
# user.

# I would like to add both of these items to scores separately, and merge
# them so they play together in a crazy fashion

# Then, I'd like to finish the .midi annoying export issue of having to
# specify the extension at the last step

# Next, I want to use PyQT via their documentation to give this an overall
# overhaul in terms of GUI

# Finally, I want to package this into a single EXE without having the need
# for having a Python interpreter

# Update (3-23-2018):
# Followed the documentation to apply the .chordify() method but this only replicates
# the note stream of single notes, EVEN AFTER all of that hassle to create a Score
# object. This is a bit frustrating, but once I am done finalizing this score object,
# I will be able to use the other examples found in the documentation to good use
# and then only have to apply PyQT to this project, and then repackage for
# future users without Python

# Update (3-16-2018):
# After being sick for a week due to a hernia, I re-analyzed my time during
# the week, and realized I can do music (guitar and synth) on the weekend
# and work on Python Stackskills course videos for 1 hour every day after work
# and still make time on Fridays specifically for cool projects like this.

# I looked over the code again to get a feel of this project, and felt I needed
# to literally do an example to get myself in the mindset of the documentation
# team on how they would create a score, using "Recursion In Streams":
# http://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html

# From this example, I decided to simplify the code, and took out the need
# of using an index variable, i, to loop through it, and just to add a rest
# to a note stream object if a random number was equal to 3, and to add a note
# if it was NOT equal to 3. I then applied the same ideas of creating a score
# to the final note stream object, and as far as what I can tell in the
# Python console, it totally works! Plus, the rests work like they're supposed to

# Now that I have a nice score object, I want to apply the .chordify() method
# next week, and also still have the following goals:

# Use py.qt to make it look cool on its own, and package this into its own
# program without the need of a Python 3 interpreter

# Update (2-18-2018):
# I tried adding a random seed via rand.randrange(2, 4) to ulimately
# spit out a value of 3, which would be the trigger for adding a rest
# in the portion where individual musical notes are added.

# Because of my lack of understanding on how scores are made in this library
# since its not too easy to do so, I did some digging in the documentation
# and found the section on recursive to be more insightful of how to
# create a score object, than the actual section itself:

# http://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html

# This section goes into detail on creating a score, creating a measure,
# creating a part, adding the measure to the part, and adding the part to the
# score

# I did this in my code, and am only receiving a MIDI file of a single chord
# being played for some reason, so this might be a fault with the if statements
# that only a certain condition is allowing one single note / chord to be
# added.

# I've kept the noteStream object to keep the actual project working

# Future Goals: Get this actually working with the Score object itself,
# add UI with PyQT library, add a score details section that describes
# the chord progression, timing of the piece, and other info, and package
# this into an .exe that anyone WITHOUT Python can even use

# Update (2-9-2018):
# I received a comment from one of the creators of this library on their Music21 Google+ page
# and he told me that I shouldn't include keywords of actual objects of this library,
# Ex: Don't use the variable name, note, because it might conflict with library based methods
# I fixed this issue, removed the need of a "noteList" and appended the notes directly to the stream
# in the main webscraping loop. I then followed the documentation's method of creating a score object
# with "parts" and "rests", so that I can later apply the .chordify() method to create some cool harmonies
# from this data, and really create a song with melody lines as well.

# Future Goals: Implement the odd vs. even idea on the For loop to either add notes or rests based on the index
# position to make the song a bit random, OR, maybe use the Random Python library to choose a number from the entire
# length of the list to randomly add a rest object to it. Otherwise, if you just use the odd or even value
# of the For loop, its just going to be a boring song of notes followed by rests with no variation.

# Update (2-1-2018):
# After trying to incorporate the score object into the program, I tried literally copying the documentation
# example verbatim into the project, and still received an error. I posted a question regarding why this is happening:
# https://groups.google.com/forum/#!forum/music21list

# Update (1-25-2018):
# I did the from music21 import *" command at the top of the program, and fixed
# all references to the music21 library to not include "music21." since now this program
# imports all classes and methods found in this library. It now works like before, and
# doing this process made me understand more about the importance of importing statements

# Future Goals: Duplicate the notes into a "note form" and a "chord form" so that
# you can later add melody lines in addition to a chordal progression that makes sense
# because I don't want it to just play chords since that's boring. Also, I would love to
# actually use PyQt library to make this into a nice GUI menu so that you don't have to run
# this program just in browser either, and one day, it would be packaged into its own .exe
# without the need of running Python in an IDE.

# Update (1-18-2018):
# I tried adding the .chordify() method, but it turns out that the stream
# needs to have the .Score() method called on it before being passed to the
# .chordify function, otherwise the .chordify() function will return nothing

# My current goal just to avoid all this importing confusion, literally,
# just follow the "import all" type idea in the beginning of the documentation
# to avoid the confusion behind music21.(method).(submethod) since this
# is becoming more confusing than it needs to be

# Continue with Chordifying the notes:
# http://web.mit.edu/music21/doc/usersGuide/usersGuide_09_chordify.html#usersguide-09-chordify

# Update (1-10-2018):
# I got it to write to MIDI after skipping directly to Chapter 8 in the documentation
# and then figuring out how to write to file
# I also allowed the feature to have the user enter the name of the MIDI file in the console
# but also added the note to also add the appropriate extension because this doesn't
# automatically add this
# Goal: Chordify the sequence, and try the actual import all modules using the
# asterisk * based command, and modifying the commands that use "music21" below to
# make it work

# Update (1-3-2018):
# Success! I got it to play the entire song by appending all of the notes in the notesList
# to a 'Stream' object, which holds all of this data together
# I then played it via the .show('midi') command
# Next goal: write it to a Midi object, and save it to the disk, and possibly force it to
# play chords of each of the notes in major, or minor, as specified by the user, OR
# purely based on music theory to just use known progressions:
# ex: I, IV, V chord progression

# Update (12-28-2017):
# Installed Music21 Python library which is a MIT based Python library
# that parses through and plays MIDI data

# I did this through pip3 installer:
# Path for Pip:
# C:\Users\Sam\AppData\Local\Programs\Python\Python36-32\Scripts
# Then, in the terminal: pip3 install (whatever module you want)

# I also had to install "matplotlib", "numpy", and "scipy" because the Music21 library asked for it

# I was FINALLY able to play a note through MIDI
# This was done by assigning correct note values
# for each of the converted notes

# The next goal would be to add all of the notes
# to a MIDI file and then play it as well

# Update (12-18-2017):
# With the use of an if statement example on Stack Overflow, I realized it would better to iterate
# through a list of choices in the if statement, rather than having a ton of 'and' statements
# to check through each of the domain name's first characters
# I then added a global noteList array that holds all of these individual notes
# The next goal would be to actually have a Python MIDI library just play the notes in succession as a start

# Update (12-12-2017):
# I finally read up on the Python documentation on how to use the .split() function, and was able to rip the web links
# This was based on looking to see if the link contained 'http'
# Then, I looked to see if it also contained a 'www' since I want the domain name right after the 'www.'
# Then, I ripped the first character of the domain name as the unconverted MIDI note I want to play
# Future goals: Look up a good MIDI library for Python and just play the note to begin with as a starting goal

# Update (12-7-2017y)
# I finally got the href attributes to be ripped from the links using the for loops
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Overall Project Goal: Scrape a website to find top 10 visited websites on a given day
# Take the first letter character from the name of the website right after the period, "google.com"
# Then create a note sequence that plays in 4/4 time signature using a midi engine in Python
# Later, create a chord from these notes that plays in 4/4 time signature using a midi engine in Python
# Since there are 27 letters in the alphabet, and only 7 musical letters to choose from, assign letters from G onward in a pre-determined sequence from A to G again

# Resources:
# https://wiki.python.org/moin/PythonInMusic
# https://www.youtube.com/watch?v=vb9c_WFMYeI

# Breakdown of imports:
# Requests is used to ping the website with the search parameters
import requests
# BeautifulSoup is used to parse through web data
from bs4 import BeautifulSoup
from music21 import *
import random

# Webscraper:
def webscraperSearch():
	search = input("Enter your search query into Bing: ")
	params = {"q": search}
	r = requests.get("http://www.bing.com", params=params)

	# Make BeautifulSoup
	soup = BeautifulSoup(r.text, "html.parser")

	# Find all <a> HTML links
	# Look for thumbnail links
	# links = soup.findAll("a", {"class": "thumb"} )

	aElements = soup.findAll("a")

	# Print website text:
	# print("Website Text:", r.text)

	print("\n\n\n")

	# Pitch Classes Of Notes:
	# C=0, C#/Db=1, D=2,
	# D#/Eb=3, E=4, F=5,
	# F#/Gb=6, G=7, G#/Ab=8,
	# A=9, A#/Bb=10, B=11

	# Create a 'Stream' object from the stream module in the Music21 library to append notes to:
	noteStream = stream.Stream()

	# Create a chord Stream.stream() object:
	chordStream = stream.Stream()

	# Ask the user if they prefer major or minor chords:
	chordType = int(input("What kind of chords do you prefer? Major or Minor? Press '1' for Major chords, or press '2' for Minor chords:"))

	for aElement in aElements:
		randomNumber = random.randrange(2, 4)
		print("Link:", aElement)
		WebLink = str(aElement.get('href'))
		print("Href:", WebLink)
		# Make sure link contains "http"
		if WebLink.find("http") == -1:
			print("Not a valid URL")
			print("\n")
		else:
			firstPart, secondPart = WebLink.split("//")
			print("firstPart =", firstPart)
			print("secondPart =", secondPart)
			# Make sure link contains "www"
			if secondPart.find("www") == -1:
				print("Does not contain World Wide Web")
				print("\n\n")
			else:
				wordList = secondPart.split(".", -1)
				domainName = wordList[1]
				print("domainName =", str(domainName))
				firstDomainCharacter = domainName[0]
				print("firstDomainCharacter =", firstDomainCharacter)
				# Setup Notes:
				aNote = note.Note("A9", type="quarter")
				bNote = note.Note("B11", type="quarter")
				cNote = note.Note("C0", type="quarter")
				dNote = note.Note("D2", type="quarter")
				eNote = note.Note("E4", type="quarter")
				fNote = note.Note("F5", type="quarter")
				gNote = note.Note("G7", type="quarter")
				r = note.Rest(id="rest", type="quarter")
				if firstDomainCharacter.lower() in ['a', 'h', 'o', 'v']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(aNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["a", "c#", "e"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["a", "c", "e"]))
					print("\n\n")
				elif firstDomainCharacter.lower() in ['b', 'i', 'p', 'w']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(bNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["b", "d#", "f#"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["b", "d", "f#"]))
					print("\n\n")
				elif firstDomainCharacter.lower() in ['c', 'j', 'q', 'x']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(cNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["c", "e", "g"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["c", "d#", "g"]))
					print("\n\n")
				elif firstDomainCharacter.lower() in ['d', 'k', 'r', 'y']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(dNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["d", "f#", "a"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["d", "f", "a"]))
					print("\n\n")
				elif firstDomainCharacter.lower() in ['e', 'l', 's', 'z']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(eNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["e", "g#", "b"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["e", "g", "b"]))
					print("\n\n")
				elif firstDomainCharacter.lower() in ['f', 'm', 't']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(fNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["f", "a", "c"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["f", "g#", "c"]))
					print("\n\n")
				elif firstDomainCharacter.lower() in ['g', 'n', 'u']:
					if randomNumber == 3:
						print("Adding Rest")
						print("randomNumber =", randomNumber)
						noteStream.append(r)
						chordStream.append(r)
					else:
						noteStream.append(gNote)
						if chordType == 1:
							chordStream.append(chord.Chord(["g", "b", "d"]))
						elif chordType == 2:
							chordStream.append(chord.Chord(["g", "a#", "d"]))
					print("\n\n")
	print("\n")
	print("Print Tests: ")
	print("\n")

	# chordList = []

	print("\n")
	print("Checking noteStream Items")
	print("\n")

	for item in noteStream:
		print("noteStream item = ", item)

	print("\n")
	print("Checking chordStream Items")
	print("\n")

	for item in chordStream:
		print("chordStream item = ", item)

	# Ask the user if they want to hear the song they created that contains notes with rests, or if they want to just want the chord version:
	notesOrChords = int(input("SONG CREATED!!!\n\nWould you like the version with notes/rests, or would you like the chords/rests version? Press '1' for notes/rests, or press '2' for chords/rests:"))

	if notesOrChords == 1:
		noteStream.show('midi')
		noteSongName = str(input("Type In The Name Of Your Note/Rests Based Song:"))
		noteSongFileType = str(input("Type The File Extension Type That You Want To Save Your Song In: (i.e. '.midi', '.xml') *NOTE*: Make sure you include the period sign:"))
		noteStream.write(noteSongFileType, noteSongName)
		print("\n")
		print("File Successfully Saved. Goodbye.")
		print("\n")
		# noteStream.write('midi', input("Enter The Song Name (Add File Extension, i.e. midi)"))

	elif notesOrChords == 2:
		chordStream.show('midi')
		chordSongName = str(input("Type In The Name Of Your Chord/Rests Based Song:"))
		chordSongFileType = str(input("Type The File Extension Type That You Want To Save Your Song In: (i.e. '.midi', '.xml') *NOTE*: Make sure you include the period sign:"))
		chordStream.write(chordSongFileType, chordSongName)
		print("\n")
		print("File Successfully Saved. Goodbye.")
		print("\n")

webscraperSearch();
