inputstr = raw_input("input 2 ints seperated by whitespace here(height and width respectively): ").split()
inputnums = [int(inputstr[0]), int(inputstr[1])]
outputstr = ""
for i in range(inputnums[0]):
    for p in range(inputnums[1]):
        outputstr += "*"
    outputstr += "\n"
print outputstr