# Distance.py imports the distance data and contains various methods for calculating distances and times.  It also
# contains the algorithm used to optimize the truck distances, optimizeDeliveries.

import csv
import datetime
import re

with open('DistanceTable.csv') as dtCSV:
    dTable = csv.reader(dtCSV, delimiter=',')
    dist = []
    loc = []

    # Generates two tables, one that will be used for distances, one that will be used for addresses
    # O(N) complexity
    for row in dTable:
        dist.append(row)
        loc.append(row)

    # Deletes unnecessary values from dist table
    # O(N) complexity
    for i in range(len(dist)):
        del (dist[i][0])
        del (dist[i][0])

    # Remove unnecessary item from loc and generate new locList array.
    locList = loc.pop(0)

    # Remove unnecessary item from dist
    dist.pop(0)

    # This for loop parses the strings in the locList array for only the street address portion (i.e., '1330 2100 S')
    # O(N) complexity
    for i in range(len(locList)):
        j = locList[i]
        k = re.search(r"\d", j)
        locList[i] = locList[i][k.start():]


    # This method uses two street address strings as input, uses them to obtain the numerical indices where they are
    # are located in the locList array, and then finds the corresponding distance value in the dist array
    # based on the numerical indices.
    # O(1) complexity
    def getDistance(start, end):
        a = locList.index(start)
        b = locList.index(end)
        if dist[a][b] == '':
            distance = dist[b][a]
        else:
            distance = dist[a][b]
        distFloat = float(distance)
        return distFloat

    # Define start times for trucks and initialize lists of times with the start times.
    startTruck1 = '08:00:00'
    # (h, m, s) = startTruck1.split(':')
    # startTruck1F = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    startTruck2 = '09:05:00'
    # (h, m, s) = startTruck2.split(':')
    # startTruck2F = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    startTruck3 = '13:00:00'
    # (h, m, s) = startTruck3.split(':')
    # startTruck3F = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    truck1TimeList = [startTruck1]
    truck2TimeList = [startTruck2]
    truck3TimeList = [startTruck3]

    # Converts a time from a string to a float value
    # O(1) complexity
    def convertTimeToFloat(time_str):
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    # Converts a float value to a time string
    # O(1) complexity
    def convertFloatToTime(dist):
        time = '{0:02.0f}:{1:02.0f}'.format(*divmod(dist * 60, 60))
        timeFinal = time + ":00"
        return timeFinal

    # truck1Time, truck2Time, and truck3Time determine the time a truck has travelled based on the distance
    # travelled as a sum of timedelta objects.
    # All three have O(N) complexity
    def truck1Time(dist):
        newTime = dist / 18
        distinMinutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(newTime * 60, 60))
        finalTime = distinMinutes + ':00'
        truck1TimeList.append(finalTime)
        sum = datetime.timedelta()
        for i in truck1TimeList:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    def truck2Time(dist):
        newTime = dist / 18
        distinMinutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(newTime * 60, 60))
        finalTime = distinMinutes + ':00'
        truck2TimeList.append(finalTime)
        sum = datetime.timedelta()
        for i in truck2TimeList:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    def truck3Time(dist):
        newTime = dist / 18
        distinMinutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(newTime * 60, 60))
        finalTime = distinMinutes + ':00'
        truck3TimeList.append(finalTime)
        sum = datetime.timedelta()
        for i in truck3TimeList:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    # Get the distance a truck has travelled based on a provided time
    # O(1) complexity
    def truckDistance(time):
        timeDistance = convertTimeToFloat(time) * 18 / 3600
        return timeDistance

    # Get the total distance a truck has travelled (used recursively)
    # O(1) complexity
    def getTotalDistance(row, col, distSum):
        a = locList.index(row)
        b = locList.index(col)
        distance = dist[a][b]
        if distance == '':
            distance = dist[b][a]
        distSum += float(distance)
        return distSum

    # Gets the list of shortened addresses
    # O(1) complexity
    def getAddress():
        return locList

    # Initialize the arrays which will hold the sorted lists of packages.
    truck1GreedyList = []
    truck2GreedyList = []
    truck3GreedyList = []


    # Calculate distance for trucks --> Greedy Algorithm
    # Takes an unsorted list of packages, truck number, and current location of the given truck (location updates with
    # each recursive call.  The algorithm searches through all possible points to determine the lowest value.  When
    # the lowest value is found, that package is added to the sorted list.  The package is then removed from the 
    # unsorted list for the next loop.
    # This algorithm has O(N) complexity
    def optimizeDeliveries(unsortedList, truckNumber, truckLocation):

        # Breaks the recursion when all packages have been sorted.
        if len(unsortedList) == 0:
            return (unsortedList)
        else:
            try:
                # arbitrary value
                val = 100

                # Initialize nextLocation and nextPackage values
                nextLocation = 0
                nextPackage = []

                # Loops through all packages to find the lowest distance between the current location and all possible
                # package delivery locations.  At the conclusion of the loop, the closest next delivery location is
                # assigned to nextLocation.
                for i in unsortedList:
                    if getDistance(truckLocation, i[1]) <= val:
                        val = getDistance(truckLocation, i[1])
                        nextLocation = i[1]
                        nextPackage = i

                # The next package is appended to the sorted list corresponding to the truck.  The package is removed
                # from the unsorted list.  The truck location is then updated and the method is recursively called.
                if truckNumber == 1:
                    truck1GreedyList.append(nextPackage)
                    unsortedList.pop(unsortedList.index(nextPackage))
                    truckLocation = nextLocation
                    optimizeDeliveries(unsortedList, 1, truckLocation)
                elif truckNumber == 2:
                    truck2GreedyList.append(nextPackage)
                    unsortedList.pop(unsortedList.index(nextPackage))
                    truckLocation = nextLocation
                    optimizeDeliveries(unsortedList, 2, truckLocation)
                elif truckNumber == 3:
                    truck3GreedyList.append(nextPackage)
                    unsortedList.pop(unsortedList.index(nextPackage))
                    truckLocation = nextLocation
                    optimizeDeliveries(unsortedList, 3, truckLocation)
            except IndexError:
                pass

    # Getter methods for the sorted list
    # O(1) complexity
    def getTruck1GreedyList():
        return truck1GreedyList

    def getTruck2GreedyList():
        return truck2GreedyList

    def getTruck3GreedyList():
        return truck3GreedyList
