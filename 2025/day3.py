import pandas as pd
from functools import reduce

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day3_testdata.txt',header=None)
    df = pd.read_csv(filepath_or_buffer='inputs/day3_indata.txt',header=None)
    return df

def findHighest(inputString: str):
    maxL = inputString[0]
    maxR = None

    for c in inputString[1:-1]:
        if c > maxL:
            maxL = c
            maxR = None
        elif ((maxR is None) or (c > maxR)):
            maxR = c
    
    if ((maxR is None) or (inputString[-1] > maxR)):
        maxR = inputString[-1]
    
    return (maxL, maxR)

def concatNumbers(x):
    (a,b) = x
    return a+b

def main():
    df = read_file()
    df.columns = ['data']
    df['data'] = df.data.astype(str)

    df['highestNumbers'] = df['data'].map(findHighest)
    df['highNumber'] = df['highestNumbers'].map(lambda x: concatNumbers(x))
    df['highNumber'] = df['highNumber'].map(int)
    print(df)
    print(df['highNumber'].sum())

if __name__ == '__main__':
    main()