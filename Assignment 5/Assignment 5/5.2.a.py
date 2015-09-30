import string

inputstring = raw_input("input here")
lowerabc = False
upperabc = False
number = False
special = False
length = len(inputstring)
for i in inputstring:
    if i.isdigit():
        number = True
    elif i.isalpha():
        if i.isupper():
            upperabc = True
        else:
            lowerabc = True
    else:
        special = True

range = 0
if lowerabc:
    range+=26
if upperabc:
    range+=26
if number:
    range+=10
if special:
    range+=191

difficulty = pow(range, length)

print "The total difficulty is: {0} this is the total amount of possibilities therefore the number of 'tries' required to break the password brute-force style".format(difficulty)
print "a number comprised of 16 digits is generally considered to be of mediumlevel difficulty to break"