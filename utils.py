"""utils.py
author: Chase Lewis
created: November 2017
CSCI-141
"""

from rit_lib import *

#Countries = Node("Countries", "")
everything = struct_type("everything",(dict, "allCountries"), (dict, "cnty" ),(dict, "CO"), (dict, "regions"), (dict, "income"),(dict, "life"), (int, "entities"), (int, "countries") )

def read_data(filename):
    tempfile = "data/" + filename + "_metadata.txt"

    """read_data takes in a filename and parses the file. From the file, several dictionaries are created
    added into a structure. One dictionary includes the 7 regions as key and a list of countries as
    the values. Another dictionary have the income categories with the categories as keys and a list of countries
    as the values.
    param filename: name of input file
    returns: a structure of dictionaries and integers"""

    CO =  {}
    life = {}
    cnty = {}
    regions = {}
    allCountries = {}
    allCountries["all"] = []
    regions["Middle East & North Africa"] = []
    regions["Europe & Central Asia"] = []
    regions["North America"] = []
    regions["Latin America & Caribbean"] = []
    regions["South Asia"] = []
    regions["East Asia & Pacific"] = []
    regions["Sub-Saharan Africa"] = []
    income = {}
    income["High income"] = []
    income["Upper middle income"] = []
    income["Lower middle income"] = []
    income["Low income"] = []
    fd = open(tempfile)
    entities = 0
    countries = 0
    data = open("data/worldbank_life_expectancy_data.txt")
    for line in data:
        line = line.strip().split(",")
        CO[line[1]] = line[0]
        cnty[line[0]] = line[1]
        life[line[0]] = line[2:-1]
        allCountries["all"].append(line[0])
    data.close()

    for line in fd:
        line = line.strip().split(",")
        entities += 1
        if line[1] != "":
            countries +=1
            if line[1] == "Middle East & North Africa":

                regions["Middle East & North Africa"].append(CO[line[0]])
            elif line[1] == "Europe & Central Asia":

                regions["Europe & Central Asia"].append(CO[line[0]])
            elif line[1] == "North America":

                regions["North America"].append(CO[line[0]])
            elif line[1] == "Latin America & Caribbean":

                regions["Latin America & Caribbean"].append(CO[line[0]])
            elif line[1] == "South Asia":

                regions["South Asia"].append(CO[line[0]])
            elif line[1] == "East Asia & Pacific":

                regions["East Asia & Pacific"].append(CO[line[0]])
            elif line[1] == "Sub-Saharan Africa":

                regions["Sub-Saharan Africa"].append(CO[line[0]])
            if line[2] == "High income":

                income["High income"].append(CO[line[0]])
            elif line[2] == "Upper middle income":

                income["Upper middle income"].append(CO[line[0]])
            elif line[2] == "Lower middle income":

                income["Lower middle income"].append(CO[line[0]])
            elif line[2] == "Low income":

                income["Low income"].append(CO[line[0]])

    fd.close()




    return everything(allCountries, cnty, CO, regions, income, life, entities, countries)


def filter_region(everything, area):
    """ filter_region filter through a dictionary and returns a data structure on couuntries based on what the user has inputted
    as the region
    param everything: the structure that contains the dictionaries
    param area: the region that is going to be filtered
    returns: a data structure with the countries of the desired region"""

    if area == "All" or area == "all":
        empty = []
        for regions in everything.regions.values():
            for values in regions:
                empty.append(values)


        return empty

    elif area not in everything.regions.keys():
        print(area + " " + "Is not a valid region")
        pass
    else:
        returnEverythingStruct = {}

        return everything.regions[area]

def filter_income(data, income):
    """filter_income filter through a dictionary and returns a data structure on couuntries based on what the user has inputted
    as the income category
    param everything: the structure that contains the dictionaries
    param income: the income category that's is going to be filtered
    returns: a data structure with the countries of the desired region"""
    everything = (read_data("worldbank_life_expectancy"))
    if data == everything:
        if income == "All" or income == "all":
            empty = []
            for categories in everything.income.values():
                for values in categories:
                    empty.append(values)
            return empty
        elif income not in everything.income.keys():
            print(income + " " + "Is not a valid income category")
            pass
        else:
            return everything.income[income]
    else:
        empty = []
        for values in data:
            if values in everything.income[income]:
                empty.append(values)
        return empty



def main ():
    everything = (read_data("worldbank_life_expectancy"))
    print("Total number of entites:", everything.entities)
    print("Number of countries/territories", everything.countries)
    print ("\n")
    print("Regions and their country count:")
    print("Middle East & North Africa:", len(everything.regions["Middle East & North Africa"]))
    print("Europe & Central Asia:", len(everything.regions["Europe & Central Asia"]))
    print("North America:", len(everything.regions["North America"]))
    print("Latin America & Caribbean:", len(everything.regions["Latin America & Caribbean"]))
    print("South Asia:", len(everything.regions["South Asia"]))
    print("East Asia & Pacific:", len(everything.regions["East Asia & Pacific"]))
    print("Sub-Saharan Africa:", len(everything.regions["Sub-Saharan Africa"]))
    print("\n")
    print("Income categories and their country count:")
    print("Upper middle income:", len(everything.income["Upper middle income"]))
    print("Lower middle income:", len(everything.income["Lower middle income"]))
    print("High income:", len(everything.income["High income"]))
    print("Low income", len(everything.income["Low income"]))

    area = input("Enter region name: ")
    print("\n")
    region = filter_region(everything, area)
    if region != None:
        if area == "All" or area == "all":
            print("Countries in all regions:")
            for values in region:
                print (values + " " + "(" + everything.cnty[values] + ")")

        else:
            print ("countries in the" +" " + area + " " + "region:" )
            for country in region:
                print(country + " " + "(" + everything.cnty[country] + ")")
    money = input("Enter income category: ")
    incomes = filter_income(everything, money)
    if incomes != None:
        if money == "All" or money == "all":
            print("Countries in all income categories")
            for values in incomes:
                print(values + " " + "(" + everything.cnty[values] + ")")

        else:
            print ("countries in the" + " " + money + " " + "income category:" )
            for country in incomes:
                print(country + " " + "(" + everything.cnty[country] + ")")
    userinput = input("Enter name of country or country code (Enter to quit): ")

    if userinput in everything.CO.keys():
        num = 1960
        for year in everything.life[everything.CO[userinput]]:
            if year == "":
                num += 1
            else:
                print("Year:", num, "Life expectancy:", year)
                num += 1
    elif userinput in everything.cnty.keys():
        num = 1960
        for year in everything.life[userinput]:
            if year == "":
                print("Year:", num, "Insufficent information")
                num += 1
            else:
                print("Year:", num, "Life expectancy:", year)
                num += 1
    else:
        print(userinput + " "+ "is not a  valid country or country code")


if __name__ == "__main__":
    main()




