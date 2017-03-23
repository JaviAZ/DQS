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
	when adding student you can put any number into tutor number
	when editing student you can put any number into tutor number
	spaces after first names in tutees.csv

	1) When you open the program and select "ADMIN" and then "VIEW TUTORS", only the names of the tutors are shown. 
	   This means when "Remove Tutor" is selected, you can't see the ID of the tutor you want to remove.

	2) When the admin goes and selects "Add Tutor" or "Add Student", 
           there is no way to get out of the creation process, the admin must make the tutor or student fully in 
           order to exit the process.

	3) When the "Edit Tutor" option is selected, the ID of the tutor cannot be changed.

	4) When you open the program and select "TUTOR" and then enter a surname e.g. Marshall, 
           the following prompt asks you to enter the tutor ID number of the tutor you would like to proceed with. 
           At this point the user can enter the tutor ID of any tutor and it will display the group for 
           the tutor with the matching ID. Not restricted to the tutors that are shown on screen with the surnames.

	5) viewTutorGroup which is found in tuteesMeth.py is used in the tutee() method to display the 
           list of tutees and also in the tutor() method. However, it reads 
           "The other members of your tutor group are:" which doesn't make sense if it's used in the tutor() method.

	6) The headers such as "Tutor Number", "Name" and "Email" in the viewTutorGroup method could be changed to
	   all uppercase to make it stand out?

	+ random layout changes



Fixed:
	tutor can be added with the same ID of an old tutor, overwritting it. Make the program create the ID instead of the user - issue also applies to editting preexisting tutors
	tutee can be added with the same tuteeNo of an old tutee, overwritting it. Make the program check if that tuteeNo is already in the list.
	can't cancel editting tutor or students on admin page
	potentially can try and view tutor groups as before they've been generated, makes it crash
	view students displays first name twice
	when showing tutor list print their ID