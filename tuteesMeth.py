#!/usr/bin/python3
from database import *
from tutorsMeth import *
from tms import *

def addTutee():	#will call addToGroup if method isnt called from createProgram
	print("To be completed")

def removeTutee(): #remove from tutor group too 
	print("To be completed")

def addToGroup():	#function to add tutee to group
	print("To be completed")

def viewTutorGroup():	#Print tutorgroup depending on tutor
	print("To be completed")

def viewTuteeList(): #print tuteeList with option to add or remove tutees (which would call respective methods)
	print("To be completed")

def editTutee(): #ask for tutee surname. show possible options or print error message. ask user for attribute to change. Main menu and go back option
	sflag=True
	sflag2=True
	while sflag:
		tuteeSurname=userInput("Input the surname of the tutee you wish to edit: ")
		scount=0
		for tuteeKey in tuteeList:
			if tuteeSurname==tuteeList[tuteeKey]["surname"].lower():
				scount+=1
				sflag=False
				print ("Student number: "+tuteeList[tuteeKey]["tuteeNo"]+". Name: "+tuteeList[tuteeKey]["name"]+". Surname: "+tuteeList[tuteeKey]["surname"]+". Email: "+tuteeList[tuteeKey]["email"])
		if tcount==0:
			print("Sorry the tutee was not found.")
		else:
			while sflag2:
				Choice=userInput("Enter the student number of the tutee you wish to edit: ")
				if sChoice in tuteeList:
					tuteeObj=tuteeList[sChoice]
					sflag2=False
					break
				else:
					print("That student isn't in the list.")

def tutee():	#Ask for tutee number. Print error message if tutee not found. Ask if he wants to view tutor group info (Call print group method), enrolled courses (print list of enrolled courses of tutee) or tutor info (call view tutor). Main menu and go back option every view.
	print("\n                     -----------\n                       STUDENT\n                     -----------")
	number=userInput("Enter your student number: ")
