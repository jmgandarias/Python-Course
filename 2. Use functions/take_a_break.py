'''
Take a Break program

First program from the introductory to python course
developed by Juanma Gandarias
25/07/2017
'''
import time
import webbrowser

breaks = 0
total_breaks = 3
while(breaks<total_breaks):
	#Wait for ten seconds
	time.sleep(1)

	#Open a browser
	webbrowser.open("http://www.taislab.uma.es")
	breaks = breaks + 1

