import pandas as pd
import re

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day3_testdata.txt',header=None,delimiter='¿',engine='python')
    df = pd.read_csv(filepath_or_buffer='inputs/day3_indata.txt',header=None,delimiter='¿',engine='python')
    return df

def multiply(l):
    sum = 0
    for (x,y) in l:
        sum += int(x)*int(y)
    return sum

def multiplyTurnOnOff(l):
    sum = 0
    do = True
    for (x,y,on_off) in l:
        if do and x != '':
            sum += int(x)*int(y)
        if on_off != '':
            do = True if on_off == 'do()' else False
    return sum
        

def main():
    df = read_file()
    df.columns = ['data']
    df['muls'] = df['data'].map(lambda x: re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', x))
    df['mulsDoDont'] = df['data'].map(lambda x: re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don\'t\(\))', x))
    df['result'] = df['muls'].map(multiply)
    df['result2'] = df['mulsDoDont'].map(multiplyTurnOnOff)


    print(df['result'])
    print(df['result'].sum())
    print(df['result2'])
    print(df['result2'].sum())


    
if __name__ == '__main__':
    main()