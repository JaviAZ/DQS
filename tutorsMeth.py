#!/usr/bin/python3
from database import *
from tuteesMeth import *
from tms import *

def genGroups(): #will create the tutor groups from dictionaries using addToGroup
	print("To be completed")

def redistGroups(): #distribute students into new groups
	print("To be completed")

def addTutor():
	print("To be completed")

def removeTutor():	#call redistGroups to redistribute group if tutor has one
	print("To be completed")

def viewTutorList():	#print tutorlist. with option to add or remove tutor (which would call respective methods)
	print("To be completed")

def editTutor():	#Ask for surname. show possible options or print error message. ask user for attribute to change. Main menu and go back option
	tflag=True
	tflag2=True
	while tflag:
		tutorSurname=userInput("Input the surname of the tutor you wish to edit: ")
		tcount=0
		for tutorKey in tutorList:
			if tutorSurname==tutorList[tutorKey]["surname"].lower():
				tcount+=1
				tflag=False
				print ("ID: "+tutorList[tutorKey]["id"]+". Name: "+tutorList[tutorKey]["name"]+". Surname: "+tutorList[tutorKey]["surname"]+". Email: "+tutorList[tutorKey]["email"])
		if tcount==0:
			print("Sorry the tutor was not found.")
		else:
			while tflag2:
				tChoice=userInput("Enter the ID of the tutor you wish to edit: ")
				if tChoice in tutorList:
					tutorObj=tutorList[tChoice]
					tflag2=False
					break
				else:
					print("That tutor isn't in the list.")
	editChoice=userInput("Do you wish to edit name, surname, email, or group?")
	if editChoice=="name":
		print("To be completed")
	elif editChoice=="surname":
		print("To be completed")
	elif editChoice=="email":
		print("To be completed")
	elif editChoice=="group":
		print("To be completed")
	else:
		print("\n\n                          ***Please input name, surname, email or group.***\n\n")

def tutor():	#Ask for surname. Check list of tutors for surname. Print error message if tutor not found. Print results with id, name, surname and email. User chooses result. Call print group method. Main menu and go back option every view.
	print("\n                     -----------\n                        TUTOR\n                     -----------")
	name=userInput("Enter your surname: ")