from urllib.request import urlopen
import threading

print("This Python script was created by @techmariah (Mariah Rucker)")

def checkPlayer():
	threading.Timer(2, checkPlayer).start()
	url = "http://www.espn.com/"
	char = urlopen(url).read(20000) 
	characters = char.split()
	
	if "Steph Curry" in characters:
		print("The GOAT has been found!")
	else:
		print("Where is Steph Curry aka the GOAT?!")
		
checkPlayer()
