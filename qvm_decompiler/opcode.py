from enum import IntEnum

class Opcode(IntEnum):
    UNDEF = 0
    IGNORE = 1
    BREAK = 2
    ENTER = 3
    LEAVE = 4
    CALL = 5
    PUSH = 6
    POP = 7
    CONST = 8
    LOCAL = 9
    JUMP = 10
    EQ = 11
    NE = 12
    LTI = 13
    LEI = 14
    GTI = 15
    GEI = 16
    LTU = 17
    LEU = 18
    GTU = 19
    GEU = 20
    EQF = 21
    NEF = 22
    LTF = 23
    LEF = 24
    GTF = 25
    GEF = 26
    LOAD1 = 27
    LOAD2 = 28
    LOAD4 = 29
    STORE1 = 30
    STORE2 = 31
    STORE4 = 32
    ARG = 33
    BLOCK_COPY = 34
    SEX8 = 35
    SEX16 = 36
    NEGI = 37
    ADD = 38
    SUB = 39
    DIVI = 40
    DIVU = 41
    MODI = 42
    MODU = 43
    MULI = 44
    MULU = 45
    BAND = 46
    BOR = 47
    BXOR = 48
    BCOM = 49
    LSH = 50
    RSHI = 51
    RSHU = 52
    NEGF = 53
    ADDF = 54
    SUBF = 55
    DIVF = 56
    MULF = 57
    CVIF = 58
    CVFI = 59