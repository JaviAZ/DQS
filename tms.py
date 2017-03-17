#!/usr/bin/python3
from database import *
from tuteesMeth import *
from tutorsMeth import *

def endProgram():	#Later dictionaries will be put into csv in this method
	print("Exiting program.")
	quit()

def userInput(msg):	#Function to handle user input, check gameparser from Computatinal thinking coursework. To be completed
	npt = input(msg).lower()
	if npt=="endp":
		endProgram()
	if npt=="main":
		main()
	return npt

def createProgram(): #will create the tutee and tuteeList using csv file and call genGroups(). Use addTutee()
	print("To be completed")

def startProgram(): #will fetch csv for dictionaries data
	print("To be completed")

def admin():	#Let user choose view tutors, view students, edit tutors, edit students, create program, start program or end program. Call method depending on user choice. Main menu and go back option every view
	print("\n                     -----------\n                        ADMIN\n                     -----------")
	print("Manage tutors:                             Manage students:")
	print()
	print(" View tutors                                View students  ")
	print()
	print(" Edit tutors                                Edit students  ")
	print()
	print("                     Create program                        ")
	print("                     Start program                         ")
	print("                       End program                         ")
	adminOption=userInput("")
	if adminOption=="view tutors":
		viewTutorList()
	elif adminOption=="edit tutors":
		editTutor()
	elif adminOption=="view students":
		viewTuteeList()
	elif adminOption=="edit students":
		editTutee()
	elif adminOption=="create program":
		createProgram()
	elif adminOption=="start program":
		startProgram()
	elif adminOption=="end program":
		endProgram()
	else:
		print("\n\n                          ***Please input view tutors, edit tutors, view students, edit students, create program, start program or end program.***\n\n")
		admin()

def main():
	print("Cardiff University Computer Science Tutor Management System")
	print("Admin")
	print("Tutor")
	print("Student")
	print("**Type endp at any time to exit the program**")
	print("**Type main at any time to go back to this menu**")
	chooseView=userInput("")
	if chooseView=="admin":
		admin()
	elif chooseView=="tutor":
		tutor()
	elif chooseView=="student":
		tutee()
	else:
		print("\n\n                          ***Please input admin, tutor or student.***\n\n")
		main()

main()