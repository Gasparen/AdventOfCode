

def read_file():
    f = open('inputs/day3_indata.txt', 'r')
    #f = open('day3_testdata.txt', 'r')
    directionsString = f.readline()
    return directionsString

def main():
    directions = read_file()
    x = y = 0
    houses = {'0,0': 1}
    for c in directions:
        match c:
            case '^':
                y+=1
            case '>':
                x+=1
            case 'v':
                y-=1
            case '<':
                x-=1
        coordinate = f"{x},{y}"
        value = houses[coordinate] if coordinate in houses else 0
        #print(f"c: {c} => x,y: {x},{y}")
        houses[f"{x},{y}"] = value+1

    print(houses)
    
    print(len(list(houses.values())))

if __name__ == '__main__':
    main()