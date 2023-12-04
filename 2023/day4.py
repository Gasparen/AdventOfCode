import pandas as pd
import re

def read_file():
    df = pd.read_csv(filepath_or_buffer='day4_indata.txt',header=None, delimiter=':')
    return df

def updateTickets(wins, tickets):
    for ind, value in enumerate(wins):
        for i in range(value):
            tickets[ind+i+1] += tickets[ind]

def main():
    df = read_file()
    df.columns = ['cardId', 'data']
    df[['winningNumbers','numbers']] = df['data'].str.split('|', expand=True)
    df['numbers'] = df['numbers'].map(lambda s: re.findall(r'\d+', s))
    df['winningNumbers'] = df['winningNumbers'].map(lambda s: re.findall(r'\d+', s))
    df['commonElements'] = df.apply(lambda row: set(row['numbers']).intersection(row['winningNumbers']), axis=1)
    df['points'] = df['commonElements'].map(lambda s: 0 if len(s)==0 else pow(2, len(s)-1))

    numberOfWins = df['commonElements'].map(len).to_list()
    numberOfTickets = [1 for i in range(len(numberOfWins))]
    
    print(df)
    print(df['points'].sum())
    print(numberOfWins)
    print(numberOfTickets)
    updateTickets(numberOfWins, numberOfTickets)
    print(sum(numberOfTickets))

if __name__ == '__main__':
    main()