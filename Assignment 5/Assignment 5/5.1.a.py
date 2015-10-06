inputstr = raw_input("input shit here")
accumulator = ""
for i in range(len(inputstr)):
    accumulator += inputstr[len(inputstr)-1-i]
print accumulator   