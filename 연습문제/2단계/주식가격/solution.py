#%%
from collections import deque
# %%
prices = [1, 2, 3, 2, 3]
queue = deque([])

for day, price in enumerate(prices):
    queue.append([day+1, price, 0])


#%%

def solution(prices):
    for i in range(1, len(prices)):
        for _ in range(len(prices)):
            day, price, hold = queue.popleft()
            if price <= prices[i]:
                queue.append([day, price, hold+1])
            else:
                queue.append([day, price, hold])
    return queue
solution(prices)




# %%
