import pandas as pd

def read_file():
    df = pd.read_csv(filepath_or_buffer='day1_indata.csv',header=None)
    return df

digitDictionary = {'one': 'o1e',
                   'two': 't2o',
                   'three': 't3e',
                   'four': '4',
                   'five': '5e',
                   'six': '6',
                   'seven': '7n',
                   'eight': 'e8t',
                   'nine': 'n9e'}

def filter_numbers(s: str):
    temp = []
    for c in s:
        if c.isnumeric():
            temp.append(c)

    return temp

def tokenize(s: str):
    returnString = s
    for key, value in digitDictionary.items():
        returnString = returnString.replace(key, value)

    return returnString

def concat_first_last(numbers):
    return int("" + numbers[0] + numbers[len(numbers)-1])

def main():
    df = read_file()
    df.columns=['data']
    df['onlyNumbers'] = df.apply(lambda row: filter_numbers(row['data']), axis=1)
    df['calibrationValue'] = df['onlyNumbers'].map(concat_first_last)

    df['numbersAndWords'] = df.apply(lambda row: filter_numbers(tokenize(row['data'])), axis=1)
    df['calibrationValueExtended'] = df['numbersAndWords'].map(concat_first_last)

    print(df)
    print(df['calibrationValue'].sum())
    print(df['calibrationValueExtended'].sum())

if __name__ == '__main__':
    main()