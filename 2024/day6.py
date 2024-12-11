def read_file():
    f = open('inputs/day6_indata.txt', 'r')
    #f = open('day6_testdata.txt', 'r')
    ll = []
    
    while True:
        l = list(f.readline().strip())
        if l is None or l == '' or l == []:
            return ll
        ll.append(l)

class Guard:
    def __init__(self, index, pos, startingChar):
        self.directions = {'up': (-1,0), 'right':(0,1),'down':(1,0),'left':(0,-1)}
        self.index = index
        self.pos = pos
        translation = {'^':'up', '>':'right', 'v':'down', '<':'left'}
        self.directionName = translation[startingChar]
        self.direction = self.directions[self.directionName]

    def nextStep(self):
        return self.index + self.direction[0], self.pos + self.direction[1]

    def move(self):
        self.index, self.pos = self.nextStep()

    def turnRight(self):
        directionList = list(self.directions.keys())
        nextDirection = (directionList.index(self.directionName)+1)%4
        self.directionName = directionList[nextDirection]
        self.direction = self.directions[self.directionName]


    def __str__(self):
        return f'At [{self.index+1}, {self.pos+1}] going in direction {self.direction}'

def checkIndexInRange(listOfStrings, index):
    return index in range(0,len(listOfStrings))

def checkPosInString(s, pos):
    return pos in range(0, len(s))

def getLetter(listOfStrings, index, pos):
    if checkIndexInRange(listOfStrings, index):
        s = listOfStrings[index]
        if checkPosInString(s, pos):
            return s[pos]
    return None

def setLetter(listOfStrings, index, pos, letter):
    listOfStrings[index][pos] = letter

def findStart(listOfStrings):
    for i, s in enumerate(listOfStrings):
        for j, c in enumerate(s):
            if c in ['^', '<', '>', 'v']:
                return i, j, c

def printMap(listOfStrings):
    for l in listOfStrings:
        print("".join(l))

def main():
    listOfStrings = read_file()

    string_index, pos, c = findStart(listOfStrings)
    guard = Guard(string_index, pos, c)

    while True:
        nextIndex, nextPos = guard.nextStep()
        letter = getLetter(listOfStrings, nextIndex, nextPos)
        if letter == None:
            setLetter(listOfStrings, guard.index, guard.pos, 'X')
            print('Done')
            break
        elif letter == '#':
            guard.turnRight()
        else:
            setLetter(listOfStrings, guard.index, guard.pos, 'X')
            guard.move()

    printMap(listOfStrings)

    countX = 0
    for l in listOfStrings:
        for c in l:
            countX += 1 if c == 'X' else 0

    print(countX)

    
if __name__ == '__main__':
    main()