#!/usr/bin/python3


def viewTutorList():


def editTutor(tutorID):


def viewStudentList():


def editStudent(studentNumb):


def createProgram():


def startProgram():


def endProgram():


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
		while tflag:
			tutorSurname=input("Input the name of the tutor you wish to edit: ")
			tcount=0
			tscount=0
			for tutorSrnm in tutorList:
				ts++
				if tutorSurname==tutorSrnm["surname"]:
					tcount++
					tflag=False
					print ("ID: "+ts+". Name: "+tutorList[ts]["name"]+". Surname: "+tutorSrnm+". Email: "+tutorList[ts]["email"])
			if tcount==0:
				print("Sorry the tutor was not found.")
			else:
				tChoice=int(input("Enter the ID of the tutor you wish to edit: "))
				if tChoice>tutorList.size() or tChoice<0:
					print("That tutor isn't in the list.")
				else:
					editTutor(tChoice)



	elif adminOption=="view students":

	elif adminOption=="edit students":

	elif adminOption=="create program":

	elif adminOption=="start program":

	elif adminOption=="end program":

	else:
		print("Please input view tutors, edit tutors, view students, edit students, create program, start program or end program.")

def tutor():


def student():


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
