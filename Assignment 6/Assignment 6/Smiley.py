import math

inputnum = int(raw_input("input the size of the smiley you wish to draw, at smaller sizes it may be very ugly: "))+1
outputstr = ""
radius = inputnum/2
for y in range(inputnum):
    for x in range(inputnum):
        ydist = abs (y - int(radius))
        xdist = abs (x - int(radius))
        if int(math.ceil(math.sqrt(ydist**2 + xdist**2))) == radius:
            outputstr += "*"
        elif y == int(inputnum/3) and (x == int(inputnum/3) or x == int(inputnum/3 *2)):
            outputstr += "*"
        elif y > int(inputnum / 3 * 2)and int(math.floor(math.sqrt(ydist**2 + xdist**2))) == int(radius/2):
            outputstr += "*"
        elif y > int(inputnum / 4 * 1.75) and y < int(inputnum / 4 * 2.25) and x == int(inputnum/2):
            outputstr += "*"
        else:
            outputstr += " "
    outputstr+="\n"
print outputstr