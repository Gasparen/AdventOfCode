class letterPos:
    def __init__(self, string_pos_in_list, pos_in_string):
        self.string_index = string_pos_in_list
        self.pos_in_string = pos_in_string

    def __str__(self):
        return f"string_index: {self.string_index}, pos: {self.pos_in_string}"

class xmasWord:
    def __init__(self, x_pos: letterPos, direction=None):
        if direction is not None:
            self.positions = [x_pos, None, None, None]

            self.x_pos = 0
            self.m_pos = 1
            self.a_pos = 2
            self.s_pos = 3

            (self.index_direction, self.pos_direction) = direction
        else:
            self.positions = [x_pos, None, None, None, None]
            self.a_pos = 0
            self.quartet1_pos = 1
            self.quartet2_pos = 2
            self.quartet3_pos = 3
            self.quartet4_pos = 4

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
    
    def getLetter(self, listOfStrings, index, pos):
        if self.checkIndexInRange(listOfStrings, index):
            s = listOfStrings[index]
            if self.checkPosInString(s, pos):
                return s[pos]
        return None

    def findLetter(self, listOfStrings, letter, pos_to_start_from, pos_to_update):
        nextIndex = self.positions[pos_to_start_from].string_index+self.index_direction
        nextPos = self.positions[pos_to_start_from].pos_in_string+self.pos_direction
        
        if (self.checkForLetter(listOfStrings, letter, nextIndex, nextPos)):
            self.positions[pos_to_update] = letterPos(nextIndex, nextPos)
            return True

        return False

    def findM(self, listOfStrings):
        return self.findLetter(listOfStrings, 'M', self.x_pos, self.m_pos)
    
    def findA(self, listOfStrings):
        return self.findLetter(listOfStrings, 'A', self.m_pos, self.a_pos)

    def findS(self, listOfStrings):
        return self.findLetter(listOfStrings, 'S', self.a_pos, self.s_pos)
    
    def findX_MAS(self, listOfStrings):
        #   Q2[1,-1] | Q1[1, 1]
        #  ---------------------
        #  Q3[-1,-1] | Q4[-1,1]
        #
        letter_a = self.positions[self.a_pos]
        index_base = letter_a.string_index
        pos_base = letter_a.pos_in_string
        q1 = self.getLetter(listOfStrings, index_base+1, pos_base+1)
        q2 = self.getLetter(listOfStrings, index_base+1, pos_base-1)
        q3 = self.getLetter(listOfStrings, index_base-1, pos_base-1)
        q4 = self.getLetter(listOfStrings, index_base-1, pos_base+1)
        if q1 is None or q2 is None or q3 is None or q4 is None:
            return False
        if ((q1 == 'M' and q3 == 'S') or (q1 == 'S' and q3 == 'M')) and ((q1 == q2 and q3 == q4 and q1 != q3) or (q1 == q4 and q2 == q3 and q1 != q3)):
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
    listOfAs = []
    for string_index, s in enumerate(listOfStrings):
        for i, c in enumerate(s):
            if c == 'X':
                for y_direction in range(-1,2,1):
                    for x_direction in range(-1,2,1):
                        if x_direction == 0 and y_direction == 0:
                            continue
                        listOfXs.append(xmasWord(letterPos(string_pos_in_list=string_index, pos_in_string=i), (x_direction,y_direction)))
            if c == 'A':
                listOfAs.append(xmasWord(letterPos(string_pos_in_list=string_index, pos_in_string=i)))
    
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

#    for xmas in listOfXMASs:
#        print(xmas)

    listOfX_MASs = []
    for a in listOfAs:
        if a.findX_MAS(listOfStrings):
            listOfX_MASs.append(a)
    
    print(len(listOfXMASs))
    #print(listOfAs)
    print(len(listOfX_MASs))

if __name__ == '__main__':
    main()