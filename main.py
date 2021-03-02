# Main.py provides the user interface for the program and displays information for the user.
# Trevor Ross, tros114@wgu.edu, Student ID: 001388692

from Package import *
from ImportData import getHashMap
import datetime


class Main:
    # Indicates program is starting
    print('Starting up tracking system...')
    # Provides total distance travelled by trucks
    print('--- WGU PARCEL SERVICE TRACKING SYSTEM ---')
    print('Packages were successfully delivered in', "{0:.2f}".format(totalDistance(), 1), 'miles.')
    # Prompts user for input
    prompt = input('\nPlease type one of the following options: \n'
                  '"package" - Search for package by package ID number \n'
                  '"status" - view status of all packages at a specific time \n'
                  '"exit" - exit program \n'
                   '---->')



    # Simple method to format a time string as a timedelta object
    # O(1) complexity
    def formatTime(timeString):
        (h, m, s) = timeString.split(':')
        formattedTime = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        return formattedTime

    # Prints the information associated with a package
    # O(1) complexity
    def printInformation(id):
        print('Package ID:', getHashMap().lookup(str(id))[0], '-- Address:', getHashMap().lookup(str(id))[1],
            '-- City:', getHashMap().lookup(str(id))[2], '-- Zip Code:', getHashMap().lookup(str(id))[4],
            '-- Deadline:', getHashMap().lookup(str(id))[5],
        '-- Weight:', getHashMap().lookup(str(id))[6], 'pounds')

    # Prints the information associated with a package and includes the current status based on a given time parameter
    # O(1) complexity
    def printInformationStatus(id, checkTime):
        deliveryTime = (getHashMap().lookup(str(id))[9])
        startTime = (getHashMap().lookup(str(id))[8])
        (h, m, s) = deliveryTime.split(':')
        deliveryTimeF = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        if deliveryTimeF >= checkTime and startTime >= checkTime:
            status = 'At Hub'
        elif deliveryTimeF >= checkTime and startTime <= checkTime:
            status = 'En Route'
        else:
            status = 'Delivered'

        print('Package ID:', getHashMap().lookup(str(id))[0], '-- Status:', status, '-- Address:', getHashMap().lookup(str(id))[1],
              '-- City:', getHashMap().lookup(str(id))[2], '-- Zip Code:', getHashMap().lookup(str(id))[4],
              '-- Deadline:', getHashMap().lookup(str(id))[5],
              '-- Weight:', getHashMap().lookup(str(id))[6], 'pounds')

    while prompt != 'exit':
        # Takes a package ID and a time as a string and provides a package status, as well as all package information
        # O(1) complexity
        if prompt == 'package':
            id = input('Enter Package ID: ')
            time = input('Enter the time you wish to view the package status (HH:MM:SS): ')
            time1 = str(getHashMap().lookup(str(id))[8])
            time2 = str(getHashMap().lookup(str(id))[9])
            timeF = formatTime(time)
            time1F = formatTime(time1)
            time2F = formatTime(time2)

            if time2F >= timeF and timeF >= time1F:
                print('Status: Package is en route.  Left hub at ' +str(time1F))
                printInformation(id)

            elif time2F >= timeF:
                print('Status: Package is at Hub. Expected to leave at ' +str(time1F))
                printInformation(id)

            else:
                print('Status: Package delivered at ' +str(time2F))
                printInformation(id)

        # Provides information for all packages at a given time
        # O(N) complexity
        if prompt == 'status':

            time = input('Enter a time to check status of packages (HH:MM:SS): ')

            for i in range(len(packages)+1):
                if i != 0:
                    time1 = str(getHashMap().lookup(str(i))[8])
                    time2 = str(getHashMap().lookup(str(i))[9])
                    timeF = formatTime(time)
                    time1F = formatTime(time1)
                    time2F = formatTime(time2)
                    printInformationStatus(packages[i-1][0], timeF)

            prompt = ''

        # Exits the program
        # O(1) complexity
        elif prompt == 'exit':
            print('Exiting Program')
            exit()

        # Provides an error message and exits the program
        # O(1) complexity
        else:
            prompt = input('\nPlease type one of the following options: \n'
                  '"package" - Search for package by package ID number \n'
                  '"status" - view status of all packages at a specific time \n'
                  '"exit" - exit program \n'
                   '---->')

