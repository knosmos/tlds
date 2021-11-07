import convGcode, os
from shutil import copyfile

eq = "x**2"
res = "G0 Z10\n"
res += convGcode.writeChars("y=x^", 0, 0)

units = 20
unitSize = 0.1
gridSize = 60

yOffset = 30

# x-axis
xAxis = "\n".join([
    f"G0 X0 Y{-yOffset-gridSize/2}",
    "G1 Z0",
    f"G1 X{gridSize} Y{-yOffset-gridSize/2}",
    "G0 Z10"
])
res += xAxis + "\n"

# y-axis
yAxis = "\n".join([
    f"G0 X{gridSize/2} Y{-yOffset}",
    "G1 Z0",
    f"G1 X{gridSize/2} Y{-yOffset-gridSize}",
    "G0 Z10"
])
res += yAxis + "\n"

# graph
for i in range(-units//2,units//2+1):
    x = unitSize*i
    y = eval(eq)
    res += f"G1 X{x/unitSize*gridSize/units+gridSize/2} Y{y/unitSize*gridSize/units-yOffset-gridSize/2}\n"
    res += "G1 Z0\n"

res += "G0 Z10\n"
convGcode.charWidth = 5
convGcode.letterSpacing = 0.1
res += convGcode.writeChars(str(int(units*unitSize)//2),gridSize,-yOffset-gridSize/2)
res += convGcode.writeChars(str(int(-units*unitSize)//2),0,-yOffset-gridSize/2)

res += "G0 Z40\n"

with open("graph.gcode","w") as f:
    f.write(res)

os.system(".\\gpx.exe -m r2x graph.gcode")

# Write to SD
copyfile("graph.x3g", "D:\\graph.x3g")