
def read_file():
    f = open('inputs/day9_indata.txt', 'r')
    #f = open('day9_testdata.txt', 'r')

    return f.readline().strip()

def explode(s):
    fileID = 0
    files = []
    freeSpace = []
    index = 0
    for i,c in enumerate(s):
        amount = int(c)
        if i%2==0:
            files.append([index, fileID, amount])
            fileID += 1
        else:
            freeSpace.append([index, amount])
        index += amount
    return files, freeSpace

def defragment(files, freeSpace):
    movedFiles = []
    #print(files, freeSpace)
    for space in freeSpace:
        [freeIndex, freeAmount] = space
        #print(f'At index {freeIndex} we have {freeAmount} spaces free')
        while True:
            [index, fileID, amount] = files.pop()
            #print(f'This file should wholly/partially fit [{index}, {fileID}, {amount}]')
            #print(f'Files contains {files}')
            if index <= freeIndex:
                #print('No more files to move')
                files.append([index, fileID, amount])
                files.extend(movedFiles)
                return files
            if freeAmount < amount:
                movedFiles.append([freeIndex, fileID, freeAmount])
                files.append([index, fileID, amount-freeAmount])
                break
            elif freeAmount == amount:
                movedFiles.append([freeIndex, fileID, freeAmount])
                break
            else:
                movedFiles.append([freeIndex, fileID, amount])
                freeAmount = freeAmount - amount
                freeIndex = freeIndex + amount
            
    files.extend(movedFiles)
    return files

def main():
    diskString = read_file()

    #print(diskString)

    files, freeSpace = explode(diskString)
    #print(files)
    #print(freeSpace)

    newFiles = defragment(files, freeSpace)
    #print(newFiles)
    newFiles.sort(key=lambda x: x[0])
    #print(newFiles)

    checksum = 0
    for [index, fileID, amount] in newFiles:        
        tempSum = sum([index+i for i in range(amount)]) * fileID
        checksum += tempSum
        #print(f'temp:{tempSum} New checksum:{checksum}')
    print(checksum)

if __name__ == '__main__':
    main()