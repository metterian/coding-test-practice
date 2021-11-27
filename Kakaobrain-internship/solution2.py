

"""
https://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>

"""


#%%

def url(city, pageNumber):
    return f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={pageNumber}"




# %%
import requests


city = 'Omaha'
total_pages = requests.get(url=url(city, 1)).json()['total_pages']

resto = []
for page in range(1, total_pages+1):
    data = requests.get(url=url(city, page)).json()['data']
    for info in data:
        # resto[info['name']] = info['user_rating']['average_rating']
        resto.append([info['name'], info['user_rating']['average_rating']])
#%%
sorted_resto = sorted(resto, key=lambda x: x[1], reverse=True)
max_rate = sorted_resto[0][1]
for rest, rate in sorted_resto:
    if rate >= max_rate:
        print(rest)

# %%
