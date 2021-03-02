# Package.py handles the package sorting for delivery, truck distance calculations, and delivery time calculations.
# It calls optimizeDeliveries to sort the packages for delivery in each truck.  It also calculates the distance
# each truck travels and delivery times of packages.  The hash table is updated with the delivery time for each package.

from Distance import *
from ImportData import *

import datetime

# Simple method to obtain a timedelta from a string in (HH:MM:SS) format
# Space-time complexity O(1)
def convertTime(time):
    h, m, s = time.split(':')
    convertedTime = datetime.timedelta(hours=int(h), minutes=int(m), seconds = int(s))
    return convertedTime

# Predefined start times for trucks from Distance.py
truck1StartTimeString = startTruck1
truck2StartTimeString = startTruck2
truck3StartTimeString = startTruck3

# Generates timedelta objects for the time strings
truck1StartTime = convertTime(truck1StartTimeString)
truck2StartTime = convertTime(truck2StartTimeString)
truck3StartTime = convertTime(truck3StartTimeString)

# This method generates a list of start times for all packages on a truck.
# Space-time complexity O(N)
def updateStatus(packageList, truckStartTime):
    deliveryList = []
    for i in range(len(packageList)):
        packageList[i][8] = truckStartTime
        deliveryList.append(packageList[i])
    return deliveryList

# Updates the start time for all packages to the time the trucks begin their routes.
delivery1 = updateStatus(truck1PackageList(), truck1StartTime)
delivery2 = updateStatus(truck2PackageList(), truck2StartTime)
delivery3 = updateStatus(truck3PackageList(), truck3StartTime)

# Generates the sorted list of packages for each truck via the greedy algorithm, assuming each truck starts at hub.
optimizeDeliveries(truck1PackageList(), 1, getAddress()[0])
optimizeDeliveries(truck2PackageList(), 2, getAddress()[0])
optimizeDeliveries(truck3PackageList(), 3, getAddress()[0])

# These three for loops utilize the getTotalDistance, getDistance, and truck[X]Time methods to calculate the total
# distance travelled by each truck as well as the time at which each package is delivered,
# and update the Hash Tables with the delivery time.
# Space-time complexity for each is O(N)

##### Truck 1
truck1DistanceSum = 0
truck1PkgId = 0
truck1GL = getTruck1GreedyList()
startDistance1 = getDistance(locList[0], truck1GL[0][1])
startTime1 = truck1Time(startDistance1)

for i in range(len(truck1GL)):
    try:
        id = truck1GL[truck1PkgId][0]
        # calculate the total distance of the truck (sums with each loop)
        if i == 0:
            truck1DistanceSum = startDistance1
        else:
            truck1DistanceSum = getTotalDistance(getTruck1GreedyList()[i - 1][1], getTruck1GreedyList()[i][1],
                                                 truck1DistanceSum)
        # calculate the delivery time for each package along the route
        if i != 0:
            delivery = truck1Time(getDistance(getTruck1GreedyList()[i-1][1], getTruck1GreedyList()[i][1]))
        else:
            delivery = truck1Time(startDistance1)
        # Insert the delivery time as a string into the sublist of the package
        truck1GL[i][9] = (str(delivery))
        # Update the hash table value with the newly added delivery time value
        getHashMap().update(int(id), truck1GL[i])
        # Increment the package ID counter (this counter is unnecessary but has not yet been removed)
        truck1PkgId += 1
    except IndexError:
        pass

##### Truck 2
truck2DistanceSum = 0
truck2PkgId = 0
truck2GL = getTruck2GreedyList()
startDistance2 = getDistance(locList[0], truck2GL[0][1])
startTime2 = truck2Time(startDistance2)
for i in range(len(truck2GL)):
    try:
        id = truck2GL[truck2PkgId][0]
        # calculate the total distance of the truck (sums with each loop)
        if i == 0:
            truck2DistanceSum = startDistance2
        else:
            truck2DistanceSum = getTotalDistance(getTruck2GreedyList()[i - 1][1], getTruck2GreedyList()[i][1],
                                                 truck2DistanceSum)
        # calculate the delivery time for each package along the route
        if i != 0:
            delivery = truck2Time(getDistance(getTruck2GreedyList()[i-1][1], getTruck2GreedyList()[i][1]))
        else:
            delivery = truck2Time(startDistance2)
        # Insert the delivery time as a string into the sublist of the package
        truck2GL[i][9] = (str(delivery))
        # Update the hash table value with the newly added delivery time value
        getHashMap().update(int(id), truck2GL[i])
        # Increment the package ID counter (this counter is unnecessary but has not yet been removed)
        truck2PkgId += 1
    except IndexError:
        pass

#### Truck 3
truck3PkgId = 0
truck3GL = getTruck3GreedyList()
startDistance3 = getDistance(locList[0], truck3GL[0][1])
startTime3 = truck3Time(startDistance3)
truck3DistanceSum = startDistance3

for i in range(len(truck3GL)):
    try:
        id = truck3GL[truck3PkgId][0]
        # calculate the total distance of the truck (sums with each loop)
        if i == 0:
            truck3DistanceSum = startDistance3
        else:
            truck3DistanceSum = getTotalDistance(getTruck3GreedyList()[i - 1][1], getTruck3GreedyList()[i][1],
                                                 truck3DistanceSum)
        # calculate the delivery time for each package along the route
        if i != 0:
            delivery = truck3Time(getDistance(getTruck3GreedyList()[i-1][1], getTruck3GreedyList()[i][1]))
        else:
            delivery = truck3Time(startDistance3)
        # Insert the delivery time as a string into the sublist of the package
        truck3GL[i][9] = (str(delivery))
        # Update the hash table value with the newly added delivery time value
        getHashMap().update(int(id), truck3GL[i])
        # Increment the package ID counter (this counter is unnecessary but has not yet been removed)
        truck3PkgId += 1
    except IndexError:
        pass

# Method to calculate the total truck distances
# O(1) complexity
def totalDistance():
    totalDistance = truck1DistanceSum + truck2DistanceSum + truck3DistanceSum
    return totalDistance





