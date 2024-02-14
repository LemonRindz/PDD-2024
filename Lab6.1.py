#Imani Hollie 02.10.2024
#This program will collect two primary colors
#(primary colors, secondary color, or error)

#Module 1 - main() [Input and Calls mixColor()]
#Inputs--------------------------------------------------------------------------------------------
#Strings can't be floats, so I just used input()
priColor1 = input('Enter Primary Color: ')
priColor2 = input('Enter Different Primary Color: ')

#Module 2 - mixColor [Calculations and Output]
def mixColor(color1, color2):
    #Variables-------------------------------------------------------------------------------------
    #The 'lower()' method converts string to lowercase for case-insensitivity
    color1 = color1.lower()
    color2 = color2.lower()
    #Calculations----------------------------------------------------------------------------------
    #IF-THEN-ELSE decision structure will display secondary color or error message
    #IF color1 = red THEN IF color 2 = yellow/blue THEN display orange/purple
    if color1 == 'red':
        if color2 == 'yellow':
            print(f'The color {color1} mixed with {color2} makes ORANGE')
        elif color2 == 'blue':
            print(f'The color {color1} mixed with {color2} makes PURPLE')
        #End If
    #IF color1 = yellow THEN IF color 2 = red/blue THEN display orange/green
    elif color1 == 'yellow':
        if color2 == 'red':
            print(f'The color {color1} mixed with {color2} makes ORANGE')
        elif color2 == 'blue':
            print(f'The color {color1} mixed with {color2} makes GREEN')
        #End If
    #IF color1 = blue THEN IF color 2 = red/yellow THEN display purple/green
    elif color1 == 'blue':
        if color2 == 'red':
            print(f'The color {color1} mixed with {color2} makes PURPLE')
        elif color2 == 'yellow':
            print(f'The color {color1} mixed with {color2} makes GREEN')
        #If argument passes through - display error message
        else:
            print('ERROR! Valid Entries Include: RED, YELLOW, BLUE')
        #End If
    #End If
#End Module 2

#Calling Module 2 mixColor()---------------------------------------------------------------------
mixColor(priColor1, priColor2)
#Output is then printed to the screen.

#End Module 1