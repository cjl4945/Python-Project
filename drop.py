"""factors.py
author: Chase Lewis
created: November 2017
CSCI-141"""


from utils import *
import math
Range = struct_type("range", (str, "country"), (int, "year1"), (int, "year2"), (float, "value1"), (float, "value2"))

# def sorted_drop_data(data):
#     everything = (read_data("data/worldbank_life_expectancy_metadata.txt"))
#     for country in data:
#         lifeExpect = everything.life[country]
#         struct = Range(country,)

def sorted_drop_data(data):
    everything = read_data("worldbank_life_expectancy")
    """

    :param data: list of data
    :return:
    des: sorts the  countries by absolute growth in life expectancy over a specified range of years.
    """

    tlist = []
    tdic = {}
    for i in data:
        x = math.inf
        highest = -x
        temp = []
        for i in range(len(data[i])-2):
            for j in range(len(data[1][i])-3-i):
                if data[i][i+2] == "" or data[i][j+3+i] == "":
                    pass
                elif float(data[i][i+2]) - float(data[i][j+3+i]) > highest:
                    highest = float(data[i][i+2]) - float(data[i][j+3+i])
                    temp = [i,int(1961+i),int(1962+i+j),float(data[i][j+3+i]),float(data[i][i+2])]
        if highest != -x:
            tdic[highest] = temp
            tlist += [highest]
    tlist.sort(reverse=True)
    temp1 = []
    for i in range(len(tlist)):
        temp1 += [Range(tdic[tlist[i]][0],tdic[tlist[i]][1],tdic[tlist[i]][2],tdic[tlist[i]][4],tdic[tlist[i]][3])]
    return temp1

def main():
    data = read_data("worldbank_life_expectancy")
    dropdata = sorted_drop_data(filter_region(data, "all"))
    print("Worst life expectancy drops: 1960 to 2015")
    for x in range(10):
        print(x+1, dropdata[x].country,"from",dropdata[x].year1,"("+str(dropdata[x].value1)+")","to",dropdata[x].year2,"("+str(dropdata[x].value2)+"):",dropdata[x].value2-dropdata[x].value1)


if __name__ == "__main__":
    main()