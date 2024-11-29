

def read_file():
    f = open('inputs/day3_indata.txt', 'r')
    #f = open('day3_testdata.txt', 'r')
    directionsString = f.readline()
    return directionsString

def main():
    directions = read_file()
    robo = {'x':0, 'y':0}
    santa = {'x':0, 'y':0}
    
    houses = {'0,0': 1}
    for i,c in enumerate(directions):
        currentSanta = santa if i%2==0 else robo
        match c:
            case '^':
                currentSanta['y']+=1
            case '>':
                currentSanta['x']+=1
            case 'v':
                currentSanta['y']-=1
            case '<':
                currentSanta['x']-=1
        coordinate = f"{currentSanta['x']},{currentSanta['y']}"
        value = houses[coordinate] if coordinate in houses else 0
        houses[coordinate] = value+1
    
    print(len(list(houses.values())))

if __name__ == '__main__':
    main()