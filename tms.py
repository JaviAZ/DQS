#!/usr/bin/python3
from database import *

def viewTutorList():
	print("To be completed")

def editTutor(tutorObj):
	editChoice=input("Do you wish to edit name, surname, email, or group?").lower()
	if editChoice=="name":
		print("To be completed")
	elif editChoice=="surname":
		print("To be completed")
	elif editChoice=="email":
		print("To be completed")
	elif editChoice=="group":
		print("To be completed")
	else:
		print("Please input name, surname, email or group.")

def viewStudentList():
	print("To be completed")

def editStudent(studentObj):
	print("To be completed")

def createProgram():
	print("To be completed")

def startProgram():
	print("To be completed")

def endProgram():
	print("To be completed")

def admin():
	print("Manage tutors:                             Manage students:")
	print()
	print(" View tutors                                View students  ")
	print()
	print(" Edit tutors                                Edit students  ")
	print()
	print("                     Create program                        ")
	print("                     Start program                         ")
	print("                       End program                         ")
	adminOption=input().lower()
	print()
	if adminOption=="view tutors":
		viewTutorList()
	elif adminOption=="edit tutors":
		tflag=True
		tflag2=True
		while tflag:
			tutorSurname=input("Input the surname of the tutor you wish to edit: ").lower()
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
					tChoice=input("Enter the ID of the tutor you wish to edit: ")
					if tChoice in tutorList:
						editTutor(tutorList[tChoice])
						tflag2=False
						break
					else:
						print("That tutor isn't in the list.")
	elif adminOption=="view students":
		viewStudentList()
	elif adminOption=="edit students":
		sflag=True
		sflag2=True
		while sflag:
			studentSurname=input("Input the surname of the student you wish to edit: ").lower()
			scount=0
			for studentKey in studentList:
				if studentSurname==studentList[studentKey]["surname"].lower():
					scount+=1
					sflag=False
					print ("Student number: "+studentList[studentKey]["studentNo"]+". Name: "+studentList[studentKey]["name"]+". Surname: "+studentList[studentKey]["surname"]+". Email: "+studentList[studentKey]["email"])
			if tcount==0:
				print("Sorry the student was not found.")
			else:
				while sflag2:
					Choice=input("Enter the student number of the student you wish to edit: ")
					if sChoice in studentList:
						editTutor(studentList[sChoice])
						sflag2=False
						break
					else:
						print("That student isn't in the list.")
	elif adminOption=="create program":
		createProgram()
	elif adminOption=="start program":
		startProgram()
	elif adminOption=="end program":
		endProgram()
	else:
		print("Please input view tutors, edit tutors, view students, edit students, create program, start program or end program.")

def tutor():
	print("To be completed")

def student():
	print("To be completed")

def main():
	print("Cardiff University Computer Science Tutor Management System")
	print("Admin")
	print("Tutor")
	print("Student")
	chooseView=input().lower()
	print()
	if chooseView=="admin":
		admin()
	elif chooseView=="tutor":
		tutor()
	elif chooseView=="student":
		student()
	else:
		print("Please input admin, tutor or student.")

main()