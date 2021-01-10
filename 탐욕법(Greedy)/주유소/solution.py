#%%
import sys
n =5
road = [3, 2, 1, 4]
price = [5, 8, 9, 4, 1]
# %%

total = price[0] * road[0]
min_price = price[0]


for i in range(1, n-1):
    min_price = min(min_price, price[i])
    total += min_price*road[i]

print(total)

# %%
