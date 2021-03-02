# ImportData.py imports the package data, inserts it into the hash table, and sorts packages into trucks
# (but does not optimize).

import csv
from HashTable import HashMap

with open('PackageFile.csv') as pkgCSV:
    pTable = csv.reader(pkgCSV, delimiter=',')
    packages = []

    # Generates hash table object
    pHashTable = HashMap()

    # Initializes lists of packages for trucks
    truck1 = []
    truck2 = []
    truck3 = []

    # Generates list of packages from CSV file
    for row in pTable:
        packages.append(row)

    # Creates empty elements that will later hold delivery time information
    # O(N) complexity
    for i in range(len(packages)):
        packages[i].append('')
        packages[i].append('')

    # Corrects a value in first element
    packages[0][0] = '1'

    # Inserts packages into the hash table using the package ID as a key and the package information as a value
    # O(N) complexity
    for i in range(len(packages)):
        key = packages[i][0]
        value = packages[i]
        pHashTable.insert(key, value)

    # This for loop sorts packages with specific restrictions into trucks
    # O(N) complexity
    for i in range(len(packages)):
        note = 7
        deadline = 5
        if 'truck 2' in packages[i][note]:
            truck2.append(packages[i])
        if 'EOD' in packages[i][deadline] and 'until 9:05 am' in packages[i][note]:
            truck2.append(packages[i])
        if 'EOD' not in packages[i][deadline] and 'truck 2' not in packages[i][note]:
            if "Delayed" in packages[i][note]:
                truck2.append(packages[i])
            else:
                truck1.append(packages[i])
        if 'Must' in packages[i][note] and packages[i] not in truck2:
            truck1.append(packages[i])
        if 'Wrong' in packages[i][note]:
            packages[i][1] = '410 S State St'
            packages[i][2] = 'Salt Lake City'
            packages[i][3] = 'UT'
            packages[i][4] = '84111'
            truck3.append(packages[i])

    # This for loop sorts the remaining packages into trucks, keeping the total 16/truck or less.
    # O(N) complexity
    for i in range(len(packages)):
        if packages[i] not in truck1 and packages[i] not in truck2 and packages[i] not in truck3:
            if len(truck1) < 16:
                truck1.append(packages[i])
            elif len(truck2) < 16:
                truck2.append(packages[i])
            else:
                truck3.append(packages[i])

    # Getter functions for the hash table and package lists.
    # O(1) complexity for all
    def getHashMap():
        return pHashTable

    def truck1PackageList():
        return truck1

    def truck2PackageList():
        return truck2

    def truck3PackageList():
        return truck3
