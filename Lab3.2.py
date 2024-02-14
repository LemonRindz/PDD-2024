#Imani Hollie 01.23.2024
#This program will collect item total (item total, state and county taxes, total tax, and sale total)

#Input---------------------------------------------------------------------------------------------
totalItems = float(input('Enter Total Amount for Items: '))

#Calculations--------------------------------------------------------------------------------------
#stateSTax; State Sales Tax = 2%
stateSTax = totalItems * 0.02
#countySTax; County Sales Tax = 4%
countySTax = totalItems * 0.04
#salesTax = Total Sales Taxes combined
salesTax = stateSTax + countySTax
totalSale = totalItems + salesTax

#Output--------------------------------------------------------------------------------------------
print('Item Total: $', totalItems)
print('State Tax:', stateSTax)
print('County Tax:', countySTax)
print('Tax Total: $', salesTax)
print('Sale Total: $', totalSale)