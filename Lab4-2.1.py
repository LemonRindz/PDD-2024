#Imani Hollie 02.02.2024
#This program will collect total replacement cost for property
#(replacement total and min. insurance coverage)

#Module 1 - main() [Input and Calls minIns()]
totalCost = float(input('Enter Total Replacement Cost for Property: '))

#Module 2 - minIns() [Calculations and Output]
def minIns(Cost):
    #Calculations----------------------------------------------------------------------------------
    minInsCov = Cost * 0.8
    #Output----------------------------------------------------------------------------------------
    print('Total Replacement Cost:', Cost)
    print('Minimum Insurance Cost:', minInsCov)
    #Output is then printed to the screen
#End Module 2

minIns(totalCost)
#End Module 1