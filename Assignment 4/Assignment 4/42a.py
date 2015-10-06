def inputandvalidate(player):
    choice = raw_input("player {}, input rock, paper or scissors ".format(player))
    choice = choice.lower()
    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = raw_input("you didnt input a correct value silly, only chooce rock, paper or scissors ")
    return choice
def checkwhowins(a, b):
    if a == b:
        print "Draw, too bad"
    elif a == "scissors":
        if b== "paper":
            print "player B lost"
        elif b== "rock":
            print "player A lost"
    elif playerA == "rock":
        if playerB == "scissors":
            print "player B lost"
        elif playerB == "paper":
            print "player A lost"
    else:
        if playerB == "rock":
            print "player B lost"
        elif playerB == "scissors":
            print "player A lost"


playerA = inputandvalidate("A")
playerB = inputandvalidate("B")
checkwhowins(playerA, playerB)