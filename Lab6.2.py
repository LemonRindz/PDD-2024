#Imani Hollie 02.10.2024
#This program will collect package weight
#(package weight, rate per pound, final sale)

#Module 1 - main() [Input and Calls mixColor()]
#Inputs--------------------------------------------------------------------------------------------
totalLbs = float(input('Enter Total Weight (lbs): '))

#Module 2 - totalCost [Calculations and Output]
def totalCost(lbs):
    #Calculations----------------------------------------------------------------------------------
    #IF-THEN-ELSE decision structure will display package weight, shipping rate, and shipping cost
    #if true or an error message if false
    #IF lbs <= (less than or equal to) 2 THEN Display package weight, shipping rate, and total cost
    if lbs <= 2:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound (lbs): $1.10')
        #The '.2f' is used for decimals to limit the decimal places, in this case it's two for cost
        print(f'Shipping Cost: ${lbs * 1.1:.2f}')
    #IF 2 < (less than) lbs <= 6 THEN Display package weight, shipping rate, and total cost
    elif 2 < lbs <= 6:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound (lbs): $2.20')
        print(f'Shipping Cost: ${lbs * 2.2:.2f}')
    #IF 6 < lbs <= 10 THEN Display package weight, shipping rate, and total cost
    elif 6 < lbs <= 10:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound (lbs): $3.70')
        print(f'Shipping Cost: ${lbs * 3.7:.2f}')
    #IF 10 < lbs THEN Display package weight, shipping rate, and total cost
    elif 10 < lbs:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound (lbs): $3.80')
        print(f'Shipping Cost: ${lbs * 3.8:.2f}')
    #If argument passes through - display error message
    else:
        print('ERROR! Enter total weight in pounds (lbs)')
    #End If
#End Module 2

#Calling Module 2 totalCost()----------------------------------------------------------------------
totalCost(totalLbs)
#Output is then printed to the screen.

#End Module 1