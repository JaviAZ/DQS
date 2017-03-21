#!/usr/bin/python3
import database
import tms

def addTutee(studentCode,surname,name,tutor,course,acadYear,email):	#will call addToGroup if method isnt called from createProgram
	database.tuteeList[studentCode]={"tuteeNo":studentCode, "name":name, "surname":surname, "email":email, "course":course, "courseY":acadYear, "tutor":tutor}

def removeTutee(surname): #remove from tutor group too 
	#tuteeList=database.tuteeList
	#for entry in tuteeList:
	#	if entry["surname"] == surname:
	#		print("Do you want to remove: " + surname)
	#	else:
	#		print("No Tutee's with the surname: " + surname)
	print("To be completed")

def viewTutorGroup(tutorN):	#Print tutorgroup depending on tutor
	tuteeList=database.tuteeList
	print("The other members of your tutor group are:\n")
	for entry in tuteeList:
		if int(tuteeList[entry]["tutor"]) == tutorN:
			print(tuteeList[entry]["tuteeNo"]+" "+tuteeList[entry]["name"]+" "+tuteeList[entry]["surname"]+" "+tuteeList[entry]["email"])

def viewTuteeList(): #Print tuteeList with option to add or remove tutees (which would call respective methods)
	outputList = []
	for entry in database.tuteeList:
		temp = "	Name: " + database.tuteeList[entry]["name"] + " " + database.tuteeList[entry]["surname"]
		outputList.append(temp)
	for entry in outputList:
		print(entry)
	takeAction = True
	while takeAction:
		print("\n	ADD STUDENT 		REMOVE STUDENT 			RETURN TO MENU")
		print("")
		action = tms.userInput("")	
		if action.lower()=="add student":
			print("Enter the new student's student number: ")
			studentCode=tms.userInput("")
			print("Enter the new student's first name: ")
			name=tms.userInput("")
			if len(name)>0:
				name=name[0].capitalize()+name[1:]
			print("Enter the new student's surname: ")
			surname=tms.userInput("")
			if len(surname)>0:
				surname=surname[0].capitalize()+surname[1:]
			print("Enter the new student's e-mail: ")
			email=tms.userInput("")
			print("Enter the course they will be studying: ")
			course=tms.userInput("")
			print("Enter which year of study will they be in: ")
			courseY=tms.userInput("")
			print("Enter the ID of the tutor they will have: ")
			tutor=tms.userInput("")
			print("So, \nStudent Number: "+studentCode+"\nFullname: "+name+" "+surname+"\nE-mail: "+email+" \nCourse: "+course+"\nYear of study: "+courseY+"\nTutor: "+tutor) 
			undecided = True
			while undecided:
				print("Is that correct: yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					undecided=False
					addTutee(studentCode, surname, name, course, courseY, tutor,email)
					viewTuteeList()
				elif response=="no":
					print("You'll be returned to the menu to try again.")
					undecided=False
				else:
					print("Please enter 'yes' or 'no'")
		elif action.lower()=="remove student":
			takeAction=False
			removeTutee("")
		elif action.lower()=="return to menu":
			takeAction=False
			tms.admin()
		else:
			print("invalid input")

def editTutee(): #Ask for tutee surname. show possible options or print error message. ask user for attribute to change.
	sflag=True
	sflag2=True
	while sflag:
		print("")
		tuteeSurname=tms.userInput("Input the surname of the tutee you wish to edit: ")
		scount=0
		for tuteeKey in database.tuteeList:
			if tuteeSurname==database.tuteeList[tuteeKey]["surname"].lower():
				scount+=1
				sflag=False
				print ("Student Number: "+database.tuteeList[tuteeKey]["tuteeNo"]+". Name: "+database.tuteeList[tuteeKey]["name"]+". Surname: "+database.tuteeList[tuteeKey]["surname"]+". Email: "+databse.tuteeList[tuteeKey]["email"])
		if scount==0:
			print("Sorry the tutee was not found.")
		else:
			while sflag2:
				Choice=tms.userInput("Enter the student number of the tutee you wish to edit: ").upper()
				if Choice in databse.tuteeList:
					tuteeObj=database.tuteeList[Choice]
					sflag2=False
					break
				else:
					print("That student isn't in the list.")
	editChoice=tms.userInput("Do you wish to edit name, surname, email, course, course year or tutor? ")
	if editChoice=="name":
		tuteeObj["name"] = tms.userInput("Please enter the new name: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="surname":
		tuteeObj["surname"] = tms.userInput("Please enter the new surname: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="email":
		tuteeObj["email"] = tms.userInput("Please enter the new Email address : ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="course":
		tuteeObj["course"] = tms.userInput("Please enter the new course: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="course year":
		tuteeObj["course year"] = tms.userInput("Please enter the new course year: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="tutor":
		tuteeObj["tutor"] = tms.userInput("Please enter the new tutor: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	else:
		print("\n\n                          ***Please input name, surname, email, course, course year or tutor.***\n\n")

def tutee(): #Ask for tutee number. Print error message if tutee not found. Ask if he wants to view tutor group info, enrolled courses or tutor info.
	print("\n                     -----------\n                       STUDENT\n                     -----------")
	number=tms.userInput("Enter your student number: ")