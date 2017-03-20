#!/usr/bin/python3
import database
import tms

def addTutee(studentCode,surname,name,tutor,course,acadYear,email):	#will call addToGroup if method isnt called from createProgram
	database.tuteeList[studentCode]={"tuteeNo":studentCode, "name":name, "surname":surname, "email":email, "course":course, "courseY":acadYear, "tutor":tutor}

def removeTutee(): #remove from tutor group too 
	print("To be completed")

def viewTutorGroup():	#Print tutorgroup depending on tutor
	print("To be completed")

def viewTuteeList(): #Print tuteeList with option to add or remove tutees (which would call respective methods)
	print("To be completed")

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
				Choice=tms.userInput("Enter the student number of the tutee you wish to edit: ").upper()
				if Choice in tuteeList:
					tuteeObj=tuteeList[Choice]
					sflag2=False
					break
				else:
					print("That student isn't in the list.")
	editChoice=tms.userInput("Do you wish to edit name, surname, email, course, course year or tutor?")
	if editChoice=="name":
		tuteeObj["name"] = input("Please enter the new name: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="surname":
		tuteeObj["surname"] = tms.userInput("Please enter the new surname: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="email":
		tuteeObj["email"] = input("Please enter the new Email address : ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="course":
		tuteeObj["course"] = input("Please enter the new course: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="course year":
		tuteeObj["course year"] = input("Please enter the new course year: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	elif editChoice=="tutor":
		tuteeObj["tutor"] = input("Please enter the new tutor: ")
		print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])

	else:
		print("\n\n                          ***Please input name, surname, email, course, course year or tutor.***\n\n")
	database.tuteeList=tuteeList

def tutee(): #Ask for tutee number. Print error message if tutee not found. Ask if he wants to view tutor group info, enrolled courses or tutor info.
	print("\n                     -----------\n                       STUDENT\n                     -----------")
	number=tms.userInput("Enter your student number: ")