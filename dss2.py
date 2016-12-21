def dss(dice):
    currList = [0]*(sum(dice) + 1)
    first = True
    for die in dice:
        if first:
            first = False
            for d in range(1, die + 1):
                currList[d] += 1
            continue
        nextList = [0]*(sum(dice) + 1)
        for i, s in enumerate(currList):
            if s == 0:
                continue
            for dieFace in range(1, die+ 1):
                nextList[dieFace + i] += s
        currList = nextList
    return currList
