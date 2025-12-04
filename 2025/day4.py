def read_file():
    f = open('inputs/day4_indata.txt', 'r')
    # f = open('day4_testdata.txt', 'r')
    ll = []
    
    while True:
        l = f.readline()
        if l is None or l == '':
            return ll
        ll.append(l.strip())

def countAdjacent(i, j, listOfStrings):
    adjacentCount = 0
    maxIndexI = len(listOfStrings)-1
    maxIndexJ = len(listOfStrings[0])-1
    startIndexI = i-1 if i-1>=0 else 0
    startIndexJ = j-1 if j-1>=0 else 0
    stopIndexI = i+1 if i+1<=maxIndexI else maxIndexI
    stopIndexJ = j+1 if j+1<=maxIndexJ else maxIndexJ

    for x in range(startIndexI,stopIndexI+1):
        for y in range(startIndexJ,stopIndexJ+1):
            if listOfStrings[x][y] != '.':
                adjacentCount += 1

    return adjacentCount-1 # Counts its own square, so remove that hit

def printMap(listOfStrings):
    for l in listOfStrings:
        print("".join(l))

def iterateRemoval(listOfStrings):
    listOfStringsCopy = []
    accessablePaperRolls = 0

    for i, s in enumerate(listOfStrings):
        rowString = ''
        for j , c in enumerate(s):
            addChar = c
            if (c=='@'):
                rollsAdjacent = countAdjacent(i, j, listOfStrings)
                if rollsAdjacent < 4:
                    accessablePaperRolls += 1
                    addChar = '.'
            rowString += addChar

        listOfStringsCopy.append(rowString)
    return accessablePaperRolls, listOfStringsCopy

def main():
    newState = read_file()
    totalPaperRollsRemoved = 0
    iterationRemovedRolls = 1 # goto while loop
    
    while iterationRemovedRolls > 0:
        #printMap(newState)
        iterationRemovedRolls, newState = iterateRemoval(newState)
        totalPaperRollsRemoved += iterationRemovedRolls
        #print(totalPaperRollsRemoved, iterationRemovedRolls)
   
    printMap(newState)
    print(totalPaperRollsRemoved)

if __name__ == '__main__':
    main()