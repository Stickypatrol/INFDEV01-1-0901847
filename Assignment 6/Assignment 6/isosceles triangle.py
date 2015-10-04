inputnum = int(raw_input("input the size of the triangle you wish to be drawn: "))
outputstr = ""
for i in range(inputnum):
    for p in range(inputnum + i):
        if p < inputnum-1-i:
            outputstr += " "
        elif p > inputnum-1:
            outputstr += "*"
        else:
            outputstr += "*"
    outputstr += "\n"
print outputstr