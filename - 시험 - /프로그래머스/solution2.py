#%%
purchase =["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]

import datetime
from datetime import timedelta
def solution(purchase):
    calender = [0] * (365+1)
    start = datetime.datetime.strptime('20190101', '%Y%m%d')

    data = []
    for value in purchase:
        date_str, price = value.split(' ')
        data.append([datetime.datetime.strptime(date_str, '%Y/%m/%d'), int(price)])

    for date, price in data:
        for i in range((date-start).days+1, (date-start).days+31):
            if  i > len(calender) -1:
                break
            calender[i] += price


    bronze = 0
    silver = 0
    gold = 0
    platinum = 0
    diamond = 0


    for price in calender[1:]:
        if 0<= price <10000:
            bronze += 1
        elif 10000 <= price < 20000:
            silver +=1
        elif 20000 <= price < 50000:
            gold += 1
        elif 50000 <= price < 100000:
            platinum += 1
        else:
            diamond += 1

    return ([bronze, silver, gold, platinum, diamond])


solution(purchase)
# %%
