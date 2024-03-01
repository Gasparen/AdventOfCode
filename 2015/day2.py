import pandas as pd
from functools import reduce

def read_file():
    df = pd.read_csv(filepath_or_buffer='inputs/day2_indata.csv', delimiter='x',header= None)
    return df

def calculate_total_paper_usage(l: int, w: int, h:int) -> int:
    sides = [l*w, w*h, l*h]
    min_value = min(sides)
    sides = map(lambda x: 2*x, sides)
    sum = reduce(lambda x, y: x+y, sides)
    return sum+min_value

def calculate_total_ribbon_usage(l: int, w: int, h:int) -> int:
    sides = sorted([l, w, h])
    sum = 2*sides[0]+2*sides[1]+l*w*h
    return sum

def main():
    df = read_file()
    df.columns = ['l', 'w', 'h']
    df['sumPaper'] = df.apply(lambda row: calculate_total_paper_usage(row['l'],row['w'],row['h']), axis=1)
    df['sumRibbon'] = df.apply(lambda row: calculate_total_ribbon_usage(row['l'],row['w'],row['h']), axis=1)

    print(df['sumPaper'].sum())
    print(df['sumRibbon'].sum())

if __name__ == '__main__':
    main()