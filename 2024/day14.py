import pandas as pd
import re

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day14_testdata.txt',header=None,delimiter=':')
    df = pd.read_csv(filepath_or_buffer='inputs/day14_indata.txt',header=None,delimiter=':')
    return df

def printPicture(picture):
    for l in picture:
        print(''.join(l))

def plot(picture, x, y):
    picture[y][x] = '#'

def main():
    df = read_file()
    width = 101
    height = 103
    midX = width//2
    midY = height//2
    df.columns = ['data']
    df['xPosition'] = df['data'].map(lambda x: int(re.findall(r'p=([-]*[\d]+),', x)[0]))
    df['yPosition'] = df['data'].map(lambda x: int(re.findall(r'p=[-]*[\d]+,([-]*[\d]+)', x)[0]))
    df['xVelocity'] = df['data'].map(lambda x: int(re.findall(r'v=([-]*[\d]+),', x)[0]))
    df['yVelocity'] = df['data'].map(lambda x: int(re.findall(r'v=[-]*[\d]+,([-]*[\d]+)', x)[0]))
    df['xPos100'] = (df.xPosition + (df.xVelocity*100))%width
    df['yPos100'] = (df.yPosition + (df.yVelocity*100))%height
    df['inQ1'] = df.apply(lambda row: row.xPos100 > midX and row.yPos100 < midY,axis=1)
    df['inQ2'] = df.apply(lambda row: row.xPos100 < midX and row.yPos100 < midY,axis=1)
    df['inQ3'] = df.apply(lambda row: row.xPos100 < midX and row.yPos100 > midY,axis=1)
    df['inQ4'] = df.apply(lambda row: row.xPos100 > midX and row.yPos100 > midY,axis=1)
    print(df)
    print(midX)
    print(midY)

    print(f'Q1: {df['inQ1'].sum()}')
    print(f'Q2: {df['inQ2'].sum()}')
    print(f'Q3: {df['inQ3'].sum()}')
    print(f'Q4: {df['inQ4'].sum()}')
    
    safetyFactor = df['inQ1'].sum()*df['inQ2'].sum()*df['inQ3'].sum()*df['inQ4'].sum()
    print(safetyFactor)

    

 


if __name__ == '__main__':
    main()