#!/usr/bin/python3
import database
import tutorsMeth
import tuteesMeth
import csv

def endProgram(): #Later dictionaries will be put into csv before closing the application. To be completed
	print("Exiting program.")
	quit()

def userInput(msg):	#Function to handle user input, make it lower case and check if user wants to end program or go back to main menu. Completed
	npt = input(msg).lower()
	if npt=="endp":
		endProgram()
	if npt=="main":
		main()
	return npt

def importTutees(): #Imports information from Tutees.csv into tuteeList COMPLETED
	with open (r'C:\Users\Anuj\Desktop\DQS Project\DQS\Tutees.csv',"r") as csvfile:
		spamreader=csv.reader(csvfile,delimiter=",",quotechar="|")
		next(spamreader,None)
		for row in spamreader:
			if row[0][0]!=";" and row[0][0]!="U":
				t=[]
				for col in row:
					temp=""
					for char in col:
						if char!=";":
							temp+=char
						else:
							t.append(temp)
							temp=""
				tuteesMeth.addTutee(t[0],t[1],t[2]+t[3],t[4],t[5],t[6],t[7])

def importTutors(): #Imports informtation from Tutors.csv into tutorList COMPLETED
	with open (r'C:\Users\Anuj\Desktop\DQS Project\DQS\Tutors.csv',"r") as csvfile:
		spamreader=csv.reader(csvfile,delimiter=",",quotechar="|")
		next(spamreader,None)
		for row in spamreader:
			if row[0][0]!=";":
				t=[]
				for col in row:
					temp=""
					for char in col:
						if char!=";":
							temp+=char
						else:
							t.append(temp)
							temp=""
				tutorsMeth.addTutor(t[0],t[1],t[2],t[3])

def startProgram(): #Calls importing functions and main function. COMPLETED
	importTutees()
	importTutors()
	main()

def admin(): #Let user choose view tutors, view students, edit tutors, edit students, create groups or end program. Call method depending on user choice. COMPLETED
	print("\n                              -----------\n                                 ADMIN\n                              -----------")
	print("     Manage Tutors:                                  Manage Students:")
	print()
	print("      VIEW TUTORS                                     VIEW STUDENTS  ")
	print("(Also for adding/deleting)                     (Also for adding/deleting)")
	print()
	print("      EDIT TUTORS                                     EDIT STUDENTS  ")
	print()
	print("                               CREATE GROUPS                        ")
	print("                                END PROGRAM                         ")
	adminOption=userInput("")
	if adminOption=="view tutors":
		tutorsMeth.viewTutorList()
	elif adminOption=="edit tutors":
		tutorsMeth.editTutor()
	elif adminOption=="view students":
		print("")
		tuteesMeth.viewTuteeList()
	elif adminOption=="edit students":
		tuteesMeth.editTutee()
	elif adminOption=="create groups":
		tutorsMeth.genGroups()
	elif adminOption=="end program":
		endProgram()
	else:
		print("\n\n                          ***Please input view tutors, edit tutors, view students, edit students, create program, start program or end program.***\n\n")
	admin()

def main():
	print("")
	print("            Cardiff University Computer Science Tutor Management System\n")
	print("                                     ADMIN")
	print("")
	print("                                     TUTOR")
	print("")
	print("                                    STUDENT")
	print("\n                  **Type endp at any time to exit the program**")
	print("                **Type main at any time to go back to this menu**")
	chooseView=userInput("")
	if chooseView=="admin":
		admin()
	elif chooseView=="tutor":
		tutorsMeth.tutor()
	elif chooseView=="student":
		tuteesMeth.tutee()
	else:
		print("\n\n                          ***Please input admin, tutor or student.***\n\n")
		main()

if __name__ == "__main__":
	startProgram()