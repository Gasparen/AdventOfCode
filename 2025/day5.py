def read_file():
    f = open('inputs/day5_indata.txt', 'r')
    # f = open('day5_testdata.txt', 'r')
    ranges = []
    indexes = []
    
    l = f.readline()
    while l != '\n':
        ranges.append(l.strip())
        l = f.readline()
    while True:
        l = f.readline()
        if l is None or l == '':
            return ranges, indexes
        indexes.append(int(l.strip()))

def getMinMax(s: str):
    splitIndex = s.find('-')
    min = s[:splitIndex]
    max = s[splitIndex+1:]
    return (int(min), int(max))


def main():
    ranges, indexes = read_file()

    fresh = 0
    ranges = list(map(getMinMax, ranges))
    for i in indexes:
        for (min, max) in ranges:
            if min <= i <= max:
                fresh += 1
                break

    print(fresh)

if __name__ == '__main__':
    main()