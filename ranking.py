"""ranking.py
author: Chase Lewis
created: November 2017
CSCI-141"""


from utils import *

from rit_lib import *
from operator import *

CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))



def sorted_ranking_data(data, year):
    """sorted_ranking_data will go through a data of a filtered region or filtered income and based on the year, will return
     a list of struct type in order from greatest life expectancy to least
     param data: data structure
     param year: user inputted desired year
     return: a list of structure types"""
    s = []
    everything = (read_data("worldbank_life_expectancy"))
    for value in data:
        idx = int(year) - 1960
        hey = (everything.life[value])
        try:
            struct = CountryValue(value, float(hey[idx]))
            s.append(struct)
        except:
            pass
    s = sorted(s, key=attrgetter('value'), reverse=True)

    return s




def main():
    everything = (read_data("worldbank_life_expectancy"))
    while everything != None:
        year = int(input("Enter year of interest(-1 to quit): "))
        if year == -1:
            break
        if year > 2015 or year < 1960:
            print("Valid years are 1960-2015")
            continue
        while year >= 1960 or year <= 2015:
            region = input("Enter region (type ’all’ to consider all): ")
            if region == "all":
                pass
            elif region not in everything.regions.keys():
                print("'" + region + "'" + "not a valid region")
                continue
            lst1 = filter_region(everything, region)
            data = lst1
            sorts1 = sorted_ranking_data(data, year)
            category = input("Enter income category (type ’all’ to consider all): ")
            if category == "all":
                pass
            elif category not in everything.income.keys():
                print("'" + category + "'" + "not a valid region")
                continue
            lst2 = filter_income(everything, category)
            data2 = lst2
            sorts2 = sorted_ranking_data(data2, year)
            together = []
            for value in sorts1:
                if value in sorts2:
                    together.append(value)
            print("Top 10 Life expectancy for", year)
            num = 1
            for i in range(0,10):
                if i > (len(together) - 1):
                    break
                else:
                    print(str(num) + ":" + " " + together[i].country + " " + str(together[i].value))
                    num += 1
            print("Bottom 10 Life Expectancy for", year)
            together.reverse()
            num = len(together)
            for i in range(0,10):
                if i > (len(together) - 1):
                    break
                else:
                    print(str(num) + ":" + " " + together[i].country + " " + str(together[i].value))
                    num -= 1
            break


if __name__ == "__main__":
    main()

