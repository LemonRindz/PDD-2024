#Imani Hollie 01.23.2024
#This program will collect square feet (sq ft) of land (total sq ft and total acres)

#Input---------------------------------------------------------------------------------------------
totalSqFt = float(input('Enter Total Square Feet: '))

#Calculations--------------------------------------------------------------------------------------
totalAcres = totalSqFt / 43560

#Output--------------------------------------------------------------------------------------------
print('Total Squared Feet Entered: ', totalSqFt, 'sq ft')
print('Total Acres Calculated: ', totalAcres, 'ac')