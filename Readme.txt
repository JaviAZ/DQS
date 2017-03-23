If you want to edit csv files to add more info, or simply view them, use notepad, excel can give errors.

Javier: tms.userInput(Completed) tms.importTutees(completed),tms.importTutors(completed),tms.startprogram(completed),tms.admin(completed),tms.main(completed),tms.endProgram(completed),tms.exportTutees(completed),tms.exportTutors(completed)
Kurt:tutorMeth.removeTutor(completed), tutorMeth.viewTutorList, tuteeMeth.viewTuteeList(completed), tuteeMeth.removeTutee(completed)
Anuj:tutorMeth.editTutor(completed), tuteeMeth.editTutee(completed), tutorMeth.tutor,tuteeMeth.tutee(completed)
Andrew: tutorMeth.redistGroups,tuteeMeth.addTutee(completed),tutorsMeth.addTutor(completed)
Charlie: tuteeMeth.viewTutorGroup,tutorsMeth.genGroups(completed)

MarkScheme:
	1.Upload an excel / csv file of new students and assign new students to personal tutees
	2.Searching the personal tutor list for individual students
	3.Displaying lists of tutees for a particular personal tutor
	4.Display information on the quota of tutees each staff member has been assigned per year or degree group
	5.Teams of five or more: Delete a student from the tutor list and re-assign a single student to an alternative tutor.	

Things to fix:

	-add validation checking to inputs
	-spaces after first names in tutees.csv
	-tutor degree isnt taken in account when assigning groups
	-viewTutorGroup which is found in tuteesMeth.py is used in the tutee() method to display the 
		origin/master
          list of tutees and also in the tutor() method. However, it reads 
          "The other members of your tutor group are:" which doesn't make sense if it's used in the tutor() method.
	-The headers such as "Tutor Number", "Name" and "Email" in the viewTutorGroup method could be changed to
	   all uppercase to make it stand out?
	- random layout changes

Fixed:
	-tutor can be added with the same ID of an old tutor, overwritting it. Make the program create the ID instead of the user - issue also applies to editting preexisting tutors
	-tutee can be added with the same tuteeNo of an old tutee, overwritting it. Make the program check if that tuteeNo is already in the list.
	-can't cancel editting tutor or students on admin page
	-potentially can try and view tutor groups as before they've been generated, makes it crash
	-view students displays first name twice
	-when showing tutor list print their ID
	-when adding student you can put any number into tutor number
	-when editing student you can put any number into tutor number
	-when editing student, and asked for validation of student number, inputing any other student number would edit it
	-when editing tutor, and asked for validation of ID, inputing any other id would edit it
	-keep record of deleted students