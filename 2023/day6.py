import re
import math
from functools import reduce

def read_file():
    f = open('inputs/day6_indata_2.txt', 'r')
    timeString = f.readline()
    distanceString = f.readline()
    return timeString, distanceString

def is_above(t,x,d):
    return (t-x)*x > d

def main():
    timeString, distanceString = read_file()
    times = re.findall(r'(\d+)', timeString)
    distances = re.findall(r'(\d+)', distanceString)

    solutions = []

    # (t-x)x > d
    # x^2-tx+d=0
    for i in range(0,len(times)):
        t = int(times[i])
        d = int(distances[i])
        disk = math.sqrt(pow((-t/2),2)-d)
        high = math.floor((t/2)+disk)
        low =  math.floor((t/2)-disk)
        highs = [high-1, high, high+1]
        lows = [low-1, low, low+1]
        highs = reduce(lambda x,y: x+[y] if is_above(t,y,d) else x, highs, [])
        lows  = reduce(lambda x,y: x+[y] if is_above(t,y,d) else x, lows, [])
        solutions.append(max(highs) - min(lows) + 1)
        

    print(times, distances)
    print(solutions)
    print(reduce(lambda x,y: x*y, solutions))

if __name__ == '__main__':
    main()