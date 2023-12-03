import pandas as pd
import re

def read_file():
    df = pd.read_csv(filepath_or_buffer='day2_indata.txt',header=None,delimiter=':')
    return df

maxDictionary = {'red':12,'green':13,'blue':14}

def anyAboveMax(red, green, blue):
    return (
            (red > maxDictionary['red']) or 
            (green > maxDictionary['green']) or 
            (blue > maxDictionary['blue'])
            )

def powerOfMinimumAmount(red, green,blue):
    return red*green*blue

def main():
    df = read_file()
    df.columns = ['ID','data']
    df['ID'] = df['ID'].map(lambda x: x[5:])
    df['maxRed'] = df['data'].map(lambda s: max(map(int, re.findall(r'(\d+) red', s))))
    df['maxGreen'] = df['data'].map(lambda s: max(map(int, re.findall(r'(\d+) green', s))))
    df['maxBlue'] = df['data'].map(lambda s: max(map(int, re.findall(r'(\d+) blue', s))))
    df['exceedsMax'] = df.apply(lambda row: anyAboveMax(row['maxRed'],row['maxGreen'],row['maxBlue']), axis=1)
    df['powerOfMinimumAmount'] = df.apply(lambda row: powerOfMinimumAmount(row['maxRed'],row['maxGreen'],row['maxBlue']), axis=1)

    print(df)
    print(df[df['exceedsMax'] == False]['ID'].map(int).sum())
    print(df['powerOfMinimumAmount'].sum())

if __name__ == '__main__':
    main()