#!/usr/bin/python3
import database
import tms

def genGroups(): #Assigns a tutor to each tutee
	tuteespertutor=len(database.tuteeList)//len(database.tutorList)
	i=0
	c=0
	for tutee in tuteeList:
		if(i==0):
			c+=1
			i=tuteespertutor
		tuteeList[tutee]["tutor"]=str(c)
		i-=1

def redistGroups(tutorDelID): #Redistribute students into new groups
	print("To be completed")

def addTutor(ID,name,surname,email,tuteesN): #Adds tutor to tutorList
	database.tutorList[ID]={"id":ID, "name":name, "surname":surname, "email":email, "tuteesN":tuteesN}

def removeTutor(): #Call redistGroups to redistribute group if tutor has one, delete tutor from list
	print("To be completed")

def viewTutorList(): #Print tutorlist and how many tutees each has. With option to add or remove tutor (which would call respective methods)
<<<<<<< HEAD
	print("To be completed")
=======
	outputList = []
	for entry in database.tutorList:
		temp = "	Name: " + database.tutorList[entry]["name"] + " " + database.tutorList[entry]["surname"]
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
			print("How many tutee's does this tutor have: ")
			tuteesN=tms.userInput("")
			print("So, \nTutor ID: "+tutorID+"\nFullname: "+name+" "+surname+"\nE-mail: "+email+" \nNumber of students in his group: "+tuteesN) 
			undecided = True
			while undecided:
				print("Is that correct: yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					undecided=False
					addTutor(tutorID, name, surname, email,tueesN)
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
>>>>>>> origin/master

def editTutor(): #Ask for surname. Show possible options or print error message. ask user for attribute to change.
	while True:
		print("")
		tutorSurname=tms.userInput("Input the surname of the tutor you wish to edit: ")
		tcount=0
		for tutorKey in database.tutorList:
			if tutorSurname==database.tutorList[tutorKey]["surname"].lower():
				tcount+=1
				print ("ID: "+database.tutorList[tutorKey]["id"]+". Name: "+database.tutorList[tutorKey]["name"]+". Surname: "+database.tutorList[tutorKey]["surname"]+". Email: "+database.tutorList[tutorKey]["email"])
				break
		if tcount==0:
			print("Sorry the tutor was not found.")
		else:
			while True:
				tChoice=tms.userInput("Enter the ID of the tutor you wish to edit: ")
				if tChoice in database.tutorList:
					tutorObj=database.tutorList[tChoice]
					break
				else:
					print("That tutor isn't in the list.")
			break
	while True:
		editChoice=tms.userInput("Do you wish to edit name, surname, email, or group?. ")
		if editChoice=="name":
			tutorObj["name"] = input("Please enter the new name: ")
			break
		elif editChoice=="surname":
			tutorObj["surname"] = input("Please enter the new surname: ")
			break
		elif editChoice=="email":
			tutorObj["email"] = input("Please enter the new Email address: ")
			break
		elif editChoice=="group":
			tutorObj["group"] = input("Please enter the new tutor ID: ")
			break
		else:
			print("\n\n                          ***Please input name, surname, email or group.***\n\n")
	print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])

def tutor(): 
#Ask for surname. Check list of tutors for surname. 
#Print error message if tutor not found. Print results with id, name, surname and email. User chooses result and prints its group
	print("\n                     -----------\n                        TUTOR\n                     -----------")
	check1=True
	check2=True
	tutorList=database.tutorList
	while check1:
		print("")
		tutorSurname=tms.userInput("Enter your surname: ")
		tcount=0
		for tutorKey in tutorList:
			if tutorSurname == tutorList[tutorKey]["surname"].lower():
				tcount += 1
				tutorObj = tutorList[tutorKey]
				check1 = False
				print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])
		if check1:
			print("Sorry that tutor was not found.")
		else:
			while check2:
				Choice = tms.userInput("Enter your tutor ID: ")
				if Choice in tutorList:
					tutorObj=tutorList[Choice]
					check2=False
					break
				else:
					print("That tutor isn't in the list.")