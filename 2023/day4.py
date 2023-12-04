import pandas as pd
import re

def read_file():
    df = pd.read_csv(filepath_or_buffer='day4_indata.txt',header=None, delimiter=':')
    return df

def main():
    df = read_file()
    df.columns = ['cardId', 'data']
    df[['winningNumbers','numbers']] = df['data'].str.split('|', expand=True)
    df['numbers'] = df['numbers'].map(lambda s: re.findall(r'\d+', s))
    df['winningNumbers'] = df['winningNumbers'].map(lambda s: re.findall(r'\d+', s))
    df['commonElements'] = df.apply(lambda row: set(row['numbers']).intersection(row['winningNumbers']), axis=1)
    df['points'] = df['commonElements'].map(lambda s: 0 if len(s)==0 else pow(2, len(s)-1))

    print(df)
    print(df['points'].sum())


if __name__ == '__main__':
    main()