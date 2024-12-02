import pandas as pd

def read_file():
    #df = pd.read_csv(filepath_or_buffer='day2_testdata.csv',header=None)
    df = pd.read_csv(filepath_or_buffer='inputs/day2_indata.csv',header=None)
    return df

def check_list(s):
    l = s.split(' ')
    is_increasing = None
    for i in range(0, len(l)-1):
        [x,y] = l[i:i+2]
        diff = int(y)-int(x)
        abs_diff = abs(diff)
        if abs_diff > 3 or abs_diff < 1:
            return False
        if is_increasing is None:
            is_increasing = True if diff > 0 else False
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return False
    return True

def main():
    df = read_file()
    df.columns = ['data']
    df['safeReport'] = df['data'].map(lambda x: check_list(x))
    print(df['safeReport'].value_counts())
    
if __name__ == '__main__':
    main()