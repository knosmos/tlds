'''
numbers = {
    "0":[(0,0), (1,0), (1,-2), (0,-2), (0,0)],
    "1":[(1,0), (1,-2)],
    "2":[(0,0), (1,0), (1,-1), (0,-1), (0,-2), (1,-2)],
    "3":[(0,0), (1,0), (1,-1), (0,-1), (1,-1), (1,-2), (0,-2)]
}
'''

import os
from shutil import copyfile

def loadChar(char):
    with open(f"digits/{i}.txt","r") as f:
        return list(map(lambda i:list(map(float,i.split())),f.read().split("\n")))

numbers = {}
for i in [0,1,2,3,4,5,6,7,8,9,"+","-","="]:
    numbers[str(i)] = loadChar(i)

charWidth = 10
letterSpacing = 0.5

def convGcode(items):
    pass

def writeChar(path, x, y):
    res = []

    # move to first point
    res.append(f"G0 X{path[0][0]*charWidth+x} Y{path[0][1]*-1*charWidth+y}")

    # move z-axis downward
    res.append("G0 Z0")

    # draw path
    for point in path:
        res.append(f"G1 X{point[0]*charWidth+x} Y{point[1]*-1*charWidth+y}")
    
    # move z-axis upward
    res.append("G0 Z15")

    # return final
    return "\n".join(res)

def writeChars(s, x, y):
    res = ""
    
    # absolute positioning
    # res += "G90\n"

    # write each character
    for i, char in enumerate(s):
        res += writeChar(numbers[char], x+i*(charWidth+letterSpacing), y) + "\n"
    return res

def main(chars):
    open("res.gcode","w").write(writeChars(chars, 0, 0))
    os.system(".\\gpx.exe -m r2x res.gcode")

    # Write to SD
    copyfile("res.x3g", "D:\\res.x3g")