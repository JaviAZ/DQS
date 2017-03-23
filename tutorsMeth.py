#!/usr/bin/python3
import database
import tms
import tuteesMeth

def genGroups(): #Assigns a tutor to each tutee
	availableGroups=[]
	selectedGroup=1
	for tutor in database.tutorList:
		availableGroups.append(int(database.tutorList[tutor]["id"]))
		database.tutorList[tutor]["tuteesN"]="0"
	for tutee in database.tuteeList:
		while selectedGroup not in availableGroups:
			if selectedGroup > max(availableGroups):
				selectedGroup = 1
			else:
				selectedGroup += 1
		database.tuteeList[tutee]["tutor"]=str(selectedGroup)
		tn=int(database.tutorList[str(selectedGroup)]["tuteesN"])
		tn+=1
		database.tutorList[str(selectedGroup)]["tuteesN"]=str(tn)
		selectedGroup += 1

def redistTutee(tutorDelID,tutee):
	if database.tuteeList[tutee]["tutor"] == tutorDelID:
			temp=1000 # just a large value that is greater than total number of students
			for tutor in database.tutorList:
				
				if int(database.tutorList[tutor]["tuteesN"]) < temp :
					temp = int(database.tutorList[tutor]["tuteesN"])
					newTutorID = database.tutorList[tutor]["id"]
					tutorPos = tutor

			database.tutorList[tutorPos]["tuteesN"] = str(int(database.tutorList[tutorPos]["tuteesN"]) + 1)	
			database.tuteeList[tutee]["tutor"] = newTutorID
			print("-----------------------------------------------------")
			print(database.tuteeList[tutee]["name"] +" " + database.tuteeList[tutee]["surname"] + " has been moved to " + database.tutorList[(database.tuteeList[tutee]["tutor"])]["name"] + " " + database.tutorList[(database.tuteeList[tutee]["tutor"])]["surname"] + "'s tutor group.")

def redistGroups(tutorDelID): #Redistribute students into new groups
	tutorPos = 0
	newTutorID = 0 
	temp = 1000 
	for tutee in database.tuteeList:
		redistTutee(tutorDelID,tutee)
	print("")
	print("=====================================================")	


def addTutor(ID,name,surname,email,tuteesN): #Adds tutor to tutorList
	database.tutorList[ID]={"id":ID, "name":name, "surname":surname, "email":email, "tuteesN":tuteesN}

def removeTutor(ID): #Call redistGroups to redistribute group if tutor has one, delete tutor from list
	if ID!=len(database.tutorList):	
		while (int(ID)<len(database.tutorList)):
			#print(database.tutorList[ID])
			database.tutorList[ID]=database.tutorList[str(int(ID)+1)]
			database.tutorList[ID]["id"]=ID
			#print(database.tutorList[ID])
			for tutees in database.tuteeList:
				
				if database.tuteeList[tutees]["tutor"]==str(int(ID)+1):
					database.tuteeList[tutees]["tutor"]==ID
			ID=str(int(ID)+1)
		del database.tutorList[str(len(database.tutorList))]
	else:
		del database.tutorList[ID]
	redistGroups(ID)

def printTutors():	
	outputList = []
	i=1
	for entry in database.tutorList:
		temp = "ID: "+ database.tutorList[entry]["id"]+"   Number of tutees: "+database.tutorList[entry]["tuteesN"]+"	Name: " + database.tutorList[entry]["name"] + " " + database.tutorList[entry]["surname"]
		outputList.append(temp)
	for entry in outputList:
		print(entry)
		i+=1

def viewTutorList(): #Print tutorlist and how many tutees each has. With option to add or remove tutor (which would call respective methods)
	printTutors()
	takeAction = True
	while takeAction:
		print("\n		Add Tutor 	   Remove Tutor 	  Return to Menu")
		action = tms.userInput("")	
		if action.lower()=="add tutor":
			i=1
			for entry in  database.tutorList:
				for entry in  database.tutorList:
					if str(i)==database.tutorList[entry]["id"]:
						i+=1
					else:
						tutorID=str(i)			
			#tutorID=str(i)
			taken1=True
			while taken1:
				print("Enter their first name: ")
				name=tms.userInput("")
				if len(name)>0:
					if name.isalpha():
						name=name[0].capitalize()+name[1:]
						taken1=False
					elif not name.isalpha():
						print("		Please use just alphabetical characters.")
				elif len(name)==0:
					print("			Please enter a value.")
			taken2=True
			while taken2:
				print("Enter their surname: ")
				surname=tms.userInput("")
				if len(surname)>0:
					if surname.isalpha():
						surname=surname[0].capitalize()+surname[1:]
						taken2=False
					elif not surname.isalpha():
						print("		Please enter just alphabetical characters.")
				elif len(surname)==0:
					print("			Please enter a value.")
			taken3=True
			while taken3:
				print("Enter their e-mail: ")
				email=tms.userInput("")
				if len(email)>0:
					taken3=False
				elif len(email)==0:
					print("			Please enter a value.")
			print("So, \nTutor ID: "+tutorID+"\nFullname: "+name+" "+surname+"\nE-mail: "+email) 
			undecided = True
			while undecided:
				print("Is that correct: yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					undecided=False
					addTutor(tutorID, name, surname, email, "0")
					viewTutorList()
				elif response=="no":
					print("	   You'll be returned to the menu to try again.")
					undecided=False
				else:
					print("		   Please enter 'yes' or 'no'")
		

		elif action.lower()=="remove tutor":
			match=True
			checker = 0
			while match:
				checker8 =True
				while checker8:
					print("Enter the tutor ID of the tutor to remove: ")
					removeNo=tms.userInput("")
					if len(removeNo)>0:
						if not removeNo.isdigit():
							print("Tutor id contains only numbers.")
						else:
							checker8=False
					elif len(removeNo)<1:
						print("			Please enter a value.")
					for entry in database.tutorList:
						if removeNo == database.tutorList[entry]["id"].lower():						
							checker=1
					if checker!=1:	
						print("	    That doesn't match a tutor ID in the database.")
					elif checker==1:
						match=False
			delete = True
			while delete:
				print("			   Remove "+removeNo+": yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					delete=False
					removeTutor(removeNo)
					viewTutorList()
				elif response=="no":
					print("You'll be returned to the menu to try again.")
					delete=False
				else:
					print("Please enter 'yes' or 'no'")
		

		elif action.lower()=="return to menu":
			takeAction=False
			tms.admin(True)
		else:
			print("invalid input")

def editTutor(): #Ask for surname. Show possible options or print error message. ask user for attribute to change.
	while True:
		print("")
		tutorSurname=tms.userInput("Input the surname of the tutor you wish to edit: ")
		tcount=0
		tutorsCode=[]
		for tutorKey in database.tutorList:
			if tutorSurname==database.tutorList[tutorKey]["surname"].lower():
				tcount+=1
				print ("ID: "+database.tutorList[tutorKey]["id"]+". Name: "+database.tutorList[tutorKey]["name"]+". Surname: "+database.tutorList[tutorKey]["surname"]+". Email: "+database.tutorList[tutorKey]["email"])
				tutorsCode+=[database.tutorList[tutorKey]["id"]]
				break
		if tcount==0:
			print("Sorry the tutor was not found.")
		else:
			while True:
				tChoice=tms.userInput("Enter the ID of the tutor you wish to edit: ")
				if tChoice in database.tutorList and tChoice in tutorsCode:
					tutorObj=database.tutorList[tChoice]
					break
				else:
					print("That tutor isn't in the list.")
			break
	while True:
		editChoice=tms.userInput("Do you wish to edit name, surname, email, or group? ")
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
	check3=True
	tutorsCode=[]
	print("")
	printTutors()
	print("")
	tutorList=database.tutorList
	while check1:
		print("")
		tutorSurname=tms.userInput("Enter your surname: ")
		print("")
		tcount=0
		for tutorKey in tutorList:
			if tutorSurname == tutorList[tutorKey]["surname"].lower():
				tcount += 1
				tutorObj = tutorList[tutorKey]
				check1=False
				tutorsCode+=tutorObj["id"]
				print ("ID: "+tutorObj["id"]+". Name: "+tutorObj["name"]+". Surname: "+tutorObj["surname"]+". Email: "+tutorObj["email"])
		if check1:
			print("Sorry, that tutor was not found. Please try again.")
			print("")
		else:
			while check2:
				print("")
				Choice = tms.userInput("Enter your tutor ID number: ")
				if Choice in tutorList and Choice in tutorsCode:
					tutorObj=tutorList[Choice]
					check2=False
					while check3:
						tuteesMeth.viewTutorGroup(tutorObj["id"])
						print("\n	            		RETURN TO MENU 		                ")
						print("")
						Choice2 = tms.userInput("")
						if Choice2 == "return to menu":
							tms.main(True)
				else:
					print("That tutor isn't in the list.") 
