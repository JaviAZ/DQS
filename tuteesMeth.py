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

def viewTutorGroup():	#Print tutorgroup depending on tutor
	print("To be completed")

def viewTuteeList(): #Print tuteeList with option to add or remove tutees (which would call respective methods)
	tuteeList=database.tuteeList
	outputList = []
	for entry in tuteeList:
		temp = "	Name: " + tuteeList[entry]["name"] + " " + tuteeList[entry]["surname"]
		outputList.append(temp)
	for entry in outputList:
		print(entry)
	takeAction = True
	undecided = True
	while takeAction:
		print("\n	Add student 		Remove Student 			Return to Menu")
		action = tms.userInput("")	
		if action.lower()=="add student":
			print("What is the new students, student number: ")
			studentCode=tms.userInput("")
			print("And their first name: ")
			name=tms.userInput("")
			print("And their surname: ")
			surname=tms.userInput("")
			print("And their e-mail: ")
			email=tms.userInput("")
			print("And the course they're studying: ")
			course=tms.userInput("")
			print("And which year of study are they in: ")
			courseY=tms.userInput("")
			print("And who will be their tutor: ")
			tutor=tms.userInput("")
			print("So, \nStudent number: "+studentCode+"\nFullname: "+name+" "+surname+"\nE-mail: "+email+" \nCourse: "+course+"\nYear of study: "+courseY+"\nTutor: "+tutor) 
			undecided = True
			while undecided:
				print("Is that correct: yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					undecided=False
					addTutee(studentCode, surname, name, email, course, courseY, tutor)
					viewTuteeList()
				elif response=="no":
					print("You'll be returned to the menu to try again.")
					undecided=False
				else:
					print("Please enter 'yes' or 'no'")
		elif action.lower()=="remove student":
			takeAction=False
			removeTutee()
		elif action.lower()=="return to menu":
			takeAction=False
			tms.admin()
		else:
			print("invalid input")

def editTutee(): #Ask for tutee surname. show possible options or print error message. ask user for attribute to change.
	sflag=True
	sflag2=True
	tuteeList=database.tuteeList
	while sflag:
		tuteeSurname=tms.userInput("Input the surname of the tutee you wish to edit: ")
		scount=0
		for tuteeKey in tuteeList:
			if tuteeSurname==tuteeList[tuteeKey]["surname"].lower():
				scount+=1
				sflag=False
				print ("Student number: "+tuteeList[tuteeKey]["tuteeNo"]+". Name: "+tuteeList[tuteeKey]["name"]+". Surname: "+tuteeList[tuteeKey]["surname"]+". Email: "+tuteeList[tuteeKey]["email"])
		if scount==0:
			print("Sorry the tutee was not found.")
		else:
			while sflag2:
				Choice=tms.userInput("Enter the student number of the tutee you wish to edit: ")
				if sChoice in tuteeList:
					tuteeObj=tuteeList[sChoice]
					sflag2=False
					break
				else:
					print("That student isn't in the list.")
	editChoice=tms.userInput("Do you wish to edit name, surname, email, course, course year or tutor?")
	if editChoice=="name":
		print("To be completed")
	elif editChoice=="surname":
		print("To be completed")
	elif editChoice=="email":
		print("To be completed")
	elif editChoice=="course":
		print("To be completed")
	elif editChoice=="course year":
		print("To be completed")
	elif editChoice=="tutor":
		print("To be completed")
	else:
		print("\n\n                          ***Please input name, surname, email, course, course year or tutor.***\n\n")
	database.tuteeList=tuteeList

def tutee(): #Ask for tutee number. Print error message if tutee not found. Ask if he wants to view tutor group info, enrolled courses or tutor info.
	print("\n                     -----------\n                       STUDENT\n                     -----------")
	number=tms.userInput("Enter your student number: ")