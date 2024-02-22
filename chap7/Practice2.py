#Imani Hollie 02/21/24
#Range Practice

#DEFINE FUNCTION
def getHours():
    hour = float(input('Enter Total Hours: '))
    return hour 
def getRate():
    rate = float(input('Enter Rate: '))
    return rate

hour = getHours()
rate = getRate()

def checkhours(hour):
    if(hour > 0 and hour <= 40):
        checkrate(rate)
    else:
         getHours()
         checkhours(hour)

def checkrate(rate):
    if(rate >= 7.50 and rate <= 18.25):
        print(f'Gross Pay is: ${rate * hour}')
    else:
         getRate()
         checkrate(rate)