from enum import Enum

mnemonics = [
    "hlt",  # 0
    "add",  # 1
    "sub",  # 2
    "inc0",  # 3
    "inc1",  # 4
    "dec0",  # 5
    "dec1",  # 6
    "beep",  # 7
    "print",  # 8
    "ldr0",  # 9
    "ldr1",  # 10
    "str0",  # 11
    "str1",  # 12
    "b",  # 13
    "bz",  # 14
    "bnz",  # 15
]


def HLT():
    print("\n*** HALT ***")


def ADD(R0, R1):
    R0 += R1
    return R0, R1


def SUB(R0, R1):
    R0 -= R1
    return R0, R1


def INC0(R0, R1):
    R0 += 1
    return R0, R1


def INC1(R0, R1):
    R1 += 1
    return R0, R1


def DEC0(R0, R1):
    R0 -= 1
    return R0, R1


def DEC1(R0, R1):
    R1 -= 1
    return R0, R1


def BEEP():
    print("\n*** BEEP ***")


def PRINT(R0, R1, IP, memory):
    print("\n***", memory[memory[IP]], "***")
    return R0, R1, memory


def LDR0(R0, R1, IP, memory):
    R0 = memory[memory[IP]]
    return R0, R1, memory


def LDR1(R0, R1, IP, memory):
    R1 = memory[memory[IP]]
    return R0, R1, memory


def STR0(R0, R1, IP, memory):
    memory[memory[IP]] = R0
    return R0, R1, memory


def STR1(R0, R1, IP, memory):
    memory[memory[IP]] = R1
    return R0, R1, memory


def B(IP, R0, memory):
    IP = memory[IP]
    return IP


def BZ(IP, R0, memory):
    if R0 == 0:
        IP = memory[IP]
    else:
        IP += 1
    return IP


def BNZ(IP, R0, memory):
    if R0 != 0:
        IP = memory[IP]
    else:
        IP += 1
    return IP


class InstructionType(Enum):
    REGISTER = 1
    MEMORY = 2
    BRANCH = 3
    STATELESS = 4


instruction_set = [
    [HLT, InstructionType.STATELESS],  # 0
    [ADD, InstructionType.REGISTER],  # 1
    [SUB, InstructionType.REGISTER],  # 2
    [INC0, InstructionType.REGISTER],  # 3
    [INC1, InstructionType.REGISTER],  # 4
    [DEC0, InstructionType.REGISTER],  # 5
    [DEC1, InstructionType.REGISTER],  # 6
    [BEEP, InstructionType.STATELESS],  # 7
    [PRINT, InstructionType.MEMORY],  # 8
    [LDR0, InstructionType.MEMORY],  # 9
    [LDR1, InstructionType.MEMORY],  # 10
    [STR0, InstructionType.MEMORY],  # 11
    [STR1, InstructionType.MEMORY],  # 12
    [B, InstructionType.BRANCH],  # 13
    [BZ, InstructionType.BRANCH],  # 14
    [BNZ, InstructionType.BRANCH],  # 15
]
