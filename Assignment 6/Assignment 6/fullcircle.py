import math

inputnum = int(raw_input("input the size of the circleyou wish to be drawn: "))
outputstr = ""
radius = inputnum/2
for y in range(inputnum+2):
    for x in range(inputnum):
        ydist = abs (y - int(radius))
        xdist = abs (x - int(radius))
        if int(math.sqrt(ydist**2 + xdist**2)) < radius:
            outputstr += "*"
        else:
            outputstr += " "
    outputstr+="\n"
print outputstr