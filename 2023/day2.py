import pandas as pd
import re

def read_file():
    df = pd.read_csv(filepath_or_buffer='day2_indata.txt',header=None,delimiter=':')
    return df

maxDictionary = {'red':12,'green':13,'blue':14}

def anyAboveMax(red, green, blue):
    return (
            (max(red) > maxDictionary['red']) or 
            (max(green) > maxDictionary['green']) or 
            (max(blue) > maxDictionary['blue'])
            )

def main():
    df = read_file()
    df.columns = ['ID','data']
    df['ID'] = df['ID'].map(lambda x: x[5:])
    #df['data'].map(isPossible)
    df['reds'] = df['data'].map(lambda s: map(int, re.findall(r'(\d+) red', s)))
    df['greens'] = df['data'].map(lambda s: map(int, re.findall(r'(\d+) green', s)))
    df['blues'] = df['data'].map(lambda s: map(int, re.findall(r'(\d+) blue', s)))
    df['exceedsMax'] = df.apply(lambda row: anyAboveMax(row['reds'],row['greens'],row['blues']), axis=1)

    print(df)
    print(df[df['exceedsMax'] == False]['ID'].map(int).sum())

if __name__ == '__main__':
    main()