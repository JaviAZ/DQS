#!/usr/bin/python3
import database
import tutorsMeth
import tuteesMeth
import csv

def endProgram(): #Later dictionaries will be put into csv before closing the application. COMPLETED
	print("")
	print("Exiting program.")
	exportTutees()
	exportTutors()
	if len(database.delTuteeList)>0:
		exportDelTutees()
	quit()

def userInput(msg):	#Function to handle user input, make it lower case and check if user wants to end program or go back to main menu. To be completed
	npt = input(msg).lower()
	if npt=="endp":
		endProgram()
	if npt=="main":
		main(True)
	return npt

def importTutees(): #Imports information from Tutees.csv into tuteeList COMPLETED
	with open ('Tutees.csv',"r") as csvfile:
		spamreader=csv.reader(csvfile,delimiter=";",quotechar="|")
		next(spamreader,None)
		for row in spamreader:
			if len(row)>0:
				if row[0][0]!="U":
					tuteesMeth.addTutee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])

def importTutors(): #Imports informtation from Tutors.csv into tutorList COMPLETED
	with open ('Tutors.csv',"r") as csvfile:
		spamreader=csv.reader(csvfile,delimiter=";",quotechar="|")
		next(spamreader,None)
		for row in spamreader:
			if len(row)>0:
				if row[0][0]!="U":
					tutorsMeth.addTutor(row[0],row[1],row[2],row[3],row[4])

def exportTutees(): #Exports information from tuteeList into Tutees.csv COMPLETED
	with open ('Tutees.csv','w') as csvfile:
		writer=csv.writer(csvfile,delimiter=";")
		header=["Student Code","Surname","Forename1","Forename2","TUTOR","Course","Acad Year","Univ Email"]
		writer.writerow(header)
		for tutee in database.tuteeList:
			writer.writerow([database.tuteeList[tutee]["tuteeNo"],database.tuteeList[tutee]["surname"],database.tuteeList[tutee]["name"],database.tuteeList[tutee]["name2"],database.tuteeList[tutee]["tutor"],database.tuteeList[tutee]["course"],database.tuteeList[tutee]["courseY"],database.tuteeList[tutee]["email"]])
		courseCodes=[["UFBSCMSA","BSc Computer Science"],["UFBSCMSB","BSc Computer Science with year in industry"],["UFBSCSFA","BSc Computer Science with Security and Forensics"],["UFBSCSFB","BSC Computer Science with Security and Forensics with year in industry"],["UFBSCSHA","BSc Computer Science with HPC"],["UFBSCSHB","BSc Computer Science with HPC with year in industry"],["UFBSCVCA","BSc Computer Science with Computer Vision and Computer Graphics"],["UFBSCVCB","BSc Computer Science with Computer Vision and Computer Graphics with year in industry"],["UFBSASEA","BSc Applied Software Engineering"]]
		writer.writerows(courseCodes)

def exportDelTutees(): #Exports information from tuteeList into Tutees.csv
	with open ('DelTutees.csv','w') as csvfile:
		writer=csv.writer(csvfile,delimiter=";")
		header=["Student Code","Surname","Forename1","Forename2","TUTOR","Course","Acad Year","Univ Email"]
		writer.writerow(header)
		for tutee in database.delTuteeList:
			writer.writerow([database.delTuteeList[tutee]["tuteeNo"],database.delTuteeList[tutee]["surname"],database.delTuteeList[tutee]["name"],database.tuteeList[tutee]["name2"],database.delTuteeList[tutee]["tutor"],database.delTuteeList[tutee]["course"],database.delTuteeList[tutee]["courseY"],database.delTuteeList[tutee]["email"]])

def exportTutors(): #Exports information from tutorList into Tutors.csv
	with open ('Tutors.csv',"w") as csvfile:
		writer=csv.writer(csvfile,delimiter=";")
		header=["ID","Name","Surname","Email","nOfTutees"]
		writer.writerow(header)
		for tutor in database.tutorList:
			writer.writerow([database.tutorList[tutor]["id"],database.tutorList[tutor]["name"],database.tutorList[tutor]["surname"],database.tutorList[tutor]["email"],database.tutorList[tutor]["tuteesN"]])

def startProgram(): #Calls importing functions and main function. COMPLETED
	importTutees()
	importTutors()
	for tutee in database.tuteeList:
		if(len(database.tuteeList[tutee]["tutor"])==0):
			print("Groups must be created, go to ADMIN and create groups")
			main(False)
	main(True)

def admin(groupsCreated): #Let user choose view tutors, view students, edit tutors, edit students, create groups or end program. Call method depending on user choice. COMPLETED
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
	if groupsCreated==False:
		if adminOption=="create groups":
			tutorsMeth.genGroups()
		else:
			print("Groups must be created, go to Create groups")
			admin(False)
	else:
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
		admin(True)

def main(groupsCreated): #COMPLETED
	print("")
	print("            ===========================================================")
	print("            Cardiff University Computer Science Tutor Management System")
	print("            ===========================================================")
	print("")
	print("                                     ADMIN")
	print("")
	print("                                     TUTOR")
	print("")
	print("                                    STUDENT")
	print("\n                  **Type endp at any time to exit the program**")
	print("                **Type main at any time to go back to this menu**")
	chooseView=userInput("")
	if groupsCreated==False:
		if chooseView=="admin":
			admin(False)
		else:
			print("Groups must be created, go to ADMIN and create groups")
			main(False)
	else:
		if chooseView=="admin":
			admin(True)
		elif chooseView=="tutor":
			tutorsMeth.tutor()
		elif chooseView=="student":
			tuteesMeth.tutee()
		else:
			print("\n\n                          ***Please input admin, tutor or student.***\n\n")
			main(True)

if __name__ == "__main__":
	startProgram()
	