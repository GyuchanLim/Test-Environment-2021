import csv
import copy
import datetime
import matplotlib.pyplot as plt

priceList = []
every_4_years = []
halving_dates = ['2012-11','2016-07','2020-05','TBD']

non_zero = True
def open_CSV(fileName):
    with open(fileName, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[0] == 'ï»¿Timestamp':
                continue
            else:
                time, price = row
                # print(time)
                # print(price)
                dt_obj = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                #print(type(row[0])) TIME IN ARRAY IS STRING
                if non_zero:
                    if price != '0':
                        priceList.append([dt_obj,price])
                else:
                    priceList.append([row[0],price])
            if halving_dates[0] == row[0][:7]:
                #print("TESTING")
                every_4_years.append(copy.deepcopy(priceList))
                priceList.clear()
                halving_dates.remove(halving_dates[0])
        every_4_years.append(copy.deepcopy(priceList))
        priceList.clear()
        halving_dates.remove(halving_dates[0])
    return every_4_years


def plot_halves(datePrice):
    x=[]
    y=[]
    x1=[]
    y1=[]
    nextHalf = "24/03/27"
    creationBitcoin = "08/08/18"
    halfDate = datetime.datetime.strptime(nextHalf, "%y/%m/%d")
    creationDate = datetime.datetime.strptime(creationBitcoin, "%y/%m/%d")
    for index, dp in enumerate(datePrice):
        if index == 3:
            cmpDate = dp[-1][0] + datetime.timedelta(days=3)
            while cmpDate < halfDate:
                x1.append(cmpDate)
                y1.append(0)
                cmpDate += datetime.timedelta(days=3)
            for date,price in datePrice[index]:
                #print(price)
                x.append(date)
                y.append(float(price))
            x = x + x1
            y = y + y1
            x1.clear()
            y1.clear()
        elif index == 0:
            cmpDate = dp[0][0]
            count = 0
            while creationDate < cmpDate:
                x1.append(creationDate)
                y1.append(0)
                count+=1
                creationDate += datetime.timedelta(days=3)
            for date,price in datePrice[index]:
                #print(price)
                x.append(date)
                y.append(float(price))
            x = x1 + x
            y = y1 + y
            print(count)
            x1.clear()
            y1.clear()
        else:
            for date,price in datePrice[index]:
                #print(price)
                x.append(date)
                y.append(float(price))
        plt.figure()
        plt.plot(x,y)
        plt.gcf().autofmt_xdate()
        print(len(x),len(y))
        x.clear()
        y.clear()
    plt.show()
halves = open_CSV('CSV\BTCPrice.csv')
plot_halves(halves)
#print(len(every_4_years))