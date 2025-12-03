import pandas as pd

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day2_testdata.txt',header=None,delimiter='-',dtype=str,engine='c',lineterminator=',',names=['low', 'high'])
    df = pd.read_csv(filepath_or_buffer='inputs/day2_indata.txt',header=None,delimiter='-',dtype=str,engine='c',lineterminator=',',names=['low', 'high'])
    return df

def testing(x):
    low, high = x
    repeatedTwice = []

    for i in range(int(low),int(high)+1):
        stringI = str(i)
        stringLength = len(stringI)
        if (stringLength % 2) != 0:
            continue

        part1 = stringI[0:stringLength//2]
        part2 = stringI[stringLength//2:]
        if part1 == part2:
            repeatedTwice.append(int(stringI))

    return repeatedTwice


def main():
    df = read_file()
    
    df['InvalidIDs'] = df[['low','high']].apply(lambda x: testing(x), axis=1)
    df['sumsOfInvalids'] = df['InvalidIDs'].map(lambda x: sum(x))
    #print(df)
    print(df['sumsOfInvalids'].sum())

if __name__ == '__main__':
    main()