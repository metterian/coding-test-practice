
#%%
import numpy as np
n = 20
battery = [[6,30000],[3,18000],[4,28000],[1,9500]]
battery = sorted(battery, key=lambda x: x[1]/x[0], reverse=False)
S, P = [i for i,_ in battery], [v for _, v in battery]
price_by_S =[ p/s for s, p in battery]
x = [0]*len(battery)

#%%
def solution(n, battery):
    battery = sorted(battery, key=lambda x: x[1]/x[0], reverse=False)
    S, P = [i for i,_ in battery], [v for _, v in battery]
    price_by_S =[ p/s for s, p in battery]
    rest_s = n%S[0]
    for s in S[1::]:
        num = s
        price
        while(rest_s >= num):





    return answer

#%%

# %%

# %%

# %%
