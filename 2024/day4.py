class letterPos:
    def __init__(self, string_pos_in_list, pos_in_string):
        self.string_index = string_pos_in_list
        self.pos_in_string = pos_in_string

    def __str__(self):
        return f"string_index: {self.string_index}, pos: {self.pos_in_string}"

class xmasWord:
    def __init__(self, x_pos: letterPos, direction):
        self.x_pos = x_pos
        self.m_pos = None
        self.a_pos = None
        self.s_pos = None
        (self.index_direction, self.pos_direction) = direction

    def checkIndexInRange(self, listOfStrings, index):
        return index in range(0,len(listOfStrings))

    def checkPosInString(self, s, pos):
        return pos in range(0, len(s))

    def checkForLetter(self, listOfStrings, letter, index, pos):
        if self.checkIndexInRange(listOfStrings, index):
            s = listOfStrings[index]
            if self.checkPosInString(s, pos):
                if (s[pos] == letter):
                    return True
        return False

    def findM(self, listOfStrings):
        nextIndex = self.x_pos.string_index+self.index_direction
        nextPos = self.x_pos.pos_in_string+self.pos_direction
        
        if (self.checkForLetter(listOfStrings, 'M', nextIndex, nextPos)):
            self.m_pos = letterPos(nextIndex, nextPos)
            return True

        return False
    
    def findA(self, listOfStrings):
        nextIndex = self.m_pos.string_index+self.index_direction
        nextPos = self.m_pos.pos_in_string+self.pos_direction
        
        if (self.checkForLetter(listOfStrings, 'A', nextIndex, nextPos)):
            self.a_pos = letterPos(nextIndex, nextPos)
            return True

        return False

    def findS(self, listOfStrings):
        nextIndex = self.a_pos.string_index+self.index_direction
        nextPos = self.a_pos.pos_in_string+self.pos_direction
        
        if (self.checkForLetter(listOfStrings, 'S', nextIndex, nextPos)):
            self.s_pos = letterPos(nextIndex, nextPos)
            return True

        return False

    def __str__(self):
        outputString = f"x_pos: {self.x_pos}  going in direction [{self.index_direction}, {self.pos_direction}]"
        if self.m_pos is not None:
            outputString += f"\nm_pos: {self.m_pos}"
        if self.a_pos is not None:
            outputString += f"\na_pos: {self.a_pos}"
        if self.s_pos is not None:
            outputString += f"\ns_pos: {self.s_pos}"
        return outputString

def read_file():
    f = open('inputs/day4_indata.txt', 'r')
    #f = open('day4_testdata.txt', 'r')
    ll = []
    
    while True:
        l = f.readline()
        if l is None or l == '':
            return ll
        ll.append(l)

def main():
    listOfStrings = read_file()

    listOfXs = []
    for string_index, s in enumerate(listOfStrings):
        for i, c in enumerate(s):
            if c == 'X':
                for y_direction in range(-1,2,1):
                    for x_direction in range(-1,2,1):
                        if x_direction == 0 and y_direction == 0:
                            continue
                        listOfXs.append(xmasWord(letterPos(string_pos_in_list=string_index, pos_in_string=i), (x_direction,y_direction)))
    
    listOfXMs = []
    for x in listOfXs:
        if x.findM(listOfStrings):
            listOfXMs.append(x)

    listOfXMAs = []
    for xm in listOfXMs:
        if xm.findA(listOfStrings):
            listOfXMAs.append(xm)

    listOfXMASs = []
    for xma in listOfXMAs:
        if xma.findS(listOfStrings):
            listOfXMASs.append(xma)

    #for xmas in listOfXMASs:
    #    print(xmas)
    
    print(len(listOfXMASs))

if __name__ == '__main__':
    main()