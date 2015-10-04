inputstr = raw_input("print input here: ")
K = int(raw_input("print the number for the letters to be shifted here: "))
outputstr = ""
K %= 26
for i in inputstr:
    if i.isupper():
        outputstr += chr(((ord(i) - 64) + K) % 26 + 64)
    elif i.islower():
        outputstr += chr(((ord(i) - 96) + K) % 26 + 96)
    else:
        outputstr += i
print outputstr