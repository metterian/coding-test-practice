#%%
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
# %%
import math

max_num = -math.inf
min_num = math.inf

loc = 0
def dfs(add, sub, mul, div, num):
    global max_num, min_num, loc

    if loc > n-2:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    else:
        if add:
            loc += 1
            dfs(add-1, sub, mul, div, num+numbers[loc])
            loc -= 1
        if sub:
            loc += 1
            dfs(add, sub-1, mul, div, num-numbers[loc])
            loc -= 1
        if mul:
            loc += 1
            dfs(add, sub, mul-1, div, num*numbers[loc])
            loc -= 1
        if div:
            loc += 1
            dfs(add, sub, mul, div-1, int(num/numbers[loc]))
            loc -= 1


dfs(add,sub, mul, div, numbers[0])
print(max_num, min_num)



# %%
