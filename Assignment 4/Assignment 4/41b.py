celsius = float(raw_input("input celsius here NOW: "))
while celsius < 0:
    print "temperature is impossibly low, like literally. input a VALID value."
    celsius = float(raw_input())
print "Temp = {} Kelvin".format(celsius - 273.15)