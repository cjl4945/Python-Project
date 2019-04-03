"""growth.py
author: Chase Lewis
created: November 2017
CSCI-141"""


from utils import *
from operator import *
CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))


def sorted_growth_data(data, year1, year2):
    """sorted_growth_data will go through data and return the growth between two years
    param data: a data structure
    param year1: user inputted starting year
    param year2: user inputted ending year
    returns: a list of structure types"""
    everything = (read_data("worldbank_life_expectancy"))
    s = []
    for value in data:
        idxstart = int(year1) - 1960
        idxend = int(year2) - 1960
        hey = (everything.life[value])

        try:
            struct = CountryValue(value, float(hey[idxend]) - float(hey[idxstart]))
            s.append(struct)
        except:
            pass
    s = sorted(s, key=attrgetter('value'), reverse=True)

    return s


def main():
    everything = (read_data("worldbank_life_expectancy"))
    while everything != None:
        year1 = int(input("Enter starting year of interest(Enter -1 to quit): "))
        if year1 == -1:
            break
        year2 = int(input("Enter ending year of interest(Enter -1 to quit): "))
        if year2 == -1:
            break
        elif year1 > 2015 or year1 < 1960 or year2 > 2015 or year2 < 1960:
            print("Valid years are 1960-2015")
            continue
        while year1 <= 2015 or year1 >= 1960 or year2 >= 1960 or year2 <= 2015:
            region = input("Enter region (type ’all’ to consider all): ")
            if region == "all":
                pass
            elif region not in everything.regions.keys():
                print("'" + region + "'" + "not a valid region")
                continue
            lst1 = filter_region(everything, region)
            data = lst1
            sorts1 = sorted_growth_data(data,year1,year2)
            category = input("Enter income category (type ’all’ to consider all): ")
            if category == "all":
                pass
            elif category not in everything.income.keys():
                print("'" + category + "'" + "not a valid region")
                continue
            lst2 = filter_income(everything, category)
            data2 = lst2
            sorts2 = sorted_growth_data(data2,year1,year2)
            together = []
            for value in sorts1:
                if value in sorts2:
                    together.append(value)
            print("Top 10 Life expectancy growth:", year1,"to",year2)
            num = 1
            for i in range(0, 10):
                if i > (len(together) - 1):
                    break
                else:
                    print(str(num) + ":" + " " + together[i].country + " " + str(together[i].value))
                    num += 1
            print("Bottom 10 Life Expectancy growth:",year1,"to",year2)
            together.reverse()
            num = len(together)
            for i in range(0, 10):
                if i > (len(together) - 1):
                    break
                else:
                    print(str(num) + ":" + " " + together[i].country + " " + str(together[i].value))
                    num -= 1
            break






if __name__ == "__main__":
        main()
