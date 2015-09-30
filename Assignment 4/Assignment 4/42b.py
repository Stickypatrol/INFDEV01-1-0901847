def inputandvalidate(player):
    choice = raw_input("player {}, input rock, paper, scissors, lizard or spock here : ".format(player))
    choice = choice.lower()
    while choice != "rock" and choice != "paper" and choice != "scissors" and choice != "spock" and choice != "lizard":
        choice = raw_input("you didnt input a correct value silly, only chooce rock, paper or scissors  here: ")
    return choice

def checkwhowins(a, b):
    winlist = ["rock", "lizard", "spock", "scissors", "paper"]
    if a != b:
        aIndex = winlist.index(a)
        bIndex = winlist.index(b)
        if (aIndex - bIndex)% 2 == 0:
            if aIndex > bIndex:
                print "player A wins!!"
            else:
                print "player B wins!!"
        else:
            if aIndex > bIndex:
                print "player B wins!"
            else:
                print "player A wins!"

            
    else:
        print "Draw, too bad" 
#I use the fact that the options have a numerical relationship. if A == 0(zeroeth index of the list) then every other number, starting from 1, loses.
#I use modulus because the exact number does not matter, the only thing that matters if is it's an even number and the relationship with the other.
#the items are in a specific order but which item you start with is arbitrary because the relationship is circular.
while 1==1:
    print "Let's play a game!"
    playerA = inputandvalidate("A")
    playerB = inputandvalidate("B")
    checkwhowins(playerA, playerB)