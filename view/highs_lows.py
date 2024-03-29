import csv
from datetime import datetime
from matplotlib import pyplot as plt


# filename="sitka_weather_07-2014.csv"
# filename="sitka_weather_2014.csv"
#有空数据
filename="death_valley_2014.csv"
with open(filename) as f:
    reader=csv.reader(f)
    head_row=next(reader)
    # for index,column_header in enumerate(head_row):
    #     print(index,column_header)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,"missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(highs)

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

# plt.title("Daily high temperature, July 2014",fontsize=24)
# plt.title("Daily high and low temperature, - 2014",fontsize=24)
plt.title("Daily high and low temperature, Death Valley- 2014",fontsize=20)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature(F)",fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=16)
plt.show()


