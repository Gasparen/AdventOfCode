import pandas as pd

def read_file():
    df = pd.read_csv(filepath_or_buffer='inputs/day9_indata.txt',header=None)
    return df

def is_all_equal(l):
    return len(set(l)) == 1

def diff_reduce(l):
    if is_all_equal(l):
        return l[0]
    newList = []
    for index, value in enumerate(l[:-1]):
        newList.append(l[index+1]-value)

    return diff_reduce(newList) + l[len(l)-1]

def diff_reduce_prev(l):
    if is_all_equal(l):
        return l[0]
    newList = []
    for index, value in enumerate(l[:-1]):
        newList.append(l[index+1]-value)

    return l[0] - diff_reduce_prev(newList)


def main():
    df = read_file()
    df.columns = ['data']
    df['numberList'] = df['data'].map(lambda x: x.split(' '))
    df['numberList'] = df['numberList'].map(lambda l: list(map(int, l)))
    df['nextValue'] = df['numberList'].map(diff_reduce)
    df['previousValue'] = df['numberList'].map(diff_reduce_prev)

    print(df)
    print(df['nextValue'].sum())
    print(df['previousValue'].sum())

if __name__ == '__main__':
    main()