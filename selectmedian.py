"""selectMedian.py
author: Chase Lewis
created: October 2017
CSCI-141"""

import math
import time

def bestlocation(list):
    k = len(list) // 2
    return quickselect(list, k )

def quickselect(list, k):
    if list != []:
        pivot = list[(len(list) // 2)]
        smallerlist = []
        largerlist = []

        count= 0
        for element in list:
            if element > pivot:
                largerlist.append(element)
            if element < pivot:
                smallerlist.append(element)
            if element == pivot:
                count += 1
        m = len(smallerlist)
        if k >= m and k < m + count:
            return pivot
        if m > k:
            return quickselect( smallerlist, k)
        else:
            return quickselect(largerlist, k - m - count)

def sum(list, best):
    num = 0
    for i in list:
        num += abs(int(i) - int(best))
    return num

def main():
    filename = input("Enter Data File: ")
    fd = open(filename)
    newlist = []
    for line in fd:
        line = line.strip()
        line = line.split()
        templist = line
        newlist.append(templist[1])
    start = time.clock()
    print("Optimum new store location locatoin: " + str(bestlocation(newlist)))
    end = time.clock()
    print("sum of distances to new store: " + str(sum(newlist,bestlocation(newlist))))
    print("elasped time: " + str(end - start))

main()
                
                
    
