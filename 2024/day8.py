

def read_file():
    f = open('inputs/day8_indata.txt', 'r')
    #f = open('day8_testdata.txt', 'r')

    l = []
    while True:
        s = f.readline().strip()
        if s is None or s == '':
            return l
        listS = [c for c in s]
        l.append(listS) 

class Pos:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x},{self.y})'

def printMap(map):
    for l in map:
        print("".join(l))

def main():
    listOfStrings = read_file()

    printMap(listOfStrings)

    antennas = {}
    maxX = len(listOfStrings[0])
    maxY = len(listOfStrings)

    antinodeMap = [['.' for i in range(maxY)] for j in range(maxX)]

    for y,l in enumerate(listOfStrings):
        for x,c in enumerate(l):
            if c != '.':
                antennaPositions = antennas[c] if c in antennas else []
                antennaPositions.append(Pos(x,y))
                antennas[c] = antennaPositions

    print(antennas)
    
    for positions in antennas.values():
        if len(positions) < 2:
            continue
        for pos in positions:
            for comp in positions:
                if pos == comp:
                    continue
                antiX = pos.x + (pos.x - comp.x)
                antiY = pos.y + (pos.y - comp.y)
                #print(f'pos:{pos}\tcomp:{comp}\tanti:({antiX},{antiY})')
                if antiX >= 0 and antiX < maxX and antiY >= 0 and antiY < maxY:
                    antinodeMap[antiX][antiY] = '#'

    antinodeMap2 = [['.' for i in range(maxY)] for j in range(maxX)]

    for positions in antennas.values():
        if len(positions) < 2:
            continue
        for i, pos in enumerate(positions):
            for comp in positions[i+1:]:
                diffX = pos.x - comp.x
                diffY = pos.y - comp.y
                antiX = pos.x
                antiY = pos.y
                while True:
                    antiX = antiX - diffX
                    antiY = antiY - diffY
                    #print(f'pos:{pos}\tcomp:{comp}\tanti:({antiX},{antiY})')
                    if antiX >= 0 and antiY >= 0 and antiX < maxX and antiY < maxY:
                        antinodeMap2[antiX][antiY] = '#'
                    else:
                        break
                antiX = comp.x
                antiY = comp.y
                while True:
                    antiX = antiX + diffX
                    antiY = antiY + diffY
                    if antiX >= 0 and antiY >= 0 and antiX < maxX and antiY < maxY:
                        antinodeMap2[antiX][antiY] = '#'
                    else:
                        break
                antinodeMap2[pos.x][pos.y]
                antinodeMap2[comp.x][comp.y]

    antiNodes = 0
    for l in antinodeMap:
        for c in l:
            if c == '#':
                antiNodes += 1
    antiNodes2 = 0
    for l in antinodeMap2:
        for c in l:
            if c == '#':
                antiNodes2 += 1
    printMap(antinodeMap)
    print(antiNodes)
    printMap(antinodeMap2)
    print(antiNodes2)

if __name__ == '__main__':
    main()