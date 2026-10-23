living = ["kekkonen", "hitler", "idk man"]
deceased = ["kukkakauppias", "himler", "butler"]

invited = living + deceased

def inviteToDinner(invitedArr):
    for invited in invitedArr:
        print(invited+" has been invited to dinner")


inviteToDinner(invited)

cantMakeIt = invited[1::2]
canMakeIt = [inv for inv in invited if inv not in cantMakeIt]

for cant in cantMakeIt:
    print(cant +" cant make it")

    
for can in canMakeIt:
    print(can +" can join the dinner")