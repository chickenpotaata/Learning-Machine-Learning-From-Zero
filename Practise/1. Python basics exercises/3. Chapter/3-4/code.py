living = ["kekkonen", "hitler", "idk man"]
deceased = ["kukkakauppias", "himler", "butler"]

invited = living + deceased

def inviteToDinner(invitedArr):
    for invited in invitedArr:
        print(invited+" has been invited to dinner")


inviteToDinner(invited)