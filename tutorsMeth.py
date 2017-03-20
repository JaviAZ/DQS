#!/usr/bin/python3
import database
import tms

def genGroups(): #Assigns a tutor to each tutee
	tuteeList=database.tuteeList
	tutorList=database.tutorList
	tuteespertutor=len(tuteeList)//len(tutorList)
	i=0
	c=0
	for tutee in tuteeList:
		if(i==0):
			c+=1
			i=tuteespertutor
		tuteeList[tutee]["tutor"]=str(c)
		i-=1
	database.tuteeList=tuteeList

def redistGroups(tutorDelID): #Redistribute students into new groups
	print("To be completed")

def addTutor(ID,name,surname,email): #Adds tutor to tutorList
	database.tutorList[ID]={"id":ID, "name":name, "surname":surname, "email":email}

def removeTutor(): #Call redistGroups to redistribute group if tutor has one, delete tutor from list
	print("To be completed")

def viewTutorList(): #Print tutorlist and how many tutees each has. With option to add or remove tutor (which would call respective methods)
	print("To be completed")

def editTutor(): #Ask for surname. Show possible options or print error message. ask user for attribute to change.
	tflag=True
	tflag2=True
	tutorList=database.tutorList
	while tflag:
		tutorSurname=tms.userInput("Input the surname of the tutor you wish to edit: ")
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
				tChoice=tms.userInput("Enter the ID of the tutor you wish to edit: ")
				if tChoice in tutorList:
					tutorObj=tutorList[tChoice]
					tflag2=False
					break
				else:
					print("That tutor isn't in the list.")
	editChoice=tms.userInput("Do you wish to edit name, surname, email, or group? ")
	if editChoice=="name":
		tutorObj["name"] = tms.userInput("Please enter the new name: ")
		print(tutorObj)
	elif editChoice=="surname":
		print("To be completed")
	elif editChoice=="email":
		print("To be completed")
	elif editChoice=="group":
		print("To be completed")
	else:
		print("\n\n                          ***Please input name, surname, email or group.***\n\n")
	database.tutorList=tutorList

def tutor(): #Ask for surname. Check list of tutors for surname. Print error message if tutor not found. Print results with id, name, surname and email. User chooses result and prints its group
	print("\n                     -----------\n                        TUTOR\n                     -----------")
	name=tms.userInput("Enter your surname: ")