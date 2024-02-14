#Imani Hollie 01.23.2024
#This program will collect a sport's teams' information (team name, total wins, and average wins)

#Input---------------------------------------------------------------------------------------------
teamName = input('Enter team name: ')
year1 = float(input('Enter the total wins for first year: '))
year2 = float(input('Enter the total wins for second year: '))
year3 = float(input('Enter the total wins for third year: '))
year4 = float(input('Enter the total wins for fourth year: '))
year5 = float(input('Enter the total wins for fifth year: '))

#Calculations--------------------------------------------------------------------------------------
totalWins = year1 + year2 + year3 + year4 + year5
avgWins = totalWins / 5

#Output--------------------------------------------------------------------------------------------
print('Your team\'s name is:', teamName)
print(teamName, 'won', totalWins, ' over the past five years.')
print(teamName, 'won an average of', avgWins, ' over the past five years.')