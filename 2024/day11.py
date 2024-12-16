

def read_file():
    f = open('inputs/day11_indata.txt', 'r')
    #f = open('day11_testdata.txt', 'r')
    
    l = f.readline().split(' ')

    return l

def blinkAction(value: str):
    if value == '0':
        return '1', None
    if len(value)%2==0:
        midIndex = len(value)//2
        return f'{str(int(value[:midIndex]))}', f'{str(int(value[midIndex:]))}'
    else:
        return str(int(value)*2024), None

def addPrecalc(value, preCalculatedDict, iterationsLeft):
    pass

def iteration(listOfValues: list[str]) -> list[str]:
    newList = []
    
    for v in listOfValues:
        if len(v) == 1:
            pass
        (newValue, splitValue) = blinkAction(v)
        newList.append(newValue)
        if splitValue is not None:
            newList.append(splitValue)

    return newList

def preCalculated():
    preCalcDictionary = {str(k):[str(k)] for k in range(9) }
    print(preCalcDictionary)
    # run for 3 iterations
    """ for i in range(3):
        newList = []
        for v in preCalcDictionary['1']:
            (x,y) = blinkAction(v)
        preCalcDictionary['2']
        preCalcDictionary['3']
        preCalcDictionary['4']
 """
    # "run" for 4 iterations
    # run for 5 iterations
"""     for i in range(5):
        preCalcDictionary['5']
        preCalcDictionary['6']
        preCalcDictionary['7']
        preCalcDictionary['8']
        preCalcDictionary['9']
 """
def main():
    startNumbers = read_file()

    print(startNumbers)

    preCalculated()

    newValues = startNumbers
    for i in range(25):
        newValues = iteration(newValues)
        #print(newValues)

    print(len(newValues))

    #for v in startNumbers:
    #    print(blinkAction(v))
    """     newValue = blinkAction(v)
        if type(newValue) == tuple:
            if len(newValue) == 1:
                
        else:
     """
    
if __name__ == '__main__':
    main()