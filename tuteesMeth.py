#!/usr/bin/python3
import database
import tms


def addTutee(studentCode,surname,name,name2,tutor,course,acadYear,email):	#Adds student to database #COMPLETED
	database.tuteeList[studentCode]={"tuteeNo":studentCode, "name":name, "name2":name2, "surname":surname, "email":email, "course":course, "courseY":acadYear, "tutor":tutor}

def removeTutee(tuteeNo): #Place tutee in a separate database. COMPLETED
	database.delTuteeList[tuteeNo]=database.tuteeList[tuteeNo]
	tn=int(database.tutorList[database.tuteeList[tuteeNo]["tutor"]]["tuteesN"])
	tn-=1
	database.tutorList[database.tuteeList[tuteeNo]["tutor"]]["tuteesN"]=str(tn)
	del database.tuteeList[tuteeNo]

def viewTutorGroup(tutorN):	#Print tutorgroup depending on tutor COMPLETED
	tuteeList=database.tuteeList
	tutorList=database.tutorList
	print("")
	print("                       Tutor group information:")
	print("")
	print("TUTOR NUMBER      NAME                 EMAIL")
	for entry in tutorList:
		if tutorList[entry]["id"] == tutorN:
			print(tutorList[entry]["id"]+" "+(" ")*(17-len(tutorList[entry]["id"]))+tutorList[entry]["name"]+" "+tutorList[entry]["surname"]+" "+(" ")*(19-(len(tutorList[entry]["name"])+len(tutorList[entry]["surname"])))+tutorList[entry]["email"])
			print("")
			print("Your tutor group has " + tutorList[entry]["tuteesN"] + " tutees in it.")
			print("")
	print("STUDENT NUMBER    NAME                 EMAIL")
	for entry in tuteeList:
		if tuteeList[entry]["tutor"] == tutorN:
			print(tuteeList[entry]["tuteeNo"]+" "+(" ")*(17-len(tuteeList[entry]["tuteeNo"]))+tuteeList[entry]["name"]+" "+tuteeList[entry]["name2"]+tuteeList[entry]["surname"]+" "+(" ")*(19-(len(tuteeList[entry]["name"])+len(tuteeList[entry]["name2"])+len(tuteeList[entry]["surname"])))+tuteeList[entry]["email"])

def printTutees(): #COMPLETED
	print("")
	print("STUDENT NUMBER     NAME")
	for entry in database.tuteeList:
		if len(database.tuteeList[entry]["name2"])==0:
			print(database.tuteeList[entry]["tuteeNo"]+"           "+database.tuteeList[entry]["name"]+" "+database.tuteeList[entry]["surname"])
		else:
			print(database.tuteeList[entry]["tuteeNo"]+"           "+database.tuteeList[entry]["name"]+" "+database.tuteeList[entry]["name2"]+" "+database.tuteeList[entry]["surname"])

def viewTuteeList(): #Print tuteeList with option to add or remove tutees (which would call respective methods) 
	printTutees()
	takeAction = True
	while takeAction:
		print("\n	ADD STUDENT 		REMOVE STUDENT 		  RETURN TO MENU")
		print("")
		action = tms.userInput("")	

		if action.lower()=="add student":
			taken1=True
			checker1=0
			while taken1:
				checker2=0
				print("Enter the new student's student number: ")
				studentCode=tms.userInput("")
				if len(studentCode)==0:
					print("			Please enter a value.")
				if len(studentCode)>0:	
					if (not studentCode[0].isalpha()) or (not studentCode[1:].isdigit()) or (len(studentCode)!=8):
						print("   A student number must be in the format 1 letter followed by 7 digits. \nFor example: C1234567")
						checker2=1
					if checker2==0:
						studentCode=studentCode[0].capitalize()+studentCode[1:]	
						for entry in database.tuteeList:
							if studentCode == database.tuteeList[entry]["tuteeNo"]:
								print("			That number is already taken.")
								checker1=1
								break
						if checker1!=1:	
							taken1=False
			
			taken2 = True
			while taken2:
				print("Enter the new student's first name: ")
				name=tms.userInput("")
				if len(name)>0:
					if name.isalpha():
						name=name[0].capitalize()+name[1:]
						taken2=False
					if not name.isalpha():
						print("		Please use just alphabetical characters")
				elif len(name)==0:
					print("			Please enter a value.")

			taken8 = True
			while taken8:
				print("Enter the new student's middle name (Can leave blank): ")
				name2=tms.userInput("")
				if len(name2)>0:
					if name2.isalpha():
						name2=name2[0].capitalize()+name2[1:]
						taken8=False
					if not name2.isalpha():
						print("		Please use just alphabetical characters")
				if len(name2)==0:
					taken8=False
			taken3=True
			while taken3:
				print("Enter the new student's surname: ")
				surname=tms.userInput("")
				if len(surname)>0:
					if surname.isalpha():
						surname=surname[0].capitalize()+surname[1:]
						taken3=False
					if not surname.isalpha():
						print("		Please use just alphabetical characters")
				elif len(surname)==0:
					print("			Please enter a value.")
			taken4=True
			while taken4:
				print("Enter the new student's e-mail: ")
				email=tms.userInput("")
				if len(email)>0:
					taken4=False
				elif len(email)==0:
					print("			Please enter a value.")
			taken5=True
			while taken5:
				print("Enter the course they will be studying: ")
				course=tms.userInput("")
				if len(course)>0:
					if course.isalpha():
						taken5=False
					if not course.isalpha():
						print("		Please use just alphabetical characters")
				elif len(course)==0:
					print("			Please enter a value.")
			taken6=True
			while taken6:
				print("Enter which year of study will they be in: ")
				courseY=tms.userInput("")
				if courseY.isdigit():
					if len(courseY)>0:
						if int(courseY)<=6 and int(courseY)>0:
							taken6=False	
					if int(courseY)>6 or int(courseY)<1:
						print("		Please enter a valid year(e.g. 1-6)")
				
				elif len(courseY)==0:
					print("			Please enter a value.")
				elif not courseY.isdigit():
					print("		Please use just numerical values")
			taken7=True
			while taken7:
				print("Enter the ID of the tutor they will have: ")
				tutor=tms.userInput("")
				if tutor.isdigit():
					if len(tutor)>0 and int(tutor)<len(database.tutorList):
						taken7=False
					elif len(tutor)==0:
						print("			Please enter a value.")
					elif int(tutor)>len(database.tutorList):
						print("         Sorry there is no tutor with that ID")
				else:
					print("         Sorry the tutor ID must be an integer")
			print("So, \nStudent Number: "+studentCode+"\nFullname: "+name+" "+name2+" "+surname+"\nE-mail: "+email+" \nCourse: "+course+"\nYear of study: "+courseY+"\nTutor: "+tutor) 
			undecided = True
			while undecided:
				print("Is that correct: yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					undecided=False
					addTutee(studentCode, surname, name, name2, course, courseY, tutor,email)
					tn=int(database.tutorList[tutor]["tuteesN"])
					tn+=1
					database.tutorList[tutor]["tuteesN"]=str(tn)
					viewTuteeList()
				elif response=="no":
					print("You'll be returned to the menu to try again.")
					undecided=False
				else:
					print("Please enter 'yes' or 'no'")
		
		elif action.lower()=="remove student":
			match=True
			checker = 0
			while match:
				checker8=True
				while checker8:
					checker9 = 0
					print("Enter the Student number of the student to remove: ")
					removeNo=tms.userInput("")
					if len(removeNo)>0:	
						if (not removeNo[0].isalpha()) or (not removeNo[1:].isdigit()) or (len(removeNo)!=8):
							print("   A student number must be in the format 1 letter followed by 7 digits. \nFor example: C1234567")
							checker9=1
						if checker9==0:
							removeNo=removeNo[0].capitalize()+removeNo[1:]
							checker8=False	

				for entry in database.tuteeList:
					if removeNo == database.tuteeList[entry]["tuteeNo"]:						
						checker=1
				if checker!=1:	
					print("	    That doesn't match a student number in the database.")
				elif checker==1:
					match=False
			delete = True
			while delete:
				print("			   Remove "+removeNo+": yes/no")
				response = tms.userInput("")
				if response=="yes":
					takeAction=False
					delete=False
					removeTutee(removeNo)
					viewTuteeList()
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

def editTutee(): #Ask for tutee surname. show possible options or print error message. ask user for attribute to change.
	sflag=True
	sflag2=True
	while sflag:
		print("")
		tuteeSurname=tms.userInput("Input the surname of the tutee you wish to edit: ")
		scount=0
		tuteesCode=[]
		for tuteeKey in database.tuteeList:
			if tuteeSurname==database.tuteeList[tuteeKey]["surname"].lower():
				scount+=1
				sflag=False
				print ("Student Number: "+database.tuteeList[tuteeKey]["tuteeNo"]+". Name: "+database.tuteeList[tuteeKey]["name"]+" "+database.tuteeList[tuteeKey]["name2"]+". Surname: "+database.tuteeList[tuteeKey]["surname"]+". Email: "+database.tuteeList[tuteeKey]["email"])
				tuteesCode+=[database.tuteeList[tuteeKey]["tuteeNo"]]
		if scount==0:
			print("Sorry the tutee was not found.")
		else:
			while sflag2:
				Choice=tms.userInput("Enter the student number of the tutee you wish to edit: ").upper()
				if Choice in database.tuteeList and Choice in tuteesCode:
					tuteeObj=database.tuteeList[Choice]
					sflag2=False
					break
				else:
					print("That student isn't in the list.")
	while True:
		editChoice=tms.userInput("Do you wish to edit name, middle name, surname, email, course, course year or tutor? ")
		if editChoice=="name":
			tuteeObj["name"] = tms.userInput("Please enter the new name: ")
			print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
			break
		elif editChoice=="middle name":
			tuteeObj["name2"] = tms.userInput("Please enter the new name: ")
			print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
			break			
		elif editChoice=="surname":
			tuteeObj["surname"] = tms.userInput("Please enter the new surname: ")
			print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
			break
		elif editChoice=="email":
			tuteeObj["email"] = tms.userInput("Please enter the new Email address : ")
			print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
			break
		elif editChoice=="course":
			tuteeObj["course"] = tms.userInput("Please enter the new course: ")
			print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
			break
		elif editChoice=="course year":
			tuteeObj["course year"] = tms.userInput("Please enter the new course year: ")
			print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
			break
		elif editChoice=="tutor":
			tutorn = tms.userInput("Please enter the new tutor: ")
			if tutorn.isdigit():
				if int(tutorn)<len(database.tutorList):
					tuteeObj["tutor"]=tutorn
					print ("Name: "+tuteeObj["name"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
					break
				else:
					print("         Sorry there is no tutor with that ID")
			else:
				print("         Sorry the tutor ID must be an integer")
		else:
			print("\n\n                          ***Please input name, middle name, surname, email, course, course year or tutor.***\n\n")

def tutee(): #Ask for tutee number. Print error message if tutee not found. Ask if he wants to view tutor group info, enrolled courses or tutor info. COMPLETED
	print("\n                     -----------\n                       STUDENT\n                     -----------")
	check1=True
	check2=True
	check3=True
	tuteeList=database.tuteeList
	while check1:
		print("")
		studentNumber=tms.userInput("Enter your student number: ")
		print("")
		tcount=0
		for tuteeKey in tuteeList:
			if studentNumber == tuteeList[tuteeKey]["tuteeNo"].lower():
				tcount += 1
				tuteeObj = tuteeList[tuteeKey]
				check1=False
				print ("Name: "+tuteeObj["name"]+" "+tuteeObj["name2"]+". Surname: "+tuteeObj["surname"]+". Email: "+tuteeObj["email"]+". Course: "+tuteeObj["course"]+". Year: "+tuteeObj["courseY"]+". Tutor: "+tuteeObj["tutor"])
				break
		if check1:
			print("Sorry, that student was not found. Please try again.")
		else:
			while check2:
				print("")
				Choice = tms.userInput("Is this the correct student? ")
				if Choice == "yes":
					check2=False
					while check3:
						viewTutorGroup(tuteeObj["tutor"])
						print("\n	            		RETURN TO MENU 		                ")
						print("")
						Choice2 = tms.userInput("")
						if Choice2 == "return to menu":
							tms.main(True)
				elif Choice == "no":
					tutee()
				else:
					print("That is not a valid response. Please enter 'yes' or 'no'.")
					print("") 
