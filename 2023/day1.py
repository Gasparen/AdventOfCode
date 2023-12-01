import pandas as pd

def read_file():
    df = pd.read_csv(filepath_or_buffer='day1_indata.csv',header=None)
    return df

def filter_numbers(s: str):
    temp = []
    for c in s:
        if c.isnumeric():
            temp.append(c)

    return temp

def concat_first_last(numbers):
    return int("" + numbers[0] + numbers[len(numbers)-1])

def main():
    df = read_file()
    df.columns=['data']
    df['onlyNumbers'] = df.apply(lambda row: filter_numbers(row['data']), axis=1)
    df['calibrationValue'] = df['onlyNumbers'].map(concat_first_last)

    print(df)
    print(df['calibrationValue'].sum())

if __name__ == '__main__':
    main()