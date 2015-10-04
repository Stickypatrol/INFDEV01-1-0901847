inputnum = int(raw_input("input the size of the triangle you wish to be drawn: "))
outputstr = ""
for i in range(inputnum):
    for p in range(i+1):
        outputstr += "*"
    outputstr += "\n"
print outputstr