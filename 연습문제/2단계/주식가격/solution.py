#%%

prices = [1, 2, 3, 2, 3]

stack = []
answer = [0] * len(prices)
# %%
for i, cur_price in enumerate(prices):
    while stack and cur_price < prices[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)

for i in stack:
    answer[i] = (len(prices) - 1) - i
# %%
