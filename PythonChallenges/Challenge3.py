
import datetime
from pytz import timezone

timeIs ='Today is {}, and the current time in the {} timezone is {}.'



# print(timeIs.format(PortlandTime.strftime('%x'), PortlandTZ, PortlandTime.strftime('%X')))


# print(timeIs.format(LondonTime.strftime('%x'), LondonTZ, LondonTime.strftime('%X')))


# print(timeIs.format(NYCTime.strftime('%x'), NYCTZ, NYCTime.strftime('%X')))

def checkOpen():

    Open = datetime.time(8, 0, 0)
    Close = datetime.time(17, 0, 0)
    Current = datetime.datetime.now(timezone('America/Los_Angeles')).time()
    
    # Portland TZ
    PortlandTZ = timezone('America/Los_Angeles')
    PortlandTime = datetime.datetime.now(PortlandTZ).time()

    # London TZ
    LondonTZ = timezone('Europe/London')
    LondonTime = datetime.datetime.now(LondonTZ).time()

    # NYC TZ
    NYCTZ = timezone('America/New_York')
    NYCTime = datetime.datetime.now(NYCTZ).time()

    timeList = {'Portland':PortlandTime, 'London':LondonTime, 'New York City':NYCTime}
    
    for i in timeList:
        # print(timeList[i])
        if timeList[i] >= Open and timeList[i] < Close:
            print('The ' + i + ' branch is currently open!')
        else:
            print('The ' + i + ' branch is currently closed!')
        

if __name__ == '__main__':
    checkOpen()
