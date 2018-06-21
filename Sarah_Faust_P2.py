#-------------------------------------------------------------------------------
# Student Name: Sarah Faust / Assignment: P #2 / Date: 09/18/2012
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments: Attempting the extra credit
#-------------------------------------------------------------------------------
# Pseudocode:
#Begin
#	answer=while loop starter variable
#	while answer is variations of yes
#		angle1 = ask for angle
#		angle2 = ask for angle
#		while (angle1 + angle2)>179:
#			print(tell user to try again)
#			angle1= ask for new angle
#			angle2= ask for new angle
#		angle3 = 180-(angle1+angle2)
#		if angle1==90 or angle2==90 or angle3==90:
#			print(right:\t yes)
#		else:
#			print(right:\t no)
#		if angle1>90 or angle2>90 or angle3>90:
#			print(obtuse:\t yes)
#		else:
#			print(obtuse:\t no)
#		if angle1<90 and angle2<90 and angle3<90:
#			print(acute:\t yes)
#		else:
#			print(acute:\t no)
#		if angle1==angle2 and angle2==angle3:
#			print(equilateral:\t yes)
#		else:
#			print(equilateral:\t no)
#		if angle1==angle1 or angle1==angle3 or angle2==angle3:
#			print(isosceles:\t yes)
#		else:
#			print(isosceles:\t no)
#		answer = ask user if they want to go again
#		while answer isn't a valid choice:
#			answer = ask user again
#End
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#Allows the main while loop to start
Answer = "y"

while Answer=="Yes" or Answer=="yes" or Answer=="y" or Answer=="Y":
# Asking for the first two angles
	angle1 = int(input("What is the first angle? "))
	angle2 = int(input("What is the second angle? "))

#A while loop checks the angles to see if they work in a triangle
	while (angle1+angle2)>179:
		print("Error, please enter the angles again.")
		angle1 = int(input("What is the first angle? "))
		angle2 = int(input("What is the second angle? "))
		
# Getting the third angle	
	angle3=180-(angle1+angle2)
# if any of the angles = 90, it's a right triangle	
	if angle1==90 or angle2==90 or angle3==90:
		print("Right:\t\t yes")
	else:
		print("Right:\t\t no")
# if any of the angles are greater than 90, it's an obtuse triangle		
	if angle1>90 or angle2>90 or angle3>90:
		print("Obtuse:\t\t yes")
	else:
		print("Obtuse:\t\t no")
# if all of the angles are less than 90, then it's an acute triangle
	if angle1<90 and angle2<90 and angle3<90:
		print("Acute:\t\t yes")
	else:
		print("Acute:\t\t no")
# if all of the angles are equal, it's an equilateral triangle		
	if angle1==angle2 and angle2==angle3:
		print("Equilateral:\t yes")
	else:
		print("Equilateral:\t no")
# if any two angles are equal, it's an isosceles triangle
	if angle1==angle2 or angle1==angle3 or angle2==angle3:
		print("Isosceles:\t yes")
	else:
		print("Isosceles:\t no")
#Sets the while loop up to go again or not
	Answer = input("Would you like to put in another triangle? ")
#Restricts the input
	while Answer!="" and Answer!="No" and Answer !="no" and Answer!="n" \
	and Answer!="N" and Answer!="Yes" and Answer!="yes" and Answer!="y" \
	and Answer!="Y":
			Answer=input("What was that again? ")
	
