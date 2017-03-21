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
	tutorList=database.tutorList
	outputList = []
	for entry in tutorList:
		temp = "	Name: " + tutorList[entry]["name"] + " " + tutorList[entry]["surname"]
		outputList.append(temp)
	for entry in outputList:
		print(entry)
	takeAction = True
	while takeAction:
		print("\n	Add Tutor 		Remove Tutor 			Return to Menu")
		action = tms.userInput("")	
		if action.lower()=="add tutor":
			print("What will be the new tutor's ID: ")
			tutorID=tms.userInput("")
			print("And their first name: ")
			name=tms.userInput("")
			name=name[0].capitalize()+name[1:]
			print("And their surname: ")
			surname=tms.userInput("")
			surname=surname[0].capitalize()+surname[1:]
			print("And their e-mail: ")
			email=tms.userInput("")
			print("How many tutee's will this tutor be able to hold: ")
			size=tms.userInput("")
			print("So, \nTutor ID: "+tutorID+"\nFullname: "+name+" "+surname+"\nE-mail: "+email+" \nNumver of students for this Tutor: "+size) 
			undecided = True
			while undecided:
				print("Is that correct: yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					undecided=False
					addTutor(tutorID, name, surname, email)
					viewTutorList()
				elif response=="no":
					print("You'll be returned to the menu to try again.")
					undecided=False
				else:
					print("Please enter 'yes' or 'no'")
		elif action.lower()=="remove tutor":
			takeAction=False
			removeTutor()
		elif action.lower()=="return to menu":
			takeAction=False
			tms.admin()
		else:
			print("invalid input")

def editTutor(): #Ask for surname. Show possible options or print error message. ask user for attribute to change.
	tflag=True
	tflag2=True
	tutorList=database.tutorList
	while tflag:
		print("")
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
		tutorObj["name"] = input("Please enter the new name: ")
		print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])
	elif editChoice=="surname":
		tutorObj["surname"] = input("Please enter the new surname: ")
		print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])
	elif editChoice=="email":
		tutorObj["email"] = input("Please enter the new Email address: ")
		print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])
	elif editChoice=="group":
		tutorObj["group"] = input("Please enter the new tutor ID: ")
		print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])
	else:
		print("\n\n                          ***Please input name, surname, email or group.***\n\n")
	database.tutorList=tutorList

def tutor(): #Ask for surname. Check list of tutors for surname. Print error message if tutor not found. Print results with id, name, surname and email. User chooses result and prints its group
	print("\n                     -----------\n                        TUTOR\n                     -----------")
	name=tms.userInput("Enter your surname: ")