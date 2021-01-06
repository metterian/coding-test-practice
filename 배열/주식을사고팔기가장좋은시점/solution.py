# %% [markdown]
# ```
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             # Not 7-1 = 6, as selling price needs to be larger than buying price.
# ```
# %%
# 브루트 포스로 계산 -> 시간 초과
from typing import *
def maxProfit(prices: List[int]) -> int:
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i+1, len(prices)):
            max_price = max(max_price,   prices[j] - price)
    return max_price

maxProfit(prices= [7,1,5,3,6,4])
# %%
# 지점과 현재 값과의 차이 계산

import sys
from typing import *
def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price- min_price)
    return profit
maxProfit(prices= [7,1,5,3,6,4])
# %%
