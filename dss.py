#!/usr/bin/env python

import sys
class DiceSumStats(object):
    """
    DiceSumStats Utility.
    Returns a dieChart of all the occurences of each possible Sum using the dieChart() function.
    Usage:
    ./cool_die <die1> <die2> <die3> ... <dieN>
    """
    def __init__(self):
        self.sumList = None

    def _recurseDie(self, dieList, currSum):
        if self.sumList == None:
            raise Exception
        if len(dieList) == 0:
            self.sumList[currSum] += 1
            return
        if dieList[0] == 10:
            range(1,10)
            for i in range(0, 10):
                self._recurseDie(dieList[1:], currSum + i)
        else:
            for i in range(1, dieList[0] + 1):
                self._recurseDie(dieList[1:], currSum + i)

    def dieChart(self, dieList):
        self.sumList = [0]*(sum(dieList)+1)
        self._recurseDie(dieList, 0)
        return (self.sumList, dieList)

    def prettyPrint(self, sumDiePair):
        countUp, dieList = sumDiePair
        print dieList
        print "Sum\t#\tMean"
        s = sum(countUp)
        currEV, currCount = None, None
        for i, c in enumerate(countUp):
            if currEV == None:
                currEV, currCount = [i], c
            elif c == currCount:
                currEV.append(i)
            elif c > currCount:
                currEV, currCount = [i], c
            print "{0}\t{1}\t{2:.2f}%".format(i, c, 100.0*(float(c)/float(s)))
        print "________"
        print "Total Possible"
        print "{}".format(s)
        print "Expected Value"
        if currEV == None:
            print "None"
        else:
            print "{0:.1f}".format(float(sum(currEV))/float(len(currEV)))

def main():
    c = DiceSumStats()
    if len(sys.argv) < 2:
        print c.__doc__
        return
    dieList = map(int, sys.argv[1:])
    c.prettyPrint(c.dieChart(dieList))

if __name__ == "__main__":
    main()
