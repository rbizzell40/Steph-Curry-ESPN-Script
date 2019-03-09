"""
This is a Python script that checks ESPN.com website for updates on Steph Curry
"""

# urlopen fetches the ESPN.com url
from urllib.request import urlopen
# threading is for the timer 
import threading

# Created by
print("This Python script was created by @techmariah (Mariah Rucker)")

# wtart the timer to check ESPN.com website
def checkPlayer():
	# timer initiated for every 30 seconds 
	threading.Timer(2, checkPlayer).start()
	# define the page to check for Steph Curry mentions 
	url = "http://www.espn.com/"
	# call urlopen to read ESPN.com
	# read property to limit number of characters
	char = urlopen(url).read(20000) # set to check 20000 characters only 
	# insert the characters into a list 
	characters = char.split()

	# compare each word in the list to "Steph Curry"
	if "Steph Curry" in characters:
		print("The GOAT has been found!")
	else:
		print("Where is Steph Curry aka the GOAT?!")

# Run the checkPlayer function 
checkPlayer()
