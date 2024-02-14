#Imani Hollie 01.22.2024
#This program will collect basic student information (name, degree, credits needed, and credits taken)

#Use the pound '#' sign to comment, Python will ignore everything after it

#Input---------------------------------------------------------------------------------------------
#Use the 'input' function for strings: variable = input(prompt)
studentName = input('Enter student name: ')
degreeName = input('Enter your degree: ')

#You can convert strings to a numeric type using 'int()'
#Use the 'float' function since credits can be partial: variable = float(input(prompt))
creditsDegree = float(input('Enter the total credits needed to graduate: '))

#Use a forward slash '\' for apostrophes since Python can't read them
creditsTaken = float(input('Enter the total credits you\'ve taken so far: '))

#Calculations--------------------------------------------------------------------------------------
#Python reads calculations from left to right.
creditsLeft = creditsDegree - creditsTaken

#Output--------------------------------------------------------------------------------------------
#To display output in Python use the 'print' function: print(result)
print('Your name is:', studentName)
print('Your program is:', degreeName)
print('You need', creditsLeft, 'credits to graduate.')