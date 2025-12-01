def read_file():
    f = open('inputs/day1_indata.txt', 'r')
    #f = open('day1_testdata.txt', 'r')
    ll = []
    
    while True:
        l = f.readline().strip()
        if l is None or l == '' or l == []:
            return ll
        ll.append(l)

def iterativeCount(listOfStrings: list[str], count, state):
    for item1 in listOfStrings:
        direction = item1[0]
        clicks = int(item1[1:])
        state += (clicks if direction == 'R' else -clicks)
        state = state % 100
        if state == 0:
            count += 1
    
    return count

def iterativeSpecialCount(listOfStrings: list[str], count, state):
    for item1 in listOfStrings:
        direction = item1[0]
        clicks = int(item1[1:])
        #print('\n------\nPre move\n------')
        #print('State: ', state, '\nDirection: ', direction, 'Clicks: ', clicks)
        if state == 0 and direction == 'L':
            state = 100
        state += (clicks if direction == 'R' else -clicks)
        #print('------\nPost move\n------')
        #print('State: ', state, '\nCount: ', count)
        while state < 0:
            state += 100
            count += 1
        #print('------\n Post Negative While \n------')
        #print('State: ', state, '\nCount: ', count)
        while state > 100:
            state -= 100
            count += 1
        #print('------\n Post Positive While \n------')
        #print('State: ', state, '\nCount: ', count)
        state = state % 100
        if state == 0:
            count += 1
    
    return count

def main():
    listOfStrings = read_file()
    
    print(listOfStrings)
    total0counts = iterativeCount(listOfStrings, 0, 50)
    totalSpecial0counts = iterativeSpecialCount(listOfStrings, 0, 50)
    print(total0counts)
    print(totalSpecial0counts)


if __name__ == '__main__':
    main()