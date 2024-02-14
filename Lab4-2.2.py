#Imani Hollie 02.02.2024
#This program will collect total seats sold per class
#(total seats sold per class, total seats sold,
#total cost per class, total sales made)

#Module 1 - main() [Input and Calls totalCost()]
#Inputs--------------------------------------------------------------------------------------------
aSeat = float(input('Enter Total Class A Tickets Sold: '))
bSeat = float(input('Enter Total Class B Tickets Sold: '))
cSeat = float(input('Enter Total Class C Tickets Sold: '))

#Module 2 - totaSales() [Calculations and Output]
def totalSales(classA, classB, classC):
    #Calculations----------------------------------------------------------------------------------
    totalSeats = classA + classB + classC
    aSale = classA * 15
    bSale = classB * 12
    cSale = classC * 9
    totalSales = classA + classB + classC
    #Output----------------------------------------------------------------------------------------
    print(f'Total Class A Seats: {classA}')
    print(f'Total Class B Seats: {classB}')
    print(f'Total Class C Seats: {classC}')
    print(f'Total Seats Sold: {totalSeats}')
    print(f'Total Class A Sales: ${aSale}')
    print(f'Total Class B Sales: ${bSale}')
    print(f'Total Class C Sales: ${cSale}')
    print(f'Total Sales Cost: ${totalSales}')
    #Output is then printed to the screen
#End Module 2

#Calling Module 2 totalSales()---------------------------------------------------------------------
totalSales(aSeat, bSeat, cSeat)
#End Module 1