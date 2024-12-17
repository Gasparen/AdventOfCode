import re


def read_file():
    f = open('inputs/day17_indata.txt', 'r')
    #f = open('day17_testdata.txt', 'r')

    s = f.readline()
    regA = s.split(':')[1].strip()
    s = f.readline()
    regB = s.split(':')[1].strip()
    s = f.readline()
    regC = s.split(':')[1].strip()

    s = f.readline() # Ignore empty line
    s = f.readline()
    program = s.split(':')[1].strip()

    return regA, regB, regC, program

class Computer:
    def __init__(self, regA, regB, regC, program):
        self.regA = int(regA)
        self.regB = int(regB)
        self.regC = int(regC)
        self.createInstructions()
        self.encodedInstructions = {}
        self.encodeProgram(program)
        self.instructionPointer = 0
        self.output = []

    def createInstructions(self):
        self.instructionDictionary = {'0': self.adv,
                                      '1': self.bxl,
                                      '2': self.bst,
                                      '3': self.jnz,
                                      '4': self.bxc,
                                      '5': self.out,
                                      '6': self.bdv,
                                      '7': self.cdv}
        
    def encodeProgram(self, program):
        pairs = re.findall(r'\d,\d', program)
        i = 0
        for s in pairs:
            operatorCode, operand = s.split(',')
            operator = self.instructionDictionary[operatorCode]
            self.encodedInstructions[str(i)] = (operator, operand)
            i += 2

    # Combo operand
    # 0-3   => 0-3
    # 4     => regA
    # 5     => regB
    # 6     => regC
    # 7     => N/A
    def comboOperand(self, operand) -> int:
        if operand in ['0','1','2','3']:
            return int(operand)
        elif operand == '4':
            return int(self.regA)
        elif operand == '5':
            return int(self.regB)
        elif operand == '6':
            return int(self.regC)
        else:
            return NotImplementedError(f'{operand} not valid as a combo operand')

    def runProgram(self):
        print('---- Instructions -----')
        for inst, (operation, operand) in self.encodedInstructions.items():
            print(f'index: {inst}, operation: {operation}, operand: {operand}')
        print('-----------------------')
        while str(self.instructionPointer) in self.encodedInstructions:
            #print(self)
            #print(f'pointer: {self.instructionPointer}')
            instruction, operand = self.encodedInstructions[str(self.instructionPointer)]
            incrementPointer = instruction(operand)
            self.instructionPointer += 2 if incrementPointer else 0

    def __str__(self):
        return f'regA: {self.regA}, regB: {self.regB}, regC: {self.regC}'


    # Reg A divide with combo operand -> store in regA
    def adv(self, operand):
        self.regA = self.regA//(2**self.comboOperand(operand))
        return True

    # Reg B XOR with literal orderand -> store in regB
    def bxl(self, operand):
        self.regB = self.regB ^ int(operand) # bitwise XOR operand
        return True

    # Combo operand mod 8 -> store in regB
    def bst(self, operand):
        self.regB = self.comboOperand(operand) % 8
        return True

    # if regA != 0 -> instructionPointer := regA
    def jnz(self, operand):
        if self.regA != 0:
            self.instructionPointer = int(operand)
            return False
        return True

    # Reg B XOR Reg C -> store in regB (read but ignore operand)
    def bxc(self, operand):
        self.regB = self.regB ^ self.regC
        return True

    # Combo operand mod 8 -> output (comma separated)
    def out(self, operand):
        self.output.append(self.comboOperand(operand)%8)
        return True
    
    # Reg A divide with combo operand -> store in regB
    def bdv(self, operand):
        self.regB = self.regA//(2**self.comboOperand(operand))
        return True
    
    # Reg A divide with combo operand -> store in regC
    def cdv(self, operand):
        self.regC = self.regA//(2**self.comboOperand(operand))
        return True

def main():
    regA, regB, regC, program = read_file()

    print('file input')
    print(regA)
    print(regB)
    print(regC)
    print(program)

    computer = Computer(regA, regB, regC, program)

    #print(computer.pairs)
    print(computer.output)

    computer.runProgram()

    print(computer.output)
    print(",".join(map(str, computer.output)))
    
if __name__ == '__main__':
    main()