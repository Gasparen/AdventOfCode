import pandas as pd
from functools import reduce

def read_files():
    df = pd.read_csv(filepath_or_buffer='inputs\day15_indata.csv', header=None,lineterminator=',')
    return df

def hash_function(currentValue:int, i:int) -> int:
    return ((currentValue+i)*17)%256

def main():
    df = read_files()
    df.columns = ['data']
    df['asciiValues'] = df['data'].apply(lambda s: list(map(lambda c: ord(c), s)))
    df['hashedValue'] = df['asciiValues'].apply(lambda l:reduce(hash_function, l, 0))

    print(df)
    print(df['hashedValue'].sum())

if __name__ == '__main__':
    main()