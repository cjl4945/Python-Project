"""factors.py
author: Chase Lewis
created: November 2017
CSCI-141"""



from utils import *
from ranking import *
import turtle as t


def medians():
    """
    medians filters the income categories and regions and get their medians per year
    param: None
    return: list  medians of each region and income category for each year from 1960 to 2015
    """
    everything = (read_data("worldbank_life_expectancy"))
    medhigh = []
    medupper = []
    medlowermid = []
    medlow = []
    medSubafrica = []
    medmidEast = []
    medEurope = []
    medNA = []
    medlatin = []
    medSAsia = []
    medEastasia = []
    year0 = 1960
    while year0 <= 2015:
        tempList = []
        data = filter_income(everything, "High income")
        new = sorted_ranking_data(data , year0)
        year0 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medhigh.append(med)
    year1 = 1960
    while year1 <= 2015:
        tempList = []
        data = filter_income(everything, "Upper middle income")
        new = sorted_ranking_data(data, year1)
        year1 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medupper.append(med)
    year2 = 1960
    while year2 <= 2015:
        tempList = []
        data = filter_income(everything, "Lower middle income")
        new = sorted_ranking_data(data, year2)
        year2 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medlowermid.append(med)
    year3 = 1960
    while year3 <= 2015:
        tempList = []
        data = filter_income(everything, "Low income")
        new = sorted_ranking_data(data, year3)
        year3 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medlow.append(med)
    year4 = 1960
    while year4 <= 2015:
        tempList = []
        data = filter_region(everything, "Sub-Saharan Africa")
        new = sorted_ranking_data(data, year4)
        year4 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medSubafrica.append(med)
    year5 = 1960
    while year5 <= 2015:
        tempList = []
        data = filter_region(everything, "Middle East & North Africa")
        new = sorted_ranking_data(data, year5)
        year5 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medmidEast.append(med)
    year6 = 1960
    while year6 <= 2015:
        tempList = []
        data = filter_region(everything, "Europe & Central Asia")
        new = sorted_ranking_data(data, year6)
        year6 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medEurope.append(med)
    year7 = 1960
    while year7 <= 2015:
        tempList = []
        data = filter_region(everything, "North America")
        new = sorted_ranking_data(data, year7)
        year7 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medNA.append(med)
    year8 = 1960
    while year8 <= 2015:
        tempList = []
        data = filter_region(everything, "Latin America & Caribbean")
        new = sorted_ranking_data(data, year8)
        year8 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medlatin.append(med)
    year9 = 1960
    while year9 <= 2015:
        tempList = []
        data = filter_region(everything, "South Asia")
        new = sorted_ranking_data(data, year9)
        year9 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medSAsia.append(med)
    year10 = 1960
    while year10 <= 2015:
        tempList = []
        data = filter_region(everything, "East Asia & Pacific")
        new = sorted_ranking_data(data, year10)
        year10 += 1
        for i in range(0,len(new)):
            tempList.append(new[i].value)
        med = median(tempList)
        medEastasia.append(med)

    return medhigh,medupper, medlowermid, medlow, medSubafrica, medmidEast, medEurope, medNA, medlatin, medSAsia, medEastasia




def median(lst):
    """

    :param lst:
    :return: median of lst
    """
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0




def initIncome():
    """

    :return: a canvas of a line graph with title axises
    """
    t.up()
    t.setpos(-250,-250)
    t.down()
    t.setpos(250,-250)
    t.up()
    t.setpos(-250,-250)
    t.left(90)
    t.down()
    t.setpos(-250,250)
    t.up()
    t.setpos(-270,-250)
    t.write(0, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,-200)
    t.down()
    t.write(10, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,-150)
    t.down()
    t.write(20, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,-100)
    t.down()
    t.write(30, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,-50)
    t.down()
    t.write(40, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,0)
    t.down()
    t.write(50, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,50)
    t.down()
    t.write(60, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,100)
    t.down()
    t.write(70, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,150)
    t.down()
    t.write(80, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270,200)
    t.down()
    t.write(90, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-250,-270)
    t.down()
    t.write(1960, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(250,-270)
    t.write(2015, move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(0,-270)
    t.write("Year", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-300,0)
    t.write("Life \nExp.", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(0,250)
    t.down()
    t.right(90)
    t.pensize(3)
    t.pencolor("red")
    t.forward(30)
    t.up()
    t.setpos(0,260)
    t.pencolor("blue")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(0, 270)
    t.pencolor("orange")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(0, 280)
    t.pencolor("green")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(-230,280)
    t.color("green")
    t.write("High income", move=False, align="left", font=("Arial",11, "normal"))
    t.setpos(-230,270)
    t.color("orange")
    t.write("Upper middle income", move=False, align="left", font=("Arial",11, "normal"))
    t.setpos(-230, 260)
    t.color("blue")
    t.write("Lower middle income", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-230, 250)
    t.color("red")
    t.write("Low income", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()

def incomegraph(data):
    """

    :param data:
    :return: Line graphs for each income category
    """
    t.up()
    x= -250
    t.pencolor("green")
    t.up()
    for values in data[0]:
        t.setpos(x,(5 * values)- 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("orange")
    t.up()
    for values in data[1]:
        t.setpos(x, (5 * values)- 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("blue")
    t.up()
    for values in data[2]:
        t.setpos(x, (5 * values)- 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("red")
    t.up()
    for values in data[3]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()

def initregion():
    """Draws the canvas for the region medians

    :return:a canvas of a line graph with title axises
    """
    t.pencolor("black")
    t.up()
    t.setpos(-250, -250)
    t.down()
    t.setpos(250, -250)
    t.up()
    t.setpos(-250, -250)
    t.left(90)
    t.down()
    t.setpos(-250, 250)
    t.up()
    t.setpos(-270, -250)
    t.write(0, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, -200)
    t.down()
    t.write(10, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, -150)
    t.down()
    t.write(20, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, -100)
    t.down()
    t.write(30, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, -50)
    t.down()
    t.write(40, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, 0)
    t.down()
    t.write(50, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, 50)
    t.down()
    t.write(60, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, 100)
    t.down()
    t.write(70, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, 150)
    t.down()
    t.write(80, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-270, 200)
    t.down()
    t.write(90, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-250, -270)
    t.down()
    t.write(1960, move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(250, -270)
    t.write(2015, move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(0, -270)
    t.write("Year", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-300, 0)
    t.write("Life \nExp.", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(0, 220)
    t.down()
    t.right(90)
    t.pensize(3)
    t.pencolor("red")
    t.forward(30)
    t.up()
    t.setpos(0, 230)
    t.pencolor("blue")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(0, 240)
    t.pencolor("orange")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(0, 250)
    t.pencolor("green")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(0, 260)
    t.down()
    t.pensize(3)
    t.pencolor("purple")
    t.forward(30)
    t.up()
    t.setpos(0, 270)
    t.pencolor("yellow")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(0, 280)
    t.pencolor("pink")
    t.down()
    t.forward(30)
    t.up()
    t.setpos(-230, 250)
    t.color("green")
    t.write("Sub-Saharan Africa", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-230, 240)
    t.color("orange")
    t.write("Middle East & North Africa", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-230, 230)
    t.color("blue")
    t.write("Europe & Central Asia", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-230, 220)
    t.color("red")
    t.write("North America", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.setpos(-230, 260)
    t.color("purple")
    t.write("Latin America & Caribbean", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-230, 270)
    t.color("yellow")
    t.write("South Asia", move=False, align="left", font=("Arial", 11, "normal"))
    t.setpos(-230, 280)
    t.color("pink")
    t.write("East Asia & Pacific", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()


def regiongraph(data):
    """

    :param data:
    :return: Line graphs for each income category
    """
    t.up()
    x = -250
    t.pencolor("green")
    t.up()
    for values in data[4]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("orange")
    t.up()
    for values in data[5]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("blue")
    t.up()
    for values in data[6]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("red")
    t.up()
    for values in data[7]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("purple")
    t.up()
    for values in data[8]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("yellow")
    t.up()
    for values in data[9]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()
    x = -250
    t.pencolor("pink")
    t.up()
    for values in data[10]:
        t.setpos(x, (5 * values) - 250)
        t.down()
        x += 9.09
    t.up()









def main():
    data = medians()
    initIncome()
    incomegraph(data)
    input("Press enter to continue")
    t.clear()
    initregion()
    regiongraph(data)
    t.done()

if __name__ == "__main__":

    main()