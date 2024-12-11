import pandas as pd

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day7_testdata.txt',header=None,delimiter=':')
    df = pd.read_csv(filepath_or_buffer='inputs/day7_indata.txt',header=None,delimiter=':')
    return df

def calculate(target, stringOfNumbers):
    listOfNumbers = list(map(int, stringOfNumbers.split()))

    results = [listOfNumbers[0]]
    for i in range(1,len(listOfNumbers)):
        addFactorNumber = listOfNumbers[i]
        nextResults = []
        for j in range(0,len(results)):
            newSum = results[j] + addFactorNumber
            newProduct =  results[j] * addFactorNumber
            if newSum <= target:
                nextResults.append(newSum)
            if newProduct <= target:
                nextResults.append(newProduct)
        results = nextResults

    return results

def calculate2(target, stringOfNumbers):
    listOfNumbers = list(map(int, stringOfNumbers.split()))

    results = [listOfNumbers[0]]
    for i in range(1,len(listOfNumbers)):
        addFactorNumber = listOfNumbers[i]
        nextResults = []
        for j in range(0,len(results)):
            newSum = results[j] + addFactorNumber
            newProduct =  results[j] * addFactorNumber
            newConcat = int(f'{results[j]}{addFactorNumber}')
            if newSum <= target:
                nextResults.append(newSum)
            if newProduct <= target:
                nextResults.append(newProduct)
            if newConcat <= target:
                nextResults.append(newConcat)
        results = nextResults

    return results

def main():
    df = read_file()
    df.columns = ['target', 'numbers']
    df['target'] = df['target'].map(int)
    df['result'] = df.apply(lambda row: calculate(row['target'], row['numbers']), axis=1)
    df['result2'] = df.apply(lambda row: calculate2(row['target'], row['numbers']), axis=1)
    df['hitTarget'] = df.apply(lambda row: row['target'] in row['result'], axis=1)
    df['hitTarget2'] = df.apply(lambda row: row['target'] in row['result2'], axis=1)

    print(df)
    print(df[df['hitTarget']==True]['target'].sum())
    print(df[df['hitTarget2']==True]['target'].sum())
    
if __name__ == '__main__':
    main()