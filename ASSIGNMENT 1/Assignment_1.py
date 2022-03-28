'''
-------------------------------------
 Assignment 1 - EE2703 (Jan-May 2022)
 Done by SUHAS C EE20B132
 Created on 26/01/22
-------------------------------------
'''


from sys import argv, exit


CIRCUIT = ".circuit"
END = ".end"


def tokens(spiceLine):
    Words = spiceLine.split()

    # R, L, C, Independent Sources
    if len(Words) == 4:
        Nameofelement = Words[0]
        node1 = Words[1]
        node2 = Words[2]
        value = Words[3]
        return [Nameofelement, node1, node2, value]

    # CCxS
    elif len(Words) == 5:
        Nameofelement = Words[0]
        node1 = Words[1]
        node2 = Words[2]
        voltageSource = Words[3]
        value = Words[4]
        return [Nameofelement, node1, node2, voltageSource, value]

    # VCxS
    elif len(Words) == 6:
        Nameofelement = Words[0]
        node1 = Words[1]
        node2 = Words[2]
        voltageSourceNode1 = Words[3]
        voltageSourceNode2 = Words[4]
        value = Words[5]
        return [
            Nameofelement,
            node1,
            node2,
            voltageSourceNode1,
            voltageSourceNode2,
            value,
        ]

    else:
        return []


def getTokens(lines):
    lines_token = []
    for i in range(0, len(lines)):                         # iterating the i from 0 to len(line)
        line = (
            lines[i].split("#")[0].split()
        )                                                  # Splitting the lines and removing the comments

        lines_token.append(
            line
        )                                                  # join words after reversing and add "\n" at the end of line

    return lines_token


if len(argv) != 2:
    print("Invalid operation !")
    print(f"Usage: {argv[0]} <inputfile>'")
    exit()

try:
    with open(argv[1]) as f:
        lines = f.readlines()
        start = -1; end = -2
        for line in lines:                            
            if CIRCUIT == line[:len(CIRCUIT)]:
                start = lines.index(line)
            elif END == line[:len(END)]:
                end = lines.index(line)
                break
        if start >= end:                                # checking the validity of the circuit block
            print('Invalid circuit definition')
            exit(0)

        Lines = lines[start + 1 : end]
        LinesToken = getTokens(Lines)


        output = ""
        for i in reversed(range(start + 1, end)):       # iterate over valid range itof the circu
            line = (lines[i].split("#")[0].split())  

            line.reverse()                              # reversing the list 
            output = output + (" ".join(line) + "\n")   # adding "\n" at teh end of the line and reversening the line

        print(output)
        


except IOError:
    print("Invalid file!")
    exit()
