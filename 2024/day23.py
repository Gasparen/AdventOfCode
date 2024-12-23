

def read_file():
    f = open('inputs/day23_indata.txt', 'r')
    #f = open('day23_testdata.txt', 'r')
    ll = []
    
    while True:
        l = f.readline().strip()
        if l is None or l == '' or l == []:
            return ll
        ll.append(l)

def addComputer(connectionDict, comp1, comp2):
    connections = connectionDict[comp1] if comp1 in connectionDict else []
    connections.append(comp2)
    connectionDict[comp1] = connections

def findTriplets(comp, connectionDict):
    #print(f'{comp}')
    hop1List = connectionDict[comp]
    triplets = []

    for conn in hop1List:
        hop2List = connectionDict[conn]
        for conn2 in hop2List:
            if conn2 in hop1List:
                newConn = sorted([comp, conn, conn2])
                if newConn not in triplets:
                    triplets.append(newConn)
                #print(comp, conn, conn2)

    return triplets

def main():
    connections = read_file()

    connectionDict = {}
    for con in connections:
        (comp1, comp2) = con.split('-')
        addComputer(connectionDict, comp1, comp2)
        addComputer(connectionDict, comp2, comp1)


    tComputersDict = {}
    tComputers = []
    for k,v in connectionDict.items():
        #print(k, v)
        if k[0] == 't':
            tComputers.append(k)

    print('-------------------------')
    allTrips = []
    for comp in tComputers:
        trips = findTriplets(comp, connectionDict)
        for t in trips:
            if t not in allTrips:
                allTrips.append(t)

    print(allTrips)
    print(len(allTrips))

    print('-------------------------')

if __name__ == '__main__':
    main()