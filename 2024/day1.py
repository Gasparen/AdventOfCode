import pandas as pd

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day1_testdata.txt',header=None,delimiter=' ')
    df = pd.read_csv(filepath_or_buffer='inputs/day1_indata.txt',header=None,delimiter=' ')
    df = df.dropna(axis=1, how='all')
    return df

def main():
    df = read_file()
    df.columns = ['List1', 'List2']
    print(df)
    df['List1'] = sorted(list(df['List1']))
    df['List2'] = sorted(list(df['List2']))

    df['diff'] = df.apply(lambda row: abs(row['List1'] - row['List2']), axis=1)
    print(df['diff'].sum())

if __name__ == '__main__':
    main()