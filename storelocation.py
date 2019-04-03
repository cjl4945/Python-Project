"""storeLocation.py
author: Chase Lewis
created: October 2017
CSCI-141"""


import math

import time




def quickSort (L):
    if L == []:
        return []
    else:
        pivot = L[0]
        (less , same , more ) = partition(pivot , L) 
        sortedLess = quickSort(less)
        sortedMore = quickSort(more)
        sortedAll =  sortedLess + same + sortedMore
        return sortedAll

def partition(pivot, L):
    (less, same, more) = ([], [], [])
    for e in L:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more)


def bestlocation(list):
    list = quickSort(list)
    isEven = 0 == len(list) % 2
    if isEven:
        return (int(list[len(list)//2]) + int(list[len(list)//2 - 1])/2)
    else:
        return int(list[len(list)//2])

def sum(list, best):
    num = 0
    for i in list:
        num += abs(int(i) - best)
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
    print ("Optimum new store location locatoin: " + str(bestlocation(newlist)))
    end = time.clock()
    print ("sum of distances to new store: " + str(sum(newlist, bestlocation(newlist))))
    print("elasped time: " + str(end - start))


main()
